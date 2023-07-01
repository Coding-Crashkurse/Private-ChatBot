# Personal Fitness ChatBot (Version 1)

## Description

This project is a FastAPI-based web application. It is designed to provide a secure conversation platform for registered users. The main functionality of this version is to authenticate the user and return a static conversation message.

## Setup

This project uses FastAPI and SQLAlchemy, and it requires Python 3.7+.

To start the application, navigate to the project folder and execute the command:

python main.py

The application will be available at `http://localhost:5555`.

## Key Features

- User registration and authentication system with OAuth2.
- Secure conversation endpoint that returns a static message and the authenticated user's username.
- SQLite database for user data persistence.

## Environment Variables

To run this project, you will need to add the following environment variable:

- `SECRET_KEY`: Your secret key for encoding and decoding the JWT tokens.

Please use a `.env` file for setting this environment variable. The `.env` file is ignored by git to ensure sensitive items are not accidentally published.
