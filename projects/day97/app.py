from flask import Flask, render_template, request, redirect, url_for, session, flash, jsonify
from flask_login import LoginManager, login_user, logout_user, login_required, current_user
from models import db, User, Admin, Address, Product, Order, OrderItem
import stripe
import os
from dotenv import load_dotenv
from functools import wraps

load_dotenv("../../.env")

app = Flask(__name__)
app.config['SECRET_KEY'] = os.getenv('DB_SECRET_KEY')
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///store.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

# Stripe configuration
stripe.api_key = os.getenv('STRIPE_SECRET_KEY')
STRIPE_PUBLISHABLE_KEY = os.getenv('STRIPE_PUBLISHABLE_KEY')
db.init_app(app)

# Flask-Login setup
login_manager = LoginManager()
login_manager.init_app(app)
login_manager.login_view = 'login'

@login_manager.user_loader
def load_user(user_id):
    return User.query.get(int(user_id))

def admin_required(f):
    @wraps(f)
    def decorated_function(*args, **kwargs):
        if not current_user.is_authenticated or not current_user.is_admin():
            flash('You need admin privileges to access this page.', 'danger')
            return redirect(url_for('index'))
        return f(*args, **kwargs)
    return decorated_function

# ==================== HELPER FUNCTIONS ====================

def get_cart():
    """Get cart from session, initialize if doesn't exist"""
    if 'cart' not in session:
        session['cart'] = {}
    return session['cart']

def get_cart_total():
    """Calculate total price of items in cart"""
    cart = get_cart()
    total = 0
    for product_id, quantity in cart.items():
        product = Product.query.get(int(product_id))
        if product:
            total += product.price * quantity
    return total

def get_cart_items():
    """Get full product details for items in cart"""
    cart = get_cart()
    items = []
    for product_id, quantity in cart.items():
        product = Product.query.get(int(product_id))
        if product:
            items.append({
                'product': product,
                'quantity': quantity,
                'subtotal': product.price * quantity
            })
    return items

def validate_cart_stock():
    """
    Check if cart items are in stock and adjust quantities if needed.
    Returns dict of products that were adjusted or out of stock.
    """
    cart = get_cart()
    adjustments = {}
    
    for product_id, quantity in list(cart.items()):
        product = Product.query.get(int(product_id))
        
        if not product:
            # Product no longer exists
            cart.pop(product_id)
            adjustments[product_id] = {'status': 'removed', 'reason': 'Product no longer available'}
            continue
        
        if product.stock == 0:
            # Out of stock - remove from cart
            cart.pop(product_id)
            adjustments[product_id] = {
                'status': 'removed',
                'reason': f'{product.name} is out of stock',
                'product': product
            }

        elif product.stock < quantity:
            # Not enough stock - adjust quantity
            old_quantity = quantity
            cart[product_id] = product.stock
            adjustments[product_id] = {
                'status': 'adjusted',
                'old_quantity': old_quantity,
                'new_quantity': product.stock,
                'product': product
            }
    
    session['cart'] = cart
    return adjustments


# ==================== ROUTES ====================

@app.route('/')
def index():
    products = Product.query.all()
    return render_template('index.html', products=products)

@app.route('/product/<int:product_id>')
def product_detail(product_id):
    product = Product.query.get_or_404(product_id)
    in_stock = product.stock > 0
    return render_template('product.html', product=product, in_stock=in_stock)


# ==================== CART ROUTES ====================

@app.route('/cart')
def view_cart():
    # Validate stock availability
    adjustments = validate_cart_stock()
    
    # Show flash messages for adjustments
    for product_id, info in adjustments.items():
        if info['status'] == 'removed':
            flash(info['reason'], 'warning')
        elif info['status'] == 'adjusted':
            flash(f"{info['product'].name} quantity adjusted from {info['old_quantity']} to {info['new_quantity']} (limited stock)", 'info')
    
    items = get_cart_items()
    total = get_cart_total()
    return render_template('cart.html', items=items, total=total)

