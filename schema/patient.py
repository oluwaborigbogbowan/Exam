from pydantic import BaseModel
from decimal import Decimal

class Patient(BaseModel):
    id: int
    name: str
    age: int
    sex: str
    weight: Decimal
    height: Decimal
    phone: str

class PatientCreate(BaseModel):
    name: str
    age: int
    sex: str
    weight: Decimal
    height: Decimal
    phone: str

patients = [
]