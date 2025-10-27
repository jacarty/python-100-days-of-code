from datetime import date
from flask import Flask, abort, render_template, redirect, url_for, flash, request, jsonify
from flask_bootstrap import Bootstrap5
from flask_login import UserMixin, login_user, LoginManager, current_user, logout_user, login_required
from flask_sqlalchemy import SQLAlchemy
from sqlalchemy.orm import relationship, DeclarativeBase, Mapped, mapped_column
from sqlalchemy import Integer, String, Text, Float
from functools import wraps
from werkzeug.security import generate_password_hash, check_password_hash
from forms import RegisterForm, LoginForm
from notifications import NotificationManager


#######################################
# Configure App
#######################################
app = Flask(__name__)
app.config['SECRET_KEY'] = ''
Bootstrap5(app)


#######################################
# Configure Login Elements
#######################################
login_manager = LoginManager()
login_manager.init_app(app)

@login_manager.user_loader
def load_user(user_id):
    return db.get_or_404(Users, user_id)


#######################################
# Create and Connect DB
#######################################
class Base(DeclarativeBase):
    pass

# Connect to Database
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///tasks.db'
db = SQLAlchemy(model_class=Base)
db.init_app(app)


#######################################
# Database Models
#######################################
class Users(UserMixin, db.Model):
    __tablename__ = "users"
    id: Mapped[int] = mapped_column(Integer, primary_key=True)
    name: Mapped[str] = mapped_column(String(250), nullable=False)
    email: Mapped[str] = mapped_column(String(250), nullable=False, unique=True)
    password: Mapped[str] = mapped_column(String(1000), nullable=False)
    
    # Relationship to tasks
    tasks = relationship("Tasks", back_populates="author")


class Tasks(db.Model):
    __tablename__ = "tasks"
    id: Mapped[int] = mapped_column(Integer, primary_key=True)
    
    # Foreign key to users table
    author_id: Mapped[int] = mapped_column(Integer, db.ForeignKey("users.id"), nullable=True)
    
    # Task fields
    date: Mapped[str] = mapped_column(String(250), nullable=False)
    task_name: Mapped[str] = mapped_column(String(250), nullable=False)
    task_detail: Mapped[str] = mapped_column(Text, nullable=False)
    task_effort: Mapped[float] = mapped_column(Float, nullable=False)
    task_img: Mapped[str] = mapped_column(String(500), nullable=True)
    
    # Status for Kanban board (e.g., "To Do", "In Progress", "Done")
    status: Mapped[str] = mapped_column(String(50), nullable=False, default="To Do")
    
    # Relationship to users
    author = relationship("Users", back_populates="tasks")


with app.app_context():
    db.create_all()


#######################################
# Admin-only decorator
#######################################
def admin_only(f):
    @wraps(f)
    def decorated_function(*args, **kwargs):
        # If user is not logged in or id is not 1, abort with 403 error
        if not current_user.is_authenticated or current_user.id != 1:
            return abort(403)
        # Otherwise continue with the route function
        return f(*args, **kwargs)
    return decorated_function


#######################################
# User Routes
#######################################
@app.route('/register', methods=["GET", "POST"])
def register():
    form = RegisterForm()

    if form.validate_on_submit():
        email_add = form.email.data
        result = db.session.execute(db.select(Users).where(Users.email == email_add))
        user = result.scalar()

        if user:
            flash("You've already signed up with that email, log in instead!")
            return redirect(url_for("login"))
        else:
            hash_and_salted_password = generate_password_hash(
                form.password.data,
                method='pbkdf2:sha256',
                salt_length=8
            )
            new_user = Users(
                email=email_add,
                name=form.name.data,
                password=hash_and_salted_password,
            )
            
            db.session.add(new_user)
            db.session.commit()
            login_user(new_user)

            return redirect(url_for("tasks"))
    
    return render_template("register.html", form=form, logged_in=current_user.is_authenticated)


@app.route('/login', methods=["GET", "POST"])
def login():
    form = LoginForm()

    if form.validate_on_submit():
        email = form.email.data
        password = form.password.data
        
        # Find user by email 
        result = db.session.execute(db.select(Users).where(Users.email == email))
        user = result.scalar()

        if not user:
            flash("That email does not exist, please try again.")
            return redirect(url_for('login'))
        elif not check_password_hash(user.password, password):
            flash('Password incorrect, please try again.')
            return redirect(url_for('login'))
        else:
            login_user(user)
            return redirect(url_for('tasks'))

    return render_template("login.html", form=form, logged_in=current_user.is_authenticated)


@app.route('/logout')
@login_required
def logout():
    logout_user()
    return redirect(url_for('home'))


#######################################
# Home Page
#######################################
@app.route("/")
def home():
    return render_template("index.html", logged_in=current_user.is_authenticated)


#######################################
# Show All Tasks (Kanban Board)
#######################################
@app.route("/tasks")
@login_required
def tasks():
    # Get all tasks for current user
    all_tasks = db.session.execute(
        db.select(Tasks).where(Tasks.author_id == current_user.id).order_by(Tasks.date)
    ).scalars().all()
    
    # Organize tasks by status for Kanban board
    kanban_tasks = {
        "To Do": [],
        "In Progress": [],
        "Done": []
    }
    
    for task in all_tasks:
        if task.status in kanban_tasks:
            kanban_tasks[task.status].append(task)
    
    return render_template("tasks.html", kanban_tasks=kanban_tasks, logged_in=current_user.is_authenticated)


