from fastapi import HTTPException
from schema.patient import PatientCreate,patients


class PatientService:


    @staticmethod
    def validate_if_patient_is_registered(payload:PatientCreate):
        for patient in patients:
            if (patient.name == payload.name
                 and patient.age == payload.age
                   and patient.weight == payload.weight
                     and patient.height == payload.height
                       and patient.sex == payload.sex
                         and patient.phone == payload.phone):
                raise HTTPException(
                    status_code=400,
                    detail="Patient already exists"
                )
        return payload
            

    def get_patient_by_id(self,patients,patients_id):
        for patient in patients:
            if patient.id == patients_id:
                return patient
        raise HTTPException(
            status_code=404,
            detail="Patient not found"
        )
        
patient_service = PatientService()