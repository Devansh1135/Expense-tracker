# Expense Tracker

A simple web application to manage and track your personal expenses. Built with Django and Bootstrap for a clean and responsive UI.

## Features

- User authentication (signup, login, logout)
- Add, edit, delete expenses
- Filter and search expenses by title, category, and date range
- View total expenses, count, and top spending category on the dashboard
- Interactive pie chart visualization of expenses by category
- Responsive design using Bootstrap 5

## Technologies Used

- Python 3.x
- Django 5.x
- Bootstrap 5
- Chart.js (for data visualization)
- SQLite (default Django database)

## Setup and Installation

1. Clone the repository:

   ```bash
   git clone https://github.com/yourusername/expense-tracker.git
   cd expense-tracker

2. Create and activate a virtual enviornment:

python -m venv venv
source venv/bin/activate   # On Windows: venv\Scripts\activate


3. Install dependencies:
pip install -r requirements.txt

4. Apply migrations:
python manage.py migrate

5. Create a Superuser:
python manage.py createsuperuser

6. Run the development server:
python manage.py runserver

7. Open your browser and go to http://127.0.0.1:8000