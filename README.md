\# 🚀 Productivity API



A simple REST API built with \*\*FastAPI\*\* to manage tasks (To-Dos) and expenses.



\## Features



\- Create tasks

\- View all tasks

\- Update tasks

\- Delete tasks

\- SQLite database using SQLAlchemy

\- FastAPI automatic documentation



\## Tech Stack



\- Python

\- FastAPI

\- SQLAlchemy

\- SQLite

\- Pydantic



\## Installation



Clone the repository:



git clone https://github.com/YOUR\_USERNAME/productivity-api.git



Move into the project folder:



cd productivity-api



Install dependencies:



pip install fastapi uvicorn sqlalchemy



\## Run the API



Start the server:



uvicorn main:app --reload



The API will run at:



http://127.0.0.1:8000



\## API Documentation



FastAPI automatically generates documentation:



Swagger UI  

http://127.0.0.1:8000/docs



ReDoc  

http://127.0.0.1:8000/redoc



\## Project Structure



productivity-api/

│

├── main.py

├── models.py

├── schemas.py

├── database.py

├── productivity.db

└── README.md



\## Example Endpoint



Get all todos:



GET /todos



Create todo:



POST /todos



\## Author



Your Name

