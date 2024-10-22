## 🌐 [Versão em Português do README](README_PT.md)

# ETE-System

This project is a web application developed in Django. It has several features such as asset management, filter control, analytical dashboard, among other modules aimed at efficient resource management and random statistics.

## 🔨 Project Features

- Asset management, including creation, editing, and viewing.
- Control and monitoring of specific aerator filters.
- Data analysis and visualization in interactive dashboards.
- Historical control and information management in the system.
- User authentication and permission control.

### Visual Example of the Project

![chrome-capture-2024-10-21](https://github.com/user-attachments/assets/55317e7c-837e-4d84-8cca-2320c2b2f1d9)

## ✔️ Techniques and Technologies Used

- **Django**: Web development framework in Python.
- **HTML/CSS**: Structure and styling of the pages.
- **Tailwind CSS**: Utility CSS framework for fast and responsive styling.
- **SQLite Database**: Used for local data persistence during development.
- **Bootstrap**: Styling and reusable components to create responsive layouts (optional).
- **JavaScript**: For interactivity and DOM manipulation.

## 📁 Project Structure

- **core/**: Contains the main logic of the project.
    - **migrations/**: Migration files to configure and update the database.
    - **models.py**: Data model definitions.
    - **admin.py**: Admin panel configuration.
    - **templates/**: Contains the HTML templates used by the views.
        - **baseLogin.html**: Base template for the login page.
        - **dashboard/**: Specific templates for analysis, assets, control, and other dashboards.
    - **views.py**: Contains the view functions that render the HTML templates.
    - **urls.py**: Definition of the application's routes.

- **puddle/**: General project settings.
    - **settings.py**: Django settings such as database, installed apps, and middlewares.
    - **urls.py**: Definition of the main project routes.
    - **wsgi.py and asgi.py**: Configurations for running the project.

- **db.sqlite3**: SQLite database used during development.

- **requirements.txt**: List of dependencies needed to run the project.

## 🚠 Running the Project

To run the project locally, follow the steps below:

1. **Ensure Python is installed**:
    - [Python](https://www.python.org/) is required to run the project. You can check if it is already installed with:

   ```bash
   python --version
   ```

    - If not installed, download and install the latest version.

2. **Clone the Repository**:
    - Copy the repository URL and run the command below in the terminal:

   ```bash
   git clone <REPOSITORY_URL>
   ```

3. **Install dependencies**:
    - Navigate to the cloned project directory and install the necessary dependencies:

   ```bash
   pip install -r requirements.txt
   ```

4. **Configure the database**:
    - Run the migrations to set up the database:

   ```bash
   python manage.py migrate
   ```

5. **Create a superuser**:
    - To access the admin panel, create a superuser:

   ```bash
   python manage.py createsuperuser
   ```

6. **Start the server**:
    - To start the local server, use the command:

   ```bash
   python manage.py runserver
   ```

7. **Access the application**:
    - Open your browser and go to `http://127.0.0.1:8000/` to see the application running.

## 🌐 Deployment

To deploy the project, you can use platforms like [Heroku](https://www.heroku.com/), [DigitalOcean](https://www.digitalocean.com/), or [AWS](https://aws.amazon.com/). Make sure to properly configure environment variables and set up a production database, such as PostgreSQL or MySQL.
