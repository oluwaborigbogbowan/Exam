from fastapi import HTTPException
from schema.doctors import DoctorCreate,doctors


class DoctorService:

    @staticmethod
    def validate_if_doctor_is_registered(payload:DoctorCreate):
        for doctor in doctors:
            if (doctor.name == payload.name
                 and doctor.specialization == payload.specialization
                   and doctor.phone == payload.phone):
                raise HTTPException(
                    status_code=400,
                    detail="Doctor already exists"
                )
        return payload
    
    @staticmethod
    def does_doctor_exist(doctor_id:int):
        doctor_set = set()
        for doctor in doctors:
            doctor_set.add(doctor.id)
        if doctor_id not in doctor_set:        
            raise HTTPException(
                status_code=404,
                detail="doctor not found",
            )
        return doctor_id

doctor_service = DoctorService()