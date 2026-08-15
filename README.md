# Student Management System

A beginner-friendly Student Management System built with:

- Python
- Flask
- MySQL
- HTML
- CSS
- Bootstrap 5

## Features

1. Add student
2. View all students
3. Search students
4. View student details
5. Edit student
6. Delete student
7. MySQL database storage
8. Flash messages for successful/error operations

## Project Structure

student_management_system/
│
├── app.py
├── database.sql
├── requirements.txt
├── README.md
├── templates/
│   ├── base.html
│   ├── index.html
│   ├── student_form.html
│   └── student_details.html
└── static/
    └── style.css

## Setup

### 1. Install MySQL

Create the database by running `database.sql` in MySQL Workbench.

### 2. Create a virtual environment

Windows:

python -m venv venv
venv\Scripts\activate

### 3. Install packages

pip install -r requirements.txt

### 4. Configure MySQL

Open `app.py` and replace:

YOUR_MYSQL_PASSWORD

with your MySQL root password.

### 5. Run the application

python app.py

Open:

http://127.0.0.1:5000

## Important

For a real project, store the database password in environment variables instead of directly inside `app.py`.
