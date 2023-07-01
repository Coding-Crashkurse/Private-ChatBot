# Personal Fitness ChatBot (Version 2)

## Description

This version of the Personal Fitness ChatBot is an advanced AI chatbot. It uses OpenAI's Language Models to simulate conversation and provide personalized fitness advice to users. Each response is tailored to the user's unique profile, which includes their age and fitness level.

## Setup

This project uses FastAPI, SQLAlchemy and OpenAI, and it requires Python 3.7+.

To start the application, navigate to the project folder and execute the command:

python main.py

The application will be available at `http://localhost:5555`.

## Key Features

- User registration and authentication system with OAuth2.
- Secure conversation endpoint that generates a unique, AI-generated response based on the user's profile and question.
- SQLite database for user data persistence.
- Integration with OpenAI's Language Models to generate responses.

## Environment Variables

To run this project, you will need to add the following environment variables:

- `OPENAI_API_KEY`: Your OpenAI API key to use OpenAI's Language Models.

Please use a `.env` file for setting these environment variables. The `.env` file is ignored by git to ensure sensitive items are not accidentally published.
