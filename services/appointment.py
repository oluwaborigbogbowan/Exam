from fastapi import HTTPException
from schema.doctors import doctors
from schema.patient import patients
from schema.appointment import AppointmentCreate,appointments


class AppointmentService:

    @staticmethod
    def validate_appointment(payload:AppointmentCreate):
        patients_set = set()
        doctors_set = set()
        for patient in patients:
            patients_set.add(patient.id)
        for doctor in doctors:
            doctors_set.add(doctor.is_available)
        if payload.patient_id not in patients_set:
            raise HTTPException(
                status_code=404,
                detail=f"Patient with id {payload.patient_id} not found",
            )
        if True not in doctors_set:
            raise HTTPException(
                status_code=503,
                detail="No doctor is available at the moment.",
            )
        return payload


   

    def get_appointments_by_id(self,appointments,appointments_id):
        for appointment in appointments:
            if appointment.id == appointments_id:
                return appointment
        raise HTTPException(
            status_code=404,
            detail="appointment not found"
        )
      

    @staticmethod
    def find_doctor(doctors):
        for doctor in doctors:
            if doctor.is_available == True:
                return doctor.id
        return {'message': 'no available doctor'}  
    
    @staticmethod
    def does_appointment_exist(appointment_id:int):
        for appointment in appointments:
            if appointment.id == appointment_id:
                return appointment_id
        raise HTTPException(
            status_code=404,
            detail="appointment not found"
        )
            
appointment_service = AppointmentService()