@app.route('/cart/add/<int:product_id>', methods=['POST'])
def add_to_cart(product_id):
    product = Product.query.get_or_404(product_id)
    quantity = int(request.form.get('quantity', 1))
    
    cart = get_cart()
    product_id_str = str(product_id)
    
    if product_id_str in cart:
        cart[product_id_str] += quantity
    else:
        cart[product_id_str] = quantity
    
    session['cart'] = cart  # Save back to session
    flash(f'Added {product.name} to cart!', 'success')
    return redirect(url_for('view_cart'))

@app.route('/cart/update/<int:product_id>', methods=['POST'])
def update_cart(product_id):
    quantity = int(request.form.get('quantity', 0))
    cart = get_cart()
    product_id_str = str(product_id)
    
    if quantity > 0:
        cart[product_id_str] = quantity
    else:
        cart.pop(product_id_str, None)
    
    session['cart'] = cart
    return redirect(url_for('view_cart'))

@app.route('/cart/remove/<int:product_id>')
def remove_from_cart(product_id):
    cart = get_cart()
    cart.pop(str(product_id), None)
    session['cart'] = cart
    flash('Item removed from cart', 'info')
    return redirect(url_for('view_cart'))


# ==================== ADDRESS ROUTES ====================

@app.route('/addresses')
@login_required
def manage_addresses():
    addresses = Address.query.filter_by(user_id=current_user.id).all()
    return render_template('user/addresses.html', addresses=addresses)

@app.route('/addresses/add', methods=['GET', 'POST'])
@login_required
def add_address():
    if request.method == 'POST':
        # If this is set as default, unset all other defaults
        is_default = request.form.get('is_default') == 'on'
        if is_default:
            Address.query.filter_by(user_id=current_user.id, is_default=True).update({'is_default': False})
        
        address = Address(
            user_id=current_user.id,
            name=request.form.get('name'),
            street=request.form.get('street'),
            city=request.form.get('city'),
            state=request.form.get('state'),
            postal_code=request.form.get('postal_code'),
            country=request.form.get('country'),
            is_default=is_default
        )
        db.session.add(address)
        db.session.commit()
        flash('Address added successfully!', 'success')
        return redirect(url_for('manage_addresses'))
    
    return render_template('user/address_form.html', address=None)

@app.route('/addresses/edit/<int:address_id>', methods=['GET', 'POST'])
@login_required
def edit_address(address_id):
    address = Address.query.get_or_404(address_id)
    
    # Make sure user owns this address
    if address.user_id != current_user.id:
        flash('Unauthorized access', 'danger')
        return redirect(url_for('manage_addresses'))
    
    if request.method == 'POST':
        # If this is set as default, unset all other defaults
        is_default = request.form.get('is_default') == 'on'
        if is_default:
            Address.query.filter_by(user_id=current_user.id, is_default=True).update({'is_default': False})
        
        address.name = request.form.get('name')
        address.street = request.form.get('street')
        address.city = request.form.get('city')
        address.state = request.form.get('state')
        address.postal_code = request.form.get('postal_code')
        address.country = request.form.get('country')
        address.is_default = is_default
        
        db.session.commit()
        flash('Address updated successfully!', 'success')
        return redirect(url_for('manage_addresses'))
    
    return render_template('user/address_form.html', address=address)

@app.route('/addresses/delete/<int:address_id>')
@login_required
def delete_address(address_id):
    address = Address.query.get_or_404(address_id)
    
    # Make sure user owns this address
    if address.user_id != current_user.id:
        flash('Unauthorized access', 'danger')
        return redirect(url_for('manage_addresses'))
    
    db.session.delete(address)
    db.session.commit()
    flash('Address deleted', 'info')
    return redirect(url_for('manage_addresses'))


# ==================== CHECKOUT ROUTES ====================

