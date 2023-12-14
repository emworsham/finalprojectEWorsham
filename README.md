# Simple Shopping List App

## Description

Simple Shopping List App is a comprehensive Django web application designed to simplify and enhance the shopping experience. This project primarily focuses on allowing users to create and manage personalized shopping lists. The application offers a user-friendly interface where individuals can register and log in to access their dashboard, facilitating a secure and personalized experience.

Key features of this application include:

- **User Registration and Authentication**: Allows users to securely register and log in to access their personalized dashboard.
- **Store Management**: Users can create, edit, and delete stores, enabling them to organize shopping lists according to different shopping locations or preferences.
- **Shopping List Creation**: Within each store, users can create detailed shopping lists, adding a practical layer to everyday shopping planning.
- **Interactive Shopping Lists**: Users can add, edit, and delete items from their shopping lists. Additionally, the application provides an intuitive feature to mark items as purchased, improving the shopping experience.
- **Nutritional Information**: A unique feature that allows users to search for and display nutritional information for various food items, integrating data from an external API for accurate and up-to-date information.

Simple Shopping List App is built with the aim of providing a seamless and efficient shopping planning tool, catering to the needs of individuals looking for an organized approach to their shopping tasks.


## Installation

### Prerequisites

Before you begin, ensure you have met the following requirements:

- Python 3.x
- pip (Python package manager)
- Virtual environment (recommended)

### Setup and Installation

1. **Clone the Repository**
   
   Clone this repository to your local machine using:

   ```
   git clone https://github.com/emworsham/finalprojectEWorsham.git

2. **Create and Activate a Virtual Environment (Optional but recommended)**

   + Unix/Linux/macOS:
      ```
     python3 -m venv venv
     source venv/bin/activate
   + Windows:
      ```
     python -m venv venv
     venv\Scripts\activate
   
3. **Install Required Packages**

    Install the required packages using pip:
      ```b
      pip install -r requirements.txt

### Setting Up

1. **Initialize the Database**
   Before running the application, you need to initialize the database. Run the following commands:

      
      python manage.py makemigrations
      python manage.py migrate```
   

   These commands create the necessary database tables and apply migrations.
2. **Create a Superuser**
    ```bash
   python manage.py createsuperuser

### Running the Application

To run the development server, execute:
    ```
    python manage.py runserver
    ```


This will start the development server on http://127.0.0.1:8000/.

To access the admin site, navigate to http://127.0.0.1:8000/admin/ and use the superuser credentials to log in.