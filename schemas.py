from pydantic import BaseModel
from datetime import datetime
from typing import Optional

# --- Todo Schemas ---
class TodoCreate(BaseModel):
    title: str
    description: Optional[str] = ""

class TodoUpdate(BaseModel):
    title: Optional[str] = None
    description: Optional[str] = None
    completed: Optional[bool] = None

class TodoResponse(BaseModel):
    id: int
    title: str
    description: str
    completed: bool
    created_at: datetime

    class Config:
        from_attributes = True

# --- Expense Schemas ---
class ExpenseCreate(BaseModel):
    title: str
    amount: float
    category: Optional[str] = "General"

class ExpenseResponse(BaseModel):
    id: int
    title: str
    amount: float
    category: str
    date: datetime

    class Config:
        from_attributes = True