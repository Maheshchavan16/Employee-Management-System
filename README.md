# Employee Management System

## Overview
The **Employee Management System** is a Python-based application designed to streamline HR processes by managing employee information efficiently. It features a user-friendly graphical interface created with Tkinter and a robust backend powered by Flask. The system includes secure login and signup functionality, making it an all-in-one solution for managing employee data.

## Features
- **Graphical User Interface (GUI):** Built using Tkinter for a simple and intuitive user experience.
- **Secure Authentication:** Login and signup functionality integrated directly into the application to ensure secure access.
- **Employee Management:** Add, update, delete, and view employee records with ease.
- **Flask Backend:** Used for handling data operations and ensuring smooth communication between the GUI and the database.

## Technologies Used
- **Python:** Core language for developing the application.
- **Tkinter:** Used to create the graphical user interface.
- **Flask:** Backend framework for handling server-side operations.
- **SQLite:** Database for storing employee records.
- **HTML/CSS/JavaScript:** Used in conjunction with Flask for the login and signup pages.

## Installation

1. **Clone the repository:**
   ```bash
   git clone https://github.com/yourusername/employee-management-system.git
   cd employee-management-system

python -m venv venv
source venv/bin/activate   # On Windows use `venv\Scripts\activate`

pip install -r requirements.txt

python main.py
