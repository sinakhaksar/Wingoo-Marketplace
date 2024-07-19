# Wingoo Marketplace

Wingoo Marketplace is a test project designed to practice building a marketplace application using Django for the backend and Django templates for the frontend. This project includes core functionalities such as adding products, viewing products before publishing (by admins), and user authentication.

## Features

- Product listing
- User management
- User authentication
- Product review before release (staff users only)
- Dashboard for managing listed products (view, edit, delete)
- Search functionality

## Technologies Used

- **Backend:** Django, Pillow
- **Frontend:** HTML, CSS, Tailwind CSS
- **Database:** SQLite (default for Django)

## Requirements

To run this project, ensure you have the following installed:

- Python 3.8 or higher

## Installation

Follow these steps to set up the project on your local machine:

### Backend

1. **Create and activate a virtual environment:**

    ```sh
    python -m venv env
    env\Scripts\activate.bat  # On macOS: `source env/bin/activate`
    ```

2. **Clone the repository:**

    ```sh
    git clone https://github.com/sinakhaksar/Wingoo-Marketplace.git
    cd Wingoo-Marketplace
    ```

3. **Install the required Python packages:**

    ```sh
    pip install -r requirements.txt
    ```

4. **Apply migrations:**

    ```sh
    python manage.py makemigrations
    python manage.py migrate
    ```

5. **Create a superuser:**

    Existing users for testing:
    - **Superuser**: `admin`
      - Email: `changethis@gmail.com`
      - Password: `<<apt@!n_|--|@Barbo$$@>`
      
    - **Test User**: `test_user`
      - Email: `test@gmail.com`
      - Password: `EVm2@M@d*mxrG4U`
      
    You can also create your own superuser with:

    ```sh
    python manage.py createsuperuser
    ```

6. **Run the development server:**

    ```sh
    python manage.py runserver  # Specify a port if desired; default is 8000
    ```

## Project Structure

- `Wingoo/`: Project settings
- `core/`: Core functionalities
- `dashboard/`: Dashboard features
- `item/`: Product-related features
- `media/`: Directory for item images
- `db.sqlite3`: SQLite database file
- `manage.py`: Django's command-line utility

## Contributing

This is a learning project, and contributions are welcome! Feel free to fork the repository and submit pull requests.

## License

This project is licensed under the MIT License. See the [LICENSE](LICENSE) file for details.

## Contact

For questions or suggestions, open an issue or contact me at sinakhaksar3@gmail.com .
