// ===================================
// TaskBoard JavaScript
// ===================================

console.log('TaskBoard loaded');

// ===================================
// Add Task Function
// ===================================
async function addTask() {
    const name = document.getElementById('taskName').value;
    
    // Get CKEditor 5 data from global reference
    const editor = window.addTaskEditorGlobal;
    
    if (!editor) {
        alert('Editor not initialized. Please try reopening the modal.');
        return;
    }
    
    const detail = editor.getData();
    const effort = document.getElementById('taskEffort').value;
    const status = document.getElementById('taskStatus').value;
    const img_url = document.getElementById('taskImg').value;

    if (!name || !detail || !effort) {
        alert('Please fill in all required fields');
        return;
    }

    try {
        const response = await fetch('/api/tasks', {
            method: 'POST',
            headers: {
                'Content-Type': 'application/json',
            },
            body: JSON.stringify({
                name: name,
                details: detail,
                effort: parseFloat(effort),
                status: status,
                img_url: img_url
            })
        });

        if (response.ok) {
            // Close modal and reload page
            const modal = bootstrap.Modal.getInstance(document.getElementById('addTaskModal'));
            modal.hide();
            location.reload();
        } else {
            alert('Error adding task');
        }
    } catch (error) {
        console.error('Error:', error);
        alert('Error adding task');
    }
}

// ===================================
// Edit Task Function
// ===================================
async function editTask(taskId) {
    try {
        // Fetch task data
        const response = await fetch(`/api/tasks/${taskId}`);
        
        if (!response.ok) {
            alert('Error loading task data');
            return;
        }
        
        const task = await response.json();
        
        // Populate form fields
        document.getElementById('editTaskId').value = task.id;
        document.getElementById('editTaskName').value = task.task_name;
        document.getElementById('editTaskEffort').value = task.task_effort;
        document.getElementById('editTaskStatus').value = task.status;
        document.getElementById('editTaskImg').value = task.task_img;
        
        // Show the modal
        const editModal = new bootstrap.Modal(document.getElementById('editTaskModal'));
        editModal.show();
        
        // Set CKEditor content after modal is shown and editor is initialized
        // We need to wait for the editor to be ready
        setTimeout(() => {
            const editorElement = document.querySelector('#editTaskDetail');
            if (editorElement.ckeditorInstance) {
                editorElement.ckeditorInstance.setData(task.task_detail);
            }
        }, 500);
        
    } catch (error) {
        console.error('Error:', error);
        alert('Error loading task data');
    }
}

// ===================================
// Update Task Function
// ===================================
async function updateTask() {
    const taskId = document.getElementById('editTaskId').value;
    const name = document.getElementById('editTaskName').value;
    
    // Get CKEditor 5 data from global reference
    const editor = window.editTaskEditorGlobal;
    
    if (!editor) {
        alert('Editor not initialized. Please try reopening the modal.');
        return;
    }
    
    const detail = editor.getData();
    const effort = document.getElementById('editTaskEffort').value;
    const status = document.getElementById('editTaskStatus').value;
    const img_url = document.getElementById('editTaskImg').value;

    if (!name || !detail || !effort) {
        alert('Please fill in all required fields');
        return;
    }

    try {
        const response = await fetch(`/api/tasks/${taskId}`, {
            method: 'PATCH',
            headers: {
                'Content-Type': 'application/json',
            },
            body: JSON.stringify({
                name: name,
                details: detail,
                effort: parseFloat(effort),
                status: status,
                img_url: img_url
            })
        });

        if (response.ok) {
            const modal = bootstrap.Modal.getInstance(document.getElementById('editTaskModal'));
            modal.hide();
            location.reload();
        } else {
            alert('Error updating task');
        }
    } catch (error) {
        console.error('Error:', error);
        alert('Error updating task');
    }
}

// ===================================
// Delete Task Function
// ===================================
async function deleteTask(taskId) {
    if (!confirm('Are you sure you want to delete this task?')) {
        return;
    }

    try {
        const response = await fetch(`/api/tasks/${taskId}`, {
            method: 'DELETE'
        });

        if (response.ok) {
            location.reload();
        } else {
            alert('Error deleting task');
        }
    } catch (error) {
        console.error('Error:', error);
        alert('Error deleting task');
    }
}

// ===================================
// Search Functionality
// ===================================
document.addEventListener('DOMContentLoaded', function() {
    const searchInput = document.getElementById('searchInput');
    
    if (searchInput) {
        searchInput.addEventListener('input', function(e) {
            const searchTerm = e.target.value.toLowerCase();
            const taskCards = document.querySelectorAll('.task-card');

            taskCards.forEach(card => {
                const title = card.querySelector('.task-title').textContent.toLowerCase();
                const detail = card.querySelector('.task-detail').textContent.toLowerCase();

                if (title.includes(searchTerm) || detail.includes(searchTerm)) {
                    card.style.display = '';
                } else {
                    card.style.display = 'none';
                }
            });
        });
    }
});