@app.route('/checkout', methods=['GET', 'POST'])
@login_required
def checkout():
    items = get_cart_items()
    if not items:
        flash('Your cart is empty', 'warning')
        return redirect(url_for('index'))
    
    # Validate stock before checkout
    adjustments = validate_cart_stock()
    if adjustments:
        flash('Your cart was updated due to stock availability. Please review before continuing.', 'warning')
        return redirect(url_for('view_cart'))
    
    addresses = Address.query.filter_by(user_id=current_user.id).all()
    default_address = current_user.get_default_address()
    
    if request.method == 'POST':
        # Handle address selection or new address
        address_id = request.form.get('address_id')
        
        if address_id == 'new':
            # Create new address (optionally save it)
            save_address = request.form.get('save_address') == 'on'
            is_default = request.form.get('is_default') == 'on'
            
            if is_default:
                Address.query.filter_by(user_id=current_user.id, is_default=True).update({'is_default': False})
            
            address = Address(
                user_id=current_user.id if save_address else None,
                name=request.form.get('name'),
                street=request.form.get('street'),
                city=request.form.get('city'),
                state=request.form.get('state'),
                postal_code=request.form.get('postal_code'),
                country=request.form.get('country'),
                is_default=is_default if save_address else False
            )
            
            if save_address:
                db.session.add(address)
                db.session.flush()
                db.session.commit()
            
            # Store address_id in session for the Stripe callback
            session['checkout_address_id'] = address.id if save_address else None
            session['checkout_address_data'] = {
                'name': address.name,
                'street': address.street,
                'city': address.city,
                'state': address.state,
                'postal_code': address.postal_code,
                'country': address.country
            }
        else:
            # Use existing address
            session['checkout_address_id'] = int(address_id)
            session['checkout_address_data'] = None
        
        # Redirect to payment
        return redirect(url_for('process_payment'))
    
    total = get_cart_total()
    return render_template('checkout.html', 
                         items=items, 
                         total=total,
                         addresses=addresses,
                         default_address=default_address)

@app.route('/process-payment')
@login_required
def process_payment():
    """Show payment page after address is selected"""
    if 'checkout_address_id' not in session and 'checkout_address_data' not in session:
        flash('Please select a shipping address', 'warning')
        return redirect(url_for('checkout'))
    
    items = get_cart_items()
    total = get_cart_total()
    
    return render_template('payment.html',
                         items=items,
                         total=total,
                         stripe_key=STRIPE_PUBLISHABLE_KEY)

@app.route('/create-checkout-session', methods=['POST'])
@login_required
def create_checkout_session():
    cart = get_cart()
    if not cart:
        return jsonify({'error': 'Cart is empty'}), 400
    
    # Create line items for Stripe
    line_items = []
    for product_id, quantity in cart.items():
        product = Product.query.get(int(product_id))
        if product:
            line_items.append({
                'price_data': {
                    'currency': 'usd',
                    'product_data': {
                        'name': product.name,
                    },
                    'unit_amount': int(product.price * 100),
                },
                'quantity': quantity,
            })
    
    try:
        checkout_session = stripe.checkout.Session.create(
            payment_method_types=['card'],
            line_items=line_items,
            mode='payment',
            success_url=url_for('order_success', _external=True) + '?session_id={CHECKOUT_SESSION_ID}',
            cancel_url=url_for('checkout', _external=True),
        )
        return jsonify({'id': checkout_session.id})
    except Exception as e:
        return jsonify({'error': str(e)}), 400

