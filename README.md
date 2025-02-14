# DarkForum

## Description
DarkForum is an application that allowed users to discuss many different subjects with the ability to post and react to others as well. The application supports login and register alongside posting, comments, searching and rating. The application uses python alongside flask, sqlAlchemy,Javascript and mysql with additional files for heroku deployment.

## Motivation
The motivation for this project came when me and my colleagues were discussing a project to make were wondering if we could create our own private reddit for our topic posting and our friends. Using this as motivation we started creating the concepts and decided to work on the basics features like posting, comments, searching, and ratings. The goal for this project was to create a blueprint for private forums that function like reddit for posts and reaction from your community.

## Quick Start
This project use python:
- Download Python and put to path (option will show in installation)
  - https://www.python.org/downloads/release/python-3110/ 
-  Create file and into it copy in terminal:
   -  ```git clone https://github.com/Jruz9/darkforum.git```
-  Open project folder on your favorite ide to beginning looking.

## Usage
Application features:
- Register and signing in with bcrypt encryption
- Posting topics
- Commenting on topics post. 
- Rating posts
## Contributing
This assumes you have followed the quick guide and your project is in your computer.
###  Create virtual environment
  - Open project folder and in terminal type or paste:
     1. ```python -m venv venv ``` 
### Activate venv
  - Windows 
    - ```cd/venv/Script```
    - ```./activate.ps1```
  - MacOS and other unix system:
    - ```source ./venv/bin/activate``` 
  - In the terminal venv will show on your left of your terminal line.
  - Some terminal support auto venv and that works but careful with that, it could confuse you later on and cause issues if you not aware of its limitations. 
### Download dependencies to virtual environment:
- In terminal type or paste in project folder:
  - ```pip install -r requirements.txt ```

### Database setup:
- Create MySQL database using the gui or shell command:
  - Gui:
    - In mysql workbench you can create database username = forum and password and that should be all modification.
### Database sql file
- Using the schema sql file, run the sql to create the tables and relations. 

### Database url
- Database url will look similar to:  mysql://USERNAME:PASSWORD@HOST:PORT/forum
- Username being root and password being whatever you put.
### Database env file
- The application will read the environment file.
- Create a .env in your folder and copy and paste what is in env. Sample and change whatever fits your needs.
### Run Application:
- The application can run with just running the app.py file on your ide. Future flask command will be added later for ease of use.
## Technologies:
- Python 3.11+ 
- SqlAlchemy
- MySQL
- Flask
- Javascript
- Heroku files