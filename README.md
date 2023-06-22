# Note_saving_app
# MyNotes

MyNotes is a note-taking platform that allows users to store and manage textual, audio, and video notes. Users can register, log in, create their own notes, and search for existing notes by title. Additionally, users can share their notes with other users on the platform.

## Features

- User registration: Users can create an account to access the note-taking platform.
- User authentication: Registered users can log in to their accounts.
- Note creation: Users can create new notes by providing a title, content, and optional audio or video attachments.
- Note search: Users can search for notes by their titles.
- Note sharing: Users can share their notes with other users on the platform.
- User-specific notes: Each user can only view and manage their own notes.
- Responsive design: The platform is designed to be accessible and usable on various devices.

## Technologies Used

- Backend: Django (Python web framework)
- Frontend: HTML, CSS, JavaScript
- Database: SQLite (for testing purposes)
- API: Django REST Framework

## Installation

1. Clone the repository:

```bash
git clone https://github.com/your-username/MyNotes.git

2. Install the required dependencies:
pip install -r requirements.txt

3.Apply database migrations:
python manage.py migrate

4.Start the development server:
python manage.py runserver

5.Access the application in your web browser:
http://127.0.0.1:8000/

API Endpoints-
-POST /api/register: Register a new user.
-POST /api/login: Log in an existing user.
-POST /api/notes/create: Create a new note.
-GET /api/notes/search?query=title: Search for notes by title.
-GET /api/notes/: Retrieve all notes.
-GET /api/notes/{note_id}/: Retrieve a specific note by ID.
