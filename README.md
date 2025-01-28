# TeleManage: Automated Customer Transactions and Data Handling Bot

## Overview
**TeleManage** is a Telegram Bot designed to streamline customer transactions and manage data efficiently. With 7 automated functionalities, it caters to over 500 customers while integrating seamlessly with a MySQL database to handle queries across multiple relational tables. The project also includes a secure REST API built with Django, featuring JWT authentication and role-based access control.

## Features
- **Automated Transactions**: Handles customer transactions with 7 unique automated features.
- **Database Integration**: Efficiently queries MySQL across 5 relational tables to manage customer data.
- **Secure REST API**: Designed with JWT authentication and role-based access control (3 roles) to maintain data integrity and security.
- **Telegram Bot Functionality**: Utilizes the Telegram Bot API to interact with users, providing a robust and user-friendly communication platform.

## Tech Stack
- **Backend**: Python, Django, Telegram Bot API
- **Frontend**: React
- **Database**: MySQL
- **Security**: JWT Authentication, Role-Based Access Control
- **APIs**: REST API

## Domain
- DevOps

## Installation

1. **Clone the Repository**
   ```bash
   git clone https://github.com/yourusername/dummy-project-5.git
   cd dummy-project-5
   ```

2. **Set Up the Backend**
   - Navigate to the backend directory.
   - Create a virtual environment and activate it:
     ```bash
     python -m venv env
     source env/bin/activate  # Linux/Mac
     env\Scripts\activate  # Windows
     ```
   - Install dependencies:
     ```bash
     pip install -r requirements.txt
     ```
   - Configure your MySQL database in the Django settings file.
   - Run database migrations:
     ```bash
     python manage.py migrate
     ```
   - Start the Django server:
     ```bash
     python manage.py runserver
     ```

3. **Set Up the Telegram Bot**
   - Register a new bot with Telegram’s BotFather to obtain your API key.
   - Add the API key to the `.env` file in the backend.

4. **Set Up the Frontend**
   - Navigate to the frontend directory.
   - Install dependencies:
     ```bash
     npm install
     ```
   - Start the React development server:
     ```bash
     npm start
     ```

## Usage
1. Start the Django server and the React frontend server.
2. Interact with the bot via Telegram to perform transactions, upload data, or retrieve information.
3. Access administrative and user functionalities securely through role-based authentication.

## Future Enhancements
- Add additional Telegram Bot features such as file handling or advanced analytics.
- Implement audit logging for all transactions.

## Contributing
Contributions are welcome! Fork the repository, make your changes, and submit a pull request.

## License
This project is licensed under the MIT License.