#######################################
# Get Task as JSON (for Edit Modal)
#######################################
@app.route("/api/tasks/<int:task_id>", methods=["GET"])
@login_required
def get_task(task_id):
    """Get a single task as JSON"""
    task = db.session.get(Tasks, task_id)
    
    if task is None:
        return jsonify(error={"Not Found": "Task not found."}), 404
    
    # Ensure user can only get their own tasks
    if task.author_id != current_user.id:
        return jsonify(error={"Forbidden": "Not authorized."}), 403
    
    # Return task data as JSON
    return jsonify({
        "id": task.id,
        "task_name": task.task_name,
        "task_detail": task.task_detail,
        "task_effort": task.task_effort,
        "task_img": task.task_img or "",
        "status": task.status,
        "date": task.date
    }), 200


#######################################
# Add Task
#######################################
@app.route("/api/tasks", methods=["POST"])
@login_required
def add_task():
    # Accept both form data and JSON
    if request.is_json:
        data = request.get_json()
        task_name = data.get("name")
        task_detail = data.get("details")
        task_effort = data.get("effort")
        task_img = data.get("img_url", "")
        status = data.get("status", "To Do")
    else:
        task_name = request.form.get("name")
        task_detail = request.form.get("details")
        task_effort = request.form.get("effort")
        task_img = request.form.get("img_url", "")
        status = request.form.get("status", "To Do")
    
    new_task = Tasks(
        author_id=current_user.id,
        date=date.today().strftime("%B %d, %Y"),
        task_name=task_name,
        task_detail=task_detail,
        task_effort=float(task_effort),
        task_img=task_img,
        status=status
    )
    
    db.session.add(new_task)
    db.session.commit()
    
    return jsonify(response={"success": "Successfully added the new task."}), 201


#######################################
# Update Task
#######################################
@app.route("/api/tasks/<int:task_id>", methods=["PATCH", "PUT"])
@login_required
def update_task(task_id):
    """Update fields of a task"""
    task = db.session.get(Tasks, task_id)
    
    if task is None:
        return jsonify(error={"Not Found": "Sorry, a task with that id was not found in the database."}), 404
    
    # Ensure user can only update their own tasks
    if task.author_id != current_user.id:
        return jsonify(error={"Forbidden": "You can only update your own tasks."}), 403
    
    # Get JSON data from request
    data = request.get_json()
    
    # Update fields if provided
    if data.get('name'):
        task.task_name = data.get('name')
    if data.get('details'):
        task.task_detail = data.get('details')
    if data.get('effort'):
        task.task_effort = float(data.get('effort'))
    if data.get('img_url') is not None:
        task.task_img = data.get('img_url')
    if data.get('status'):
        task.status = data.get('status')
        
    db.session.commit()
    
    return jsonify(response={"success": "Successfully updated the task."}), 200


#######################################
# Update Task Status (for Kanban drag)
#######################################
@app.route("/api/tasks/<int:task_id>/status", methods=["PATCH"])
@login_required
def update_task_status(task_id):
    """Quick update for task status (used for Kanban board)"""
    task = db.session.get(Tasks, task_id)
    
    if task is None:
        return jsonify(error={"Not Found": "Task not found."}), 404
    
    if task.author_id != current_user.id:
        return jsonify(error={"Forbidden": "Not authorized."}), 403
    
    data = request.get_json()
    new_status = data.get('status')
    
    if new_status in ["To Do", "In Progress", "Done"]:
        task.status = new_status
        db.session.commit()
        return jsonify(response={"success": "Status updated."}), 200
    else:
        return jsonify(error={"Bad Request": "Invalid status."}), 400


#######################################
# Delete Task
#######################################
@app.route("/api/tasks/<int:task_id>", methods=["DELETE"])
@login_required
def delete_task(task_id):
    task = db.session.get(Tasks, task_id)
    
    if task is None:
        return jsonify(error={"Not Found": "Sorry, a task with that id was not found in the database."}), 404
    
    # Ensure user can only delete their own tasks
    if task.author_id != current_user.id:
        return jsonify(error={"Forbidden": "You can only delete your own tasks."}), 403
    
    db.session.delete(task)
    db.session.commit()
    
    return jsonify(response={"success": "Successfully deleted the task from the database."}), 200


#######################################
# Contact Form
#######################################
@app.route("/api/contact", methods=["POST"])
def contact():
    """Handle contact form submissions"""
    data = request.get_json()
    name = data.get("name")
    email = data.get("email")
    phone = data.get("phone", "Not provided")
    subject = data.get("subject")
    message = data.get("message")
    
    if not all([name, email, subject, message]):
        return jsonify(error={"Bad Request": "Missing required fields"}), 400
    
    try:
        notification_manager = NotificationManager()
        result = notification_manager.send_email(name, email, phone, subject, message)
        return jsonify(response={"success": result}), 200
    except Exception as e:
        return jsonify(error={"Server Error": str(e)}), 500


#######################################
# Init App
#######################################
if __name__ == '__main__':
    app.run(debug=True)