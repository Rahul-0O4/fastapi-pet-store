#  FastAPI Pet Store
A simple **CRUD (Create, Read, Update, Delete)** Pet Store API built using **FastAPI** and **SQLite**.  
This project demonstrates clean folder structure, SQL-based persistence, and RESTful API design.

---

## Tech Stack
- **Python 3.11**
- **FastAPI**
- **SQLite**
- **Uvicorn**

##  Project Structure
pet_store/
├── app/
│ ├── api/
│ │ └── routes_api.py
│ ├── crud/
│ │ └── sql_crud.py
│ ├── db/
│ │ └── init_db.py
│ ├── models/
│ │ └── schemas.py
│ └── main.py
├── requirements.txt
├── .gitignore
└── README.md

## Steps Performed
1. Create Virtual Environment
2. Install Dependencies
3. Initialize Database
4. Run the Server
5. API Documentation
6. API endpoints
  - Add : /pets with POST method
  - Fetching : /pets with GET method
  - Update : /pets/{id} with PUT method
  - Delete : /pets/{id} with DELETE method