@app.route('/order-success')
@login_required
def order_success():
    session_id = request.args.get('session_id')
    
    if session_id:
        checkout_session = stripe.checkout.Session.retrieve(session_id)
        
        if checkout_session.payment_status == 'paid':
            cart = get_cart()
            total = get_cart_total()
            
            # Handle address
            address_id = session.get('checkout_address_id')
            address_data = session.get('checkout_address_data')
            
            if not address_id and address_data:
                # Create one-time address
                address = Address(**address_data)
                db.session.add(address)
                db.session.flush()
                address_id = address.id
            
            # Create order
            order = Order(
                user_id=current_user.id,
                shipping_address_id=address_id,
                total_amount=total,
                status='paid',
                stripe_payment_intent_id=checkout_session.payment_intent
            )
            db.session.add(order)
            db.session.flush()
            
            # Create order items AND decrement stock
            for product_id, quantity in cart.items():
                product = Product.query.get(int(product_id))
                if product:
                    # Create order item
                    order_item = OrderItem(
                        order_id=order.id,
                        product_id=product.id,
                        quantity=quantity,
                        price_at_purchase=product.price
                    )
                    db.session.add(order_item)
                    
                    # Decrement stock
                    product.stock -= quantity
                    if product.stock < 0:
                        product.stock = 0  # Safety check
            
            db.session.commit()
            
            # Clear session
            session['cart'] = {}
            session.pop('checkout_address_id', None)
            session.pop('checkout_address_data', None)
            
            return render_template('order_success.html', order=order)
    
    flash('There was a problem with your order', 'danger')
    return redirect(url_for('index'))

@app.route('/orders')
@login_required
def order_history():
    orders = Order.query.filter_by(user_id=current_user.id).order_by(Order.created_at.desc()).all()
    return render_template('user/order_history.html', orders=orders)

@app.route('/orders/<int:order_id>')
@login_required
def order_detail(order_id):
    order = Order.query.get_or_404(order_id)
    
    # Make sure user owns this order
    if order.user_id != current_user.id:
        flash('Unauthorized access', 'danger')
        return redirect(url_for('order_history'))
    
    return render_template('user/order_detail.html', order=order)


# ==================== AUTH ROUTES ====================

@app.route('/register', methods=['GET', 'POST'])
def register():
    if request.method == 'POST':
        email = request.form.get('email')
        password = request.form.get('password')
        name = request.form.get('name')
        
        if User.query.filter_by(email=email).first():
            flash('Email already registered', 'danger')
            return redirect(url_for('register'))
        
        user = User(email=email, name=name)
        user.set_password(password)
        db.session.add(user)
        db.session.commit()
        
        # Make first user an admin
        if User.query.count() == 1:
            admin = Admin(user_id=user.id)
            db.session.add(admin)
            db.session.commit()
            flash('Registration successful! You are now an admin.', 'success')
        else:
            flash('Registration successful!', 'success')
        
        login_user(user)
        return redirect(url_for('index'))
    
    return render_template('register.html')

@app.route('/login', methods=['GET', 'POST'])
def login():
    if request.method == 'POST':
        email = request.form.get('email')
        password = request.form.get('password')
        
        user = User.query.filter_by(email=email).first()
        
        if user and user.check_password(password):
            login_user(user)
            flash('Logged in successfully!', 'success')
            return redirect(url_for('index'))
        else:
            flash('Invalid email or password', 'danger')
    
    return render_template('login.html')

@app.route('/logout')
@login_required
def logout():
    logout_user()
    flash('Logged out successfully', 'info')
    return redirect(url_for('index'))


# ==================== ADMIN/SETUP ====================

@app.route('/admin')
@login_required
@admin_required
def admin_dashboard():
    products = Product.query.all()
    orders = Order.query.order_by(Order.created_at.desc()).limit(10).all()
    total_revenue = db.session.query(db.func.sum(Order.total_amount)).filter_by(status='paid').scalar() or 0
    return render_template('admin/dashboard.html', 
                         products=products, 
                         orders=orders,
                         total_revenue=total_revenue)

@app.route('/admin/products/add', methods=['GET', 'POST'])
@login_required
@admin_required
def admin_add_product():
    if request.method == 'POST':
        product = Product(
            name=request.form.get('name'),
            description=request.form.get('description'),
            price=float(request.form.get('price')),
            stock=int(request.form.get('stock')),
            image_url=request.form.get('image_url')
        )
        db.session.add(product)
        db.session.commit()
        flash('Product added successfully!', 'success')
        return redirect(url_for('admin_dashboard'))
    
    return render_template('admin/product_form.html', product=None)

