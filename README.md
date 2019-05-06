# Project Title
Completing Django blog tutorial from [Traversy Media](https://www.youtube.com/watch?v=D6esTdOLXh4)

# Before you get started
Concepts to be familiar with
- Web development
- Routes
- Models
- Views
- Python 3.7 knowledge
- Html/Css

# Process
1. Creating/activating a virtualenv including django using `virtualenv`
2. Creating a django project with `django-admin startproject <name>`
3. Creating an app with `python manage.py startapp <appname>`. Add app to `INSTALLED_APPS` in `settings.py`
4. Setting up database engine to MySQL (default is sqlite). `python manage.py makemigrations <app name>` to migrate database ORM to migrations folder within app directory. `python manage.py migrate` to create tables (apply migrations).
5. Adding templates directory, views & urls
6. 

# Setup

**How to install MYSQL on Ubuntu**
```sh
sudo apt-get install python-dev default-libmysqlclient-dev python3-dev
sudo apt update
sudo apt install mysql-server
sudo mysql_secure_installation
```

**How to obtain this repository:**
```sh
git clone https//link.to.this.projects.git-repo
```
**Modules/dependencies:**
- `django`
- `mysqlclient`

**Activate virtualenv and install dependencies**
```sh
cd clone/path
source venv/bin/activate
pip install django mysqlclient
```

# Tree
```sh
.
├── blog
│   ├── admin.py
│   ├── apps.py
│   ├── __init__.py
│   ├── migrations
│   │   ├── 0001_initial.py
│   │   ├── __init__.py
│   │   └── __pycache__
│   │       ├── 0001_initial.cpython-37.pyc
│   │       └── __init__.cpython-37.pyc
│   ├── models.py
│   ├── __pycache__
│   │   ├── admin.cpython-37.pyc
│   │   ├── __init__.cpython-37.pyc
│   │   ├── models.cpython-37.pyc
│   │   ├── urls.cpython-37.pyc
│   │   └── views.cpython-37.pyc
│   ├── templates
│   │   └── blog
│   │       └── index.html
│   ├── tests.py
│   ├── urls.py
│   └── views.py
├── db.sqlite3
├── manage.py
└── project
    ├── __init__.py
    ├── __pycache__
    │   ├── __init__.cpython-37.pyc
    │   ├── settings.cpython-37.pyc
    │   ├── urls.cpython-37.pyc
    │   └── wsgi.cpython-37.pyc
    ├── settings.py
    ├── urls.py
    └── wsgi.py
```

# Tests
- Created admin route
- Created blog route
- Created posts
- Created DB in MYSQL
- Migrated Model and created tables using django utilities
- Rendered posts using jinja template engine

# Contributors
- Daniel Corcoran

# Sources
- [Django Blog Tutorial](https://www.youtube.com/watch?v=D6esTdOLXh4)
- [Installing MySQL on ubuntu 18.04](https://www.digitalocean.com/community/tutorials/how-to-install-mysql-on-ubuntu-18-04)
