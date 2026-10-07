# Simple Django To-Do Web App

A beginner-friendly Django project based on the **"ToDo webapp using Django"** project listed in the GeeksforGeeks Django Projects collection.

Reference:
https://www.geeksforgeeks.org/python/django-projects/

## What this project does

The application lets a user:

- Add a task
- See all tasks
- Mark a task as completed
- Delete a task

The project intentionally uses simple Django concepts so that every part can be explained during a class demonstration.

## Technologies

- Python
- Django
- SQLite
- HTML
- Basic CSS

## Main Django concepts used

- `models.py` - stores tasks in the SQLite database
- `forms.py` - creates the task form
- `views.py` - handles requests and uses `render()`
- `urls.py` - connects URLs to views
- Templates - display the web pages
- Django ORM - saves and retrieves task data

## Project structure

```text
django_todo_project/
├── manage.py
├── requirements.txt
├── README.md
├── .gitignore
├── todo_project/
│   ├── __init__.py
│   ├── settings.py
│   ├── urls.py
│   ├── asgi.py
│   └── wsgi.py
└── todo/
    ├── __init__.py
    ├── admin.py
    ├── apps.py
    ├── forms.py
    ├── models.py
    ├── urls.py
    ├── views.py
    ├── migrations/
    │   └── __init__.py
    └── templates/
        └── todo/
            ├── home.html
            └── success.html
```

## How to run

### 1. Install Python

Make sure Python 3.10+ is installed.

Check:

```bash
python --version
```

### 2. Open the project folder

```bash
cd django_todo_project
```

### 3. Create a virtual environment

Windows:

```bash
python -m venv venv
venv\Scripts\activate
```

Mac/Linux:

```bash
python3 -m venv venv
source venv/bin/activate
```

### 4. Install Django

```bash
pip install -r requirements.txt
```

### 5. Create the database

```bash
python manage.py makemigrations
python manage.py migrate
```

### 6. Add sample data

```bash
python manage.py shell < sample_data.py
```

If the command above does not work in your terminal, open the Django shell:

```bash
python manage.py shell
```

Then paste the contents of `sample_data.py`.

### 7. Start the server

```bash
python manage.py runserver
```

Open:

http://127.0.0.1:8000/

## How the application works

### Adding a task

The user enters a task in the form and presses **Add Task**.

The form sends a POST request to Django.

`views.py` receives the request:

```python
form = TaskForm(request.POST)

if form.is_valid():
    form.save()
```

The task is then saved in the SQLite database.

### Completing a task

The user clicks **Complete**.

Django finds that task using its ID and changes:

```python
task.completed = True
```

### Deleting a task

The user clicks **Delete**.

Django finds the task and uses:

```python
task.delete()
```

## Important viva questions

### What is Django?

Django is a Python web framework used to build web applications.

### What is `render()`?

`render()` combines a template with data and returns the resulting HTML page to the browser.

### What is a model?

A model represents data that Django stores in the database.

### Why is `forms.py` used?

It creates and handles forms used to collect user input.

### What does `request.method == "POST"` mean?

It checks whether the user submitted the form.

### What does `form.is_valid()` do?

It checks whether the submitted form data is valid.

### What does `form.save()` do?

It saves the valid form data to the database.

### What is SQLite?

SQLite is a lightweight database included by default with Django projects.

### What is a migration?

A migration tells Django how the database structure should be created or changed.

### What is `urls.py`?

It maps a URL to a Django view.

## GitHub upload

After testing the project:

```bash
git init
git add .
git commit -m "Initial Django To-Do project"
git branch -M main
git remote add origin https://github.com/YOUR_USERNAME/django-todo-project.git
git push -u origin main
```

Replace `YOUR_USERNAME` with your GitHub username.

## Demo sequence

1. Run `python manage.py runserver`
2. Open the website.
3. Show the sample tasks.
4. Add a new task.
5. Show that it appears in the list.
6. Click Complete.
7. Click Delete.
8. Explain `models.py`, `forms.py`, `views.py`, `urls.py`, and the template.

## Note

This project is intentionally simple and was written as a learning implementation rather than copied from the GeeksforGeeks source code.
