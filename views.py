from flask import render_template, request, redirect, flash,url_for
from models import Category, MyTodo, Priority, db
from tej_todoapp import app


@app.route('/')
def list_all():
    return render_template(
        'list.html',
        categories=Category.query.all(),
        todos=MyTodo.query.join(Priority).join(Category).order_by(Priority.value.desc())
    )


@app.route('/<name>')
def list_todos(name):
    category = Category.query.filter_by(name=name).first()
    return render_template(
        'list.html',
        todos=MyTodo.query.filter_by(category=category).join(Priority).join(Category).order_by(Priority.value.desc()),
        categories=Category.query.all()
    )


@app.route('/new-task', methods=['GET', 'POST'])
def new():
    if request.method == 'POST':
        category = Category.query.filter_by(id=request.form['category']).first()
        priority = Priority.query.filter_by(id=request.form['priority']).first()
        todo = MyTodo(category_id=category.id, priority_id=priority.id, description=request.form['description'])
        db.session.add(todo)
        db.session.commit()
        return redirect(url_for('list_all'))
    else:
        return render_template(
            'new-task.html',
            page='new-task',
            categories=Category.query.all(),
            priorities=Priority.query.all()
        )


@app.route('/<int:todo_id>', methods=['GET', 'POST'])
def update_todo(todo_id):
    todo = MyTodo.query.get(todo_id)
    if request.method == 'GET':
        return render_template(
            'new-task.html',
            todo=todo,
            categories=Category.query.all(),
            priorities=Priority.query.all()
        )	
    else:
        category = Category.query.filter_by(id=request.form['category']).first()
        priority = Priority.query.filter_by(id=request.form['priority']).first()
        description = request.form['description']
        todo.category_id = category.id
        todo.priority_id = priority.id
        todo.description = description
        db.session.commit()
        return redirect('/')


@app.route('/new-category', methods=['GET', 'POST'])
def new_category():
    if request.method == 'POST':
        category = Category(name=request.form['category'])
        db.session.add(category)
        db.session.commit()
        return redirect('/')
    else:
        return render_template(
            'new-category.html',
            page='new-category.html')


@app.route('/edit_category/<int:category_id>', methods=['GET', 'POST'])
def edit_category(category_id):
    category = Category.query.get(category_id)
    if request.method == 'GET':
        return render_template(
            'new-category.html',
            category=category
        )
    else:
        category_name = request.form['category']
        category.name = category_name
        db.session.commit()
        return redirect('/')


@app.route('/delete-category/<int:category_id>', methods=['POST'])
def delete_category(category_id):
    if request.method == 'POST':
    	todo=MyTodo.query.filter_by(category_id=category_id)
        category = Category.query.get(category_id)
        if todo.count() == 0:
            db.session.delete(category)
            db.session.commit()
        else:
            flash('You have TODOs in that category. Remove them first.')
        return redirect('/')


@app.route('/delete-todo/<int:todo_id>', methods=['POST','GET'])
def delete_todo(todo_id):
    if request.method == 'GET':
        todo = MyTodo.query.get(todo_id)
        db.session.delete(todo)
        db.session.commit()
        return redirect('/')
    else:
        flash('Sorry I couldnt understand')
        return redirect('/')


@app.route('/mark-done/<int:todo_id>', methods=['POST','GET'])
def mark_done(todo_id):
    if request.method == 'GET':
        todo = MyTodo.query.get(todo_id)
        todo.is_done = True
        db.session.commit()
        return redirect('/')
    else:
        flash('Sorry I couldnt understand')
        return redirect('/')