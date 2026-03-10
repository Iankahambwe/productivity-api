from fastapi import FastAPI, Depends, HTTPException
from sqlalchemy.orm import Session
from typing import List
import models, schemas
from database import engine, get_db

models.Base.metadata.create_all(bind=engine)

app = FastAPI(
    title="🚀 Personal Productivity API",
    description="A REST API for managing your To-Do list and Expenses",
    version="1.0.0"
)

# TODO ENDPOINTS

@app.get("/todos", response_model=List[schemas.TodoResponse], tags=["Todos"])
def get_todos(db: Session = Depends(get_db)):
    return db.query(models.Todo).all()

@app.post("/todos", response_model=schemas.TodoResponse, tags=["Todos"])
def create_todo(todo: schemas.TodoCreate, db: Session = Depends(get_db)):
    new_todo = models.Todo(**todo.dict())
    db.add(new_todo)
    db.commit()
    db.refresh(new_todo)
    return new_todo

@app.put("/todos/{todo_id}", response_model=schemas.TodoResponse, tags=["Todos"])
def update_todo(todo_id: int, updates: schemas.TodoUpdate, db: Session = Depends(get_db)):
    todo = db.query(models.Todo).filter(models.Todo.id == todo_id).first()
    if not todo:
        raise HTTPException(status_code=404, detail="Todo not found")
    for key, value in updates.dict(exclude_none=True).items():
        setattr(todo, key, value)
    db.commit()
    db.refresh(todo)
    return todo

@app.delete("/todos/{todo_id}", tags=["Todos"])
def delete_todo(todo_id: int, db: Session = Depends(get_db)):
    todo = db.query(models.Todo).filter(models.Todo.id == todo_id).first()
    if not todo:
        raise HTTPException(status_code=404, detail="Todo not found")
    db.delete(todo)
    db.commit()
    return {"message": f"Todo {todo_id} deleted successfully"}

# EXPENSE ENDPOINTS

@app.get("/expenses", response_model=List[schemas.ExpenseResponse], tags=["Expenses"])
def get_expenses(db: Session = Depends(get_db)):
    return db.query(models.Expense).all()

@app.post("/expenses", response_model=schemas.ExpenseResponse, tags=["Expenses"])
def create_expense(expense: schemas.ExpenseCreate, db: Session = Depends(get_db)):
    new_expense = models.Expense(**expense.dict())
    db.add(new_expense)
    db.commit()
    db.refresh(new_expense)
    return new_expense

@app.delete("/expenses/{expense_id}", tags=["Expenses"])
def delete_expense(expense_id: int, db: Session = Depends(get_db)):
    expense = db.query(models.Expense).filter(models.Expense.id == expense_id).first()
    if not expense:
        raise HTTPException(status_code=404, detail="Expense not found")
    db.delete(expense)
    db.commit()
    return {"message": f"Expense {expense_id} deleted successfully"}

@app.get("/expenses/summary", tags=["Expenses"])
def expense_summary(db: Session = Depends(get_db)):
    expenses = db.query(models.Expense).all()
    if not expenses:
        return {"total": 0, "by_category": {}}
    total = sum(e.amount for e in expenses)
    by_category = {}
    for e in expenses:
        by_category[e.category] = by_category.get(e.category, 0) + e.amount
    return {"total": round(total, 2), "by_category": by_category}
from fastapi import FastAPI

app = FastAPI()

@app.get("/")
def home():
    return {"message": "Productivity API is running"}