from pydantic import BaseModel
from datetime import date
from schema.patient import Patient
from schema.doctors import Doctor
from enum import Enum

class AppointmentStatus(Enum):
    completed= 'completed'
    ongoing= 'ongoing'
    cancelled= 'cancelled'

    
class Appointment(BaseModel):
    id: int
    patient_id: int
    doctor_id: int
    date: date
    status: str = AppointmentStatus.ongoing.value

class AppointmentCreate(BaseModel):
    patient_id: int
    date: date


appointments =[
]