@app.route('/admin/products/edit/<int:product_id>', methods=['GET', 'POST'])
@login_required
@admin_required
def admin_edit_product(product_id):
    product = Product.query.get_or_404(product_id)
    
    if request.method == 'POST':
        product.name = request.form.get('name')
        product.description = request.form.get('description')
        product.price = float(request.form.get('price'))
        product.stock = int(request.form.get('stock'))
        product.image_url = request.form.get('image_url')
        
        db.session.commit()
        flash('Product updated successfully!', 'success')
        return redirect(url_for('admin_dashboard'))
    
    return render_template('admin/product_form.html', product=product)

@app.route('/admin/products/<int:product_id>/adjust-stock', methods=['POST'])
@login_required
@admin_required
def admin_adjust_stock(product_id):
    product = Product.query.get_or_404(product_id)
    adjustment = int(request.form.get('adjustment', 0))
    
    new_stock = product.stock + adjustment
    if new_stock < 0:
        flash('Stock cannot be negative', 'danger')
    else:
        product.stock = new_stock
        db.session.commit()
        flash(f'Stock for {product.name} updated to {product.stock}', 'success')
    
    return redirect(url_for('admin_dashboard'))

@app.route('/admin/products/delete/<int:product_id>')
@login_required
@admin_required
def admin_delete_product(product_id):
    product = Product.query.get_or_404(product_id)
    db.session.delete(product)
    db.session.commit()
    flash('Product deleted', 'info')
    return redirect(url_for('admin_dashboard'))

@app.route('/admin/orders')
@login_required
@admin_required
def admin_orders():
    orders = Order.query.order_by(Order.created_at.desc()).all()
    return render_template('admin/orders.html', orders=orders)

@app.route('/admin/orders/<int:order_id>')
@login_required
@admin_required
def admin_order_detail(order_id):
    order = Order.query.get_or_404(order_id)
    return render_template('admin/order_detail.html', order=order)

@app.route('/admin/orders/<int:order_id>/update-status', methods=['POST'])
@login_required
@admin_required
def admin_update_order_status(order_id):
    order = Order.query.get_or_404(order_id)
    new_status = request.form.get('status')
    
    if new_status in ['pending', 'paid', 'shipped', 'delivered', 'cancelled']:
        order.status = new_status
        db.session.commit()
        flash(f'Order #{order.id} status updated to {new_status}', 'success')
    else:
        flash('Invalid status', 'danger')
    
    return redirect(url_for('admin_order_detail', order_id=order_id))

@app.route('/admin/seed-products')
def seed_products():
    """Add some sample products - run once to populate DB"""
    products = [
        Product(
            name='Cool T-Shirt', 
            description='A really cool t-shirt with awesome design', 
            price=29.99, 
            stock=50, 
            image_url='https://images.unsplash.com/photo-1521572163474-6864f9cf17ab?w=500'
        ),
        Product(
            name='Awesome Mug', 
            description='Coffee tastes better in this ceramic mug', 
            price=14.99, 
            stock=100,
            image_url='https://images.unsplash.com/photo-1514228742587-6b1558fcca3d?w=500'
        ),
        Product(
            name='Tech Stickers', 
            description='Pack of 10 developer and tech stickers', 
            price=9.99, 
            stock=200,
            image_url='https://images.unsplash.com/photo-1558618666-fcd25c85cd64?w=500'
        ),
        Product(
            name='Notebook', 
            description='Premium leather-bound notebook for your ideas', 
            price=12.99, 
            stock=75,
            image_url='https://images.unsplash.com/photo-1517971129774-8a2b38fa128e?w=500'
        ),
        Product(
            name='Water Bottle', 
            description='Insulated stainless steel water bottle - stay hydrated', 
            price=19.99, 
            stock=60,
            image_url='https://images.unsplash.com/photo-1602143407151-7111542de6e8?w=500'
        ),
    ]
    
    db.session.add_all(products)
    db.session.commit()
    return 'Products added! <a href="/">Go to store</a>'


if __name__ == '__main__':
    with app.app_context():
        db.create_all()
    app.run(debug=True)