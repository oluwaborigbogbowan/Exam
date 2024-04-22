from fastapi import APIRouter, HTTPException, Depends
from schema.patient import Patient, PatientCreate,patients
from services.patient import patient_service


patient_router = APIRouter()


@patient_router.get('/',status_code=200)
def list_patient():
    return {'message':'success','data': patients}


@patient_router.post('/',status_code=201)
def create_patient(payload:PatientCreate = Depends(patient_service.validate_if_patient_is_registered)):
    patient_id = len(patients) + 1
    new_patient = Patient(
        id=patient_id,
        name=payload.name,
        age=payload.age,
        sex=payload.sex,
        weight=payload.weight,
        height=payload.height,
        phone=payload.phone
    )
    patients.append(new_patient)
    return {'message':'patient registered successfully','data': new_patient}



@patient_router.get('/{patient_id}',status_code=200)
def get_patient(patient_id:int):
    for patient in patients:
        if patient.id == patient_id:
            return patient

    raise HTTPException(
                status_code=404,
                detail="Patient not found"
            )
        
@patient_router.put('/{patient_id}',status_code=200)
def update_patient(patient_id:int,payload:PatientCreate = Depends(patient_service.validate_if_patient_is_registered)):
    for patient in patients:
        if patient.id == patient_id:
            patient.name = payload.name
            patient.age = payload.age
            patient.sex = payload.sex
            patient.weight = payload.weight
            patient.height = payload.height
            patient.phone = payload.phone
            return {'message': 'patient updated successfully', 'data': patient}
    raise HTTPException(
                status_code=404,
                detail="Patient not found"
            )
        
@patient_router.delete('/{patient_id}',status_code=200)
def delete_patient(patient_id:int):
    for patient in patients:
        if patient.id == patient_id:
            patients.remove(patient)
            return {'message': 'patient deleted successfully'}
    raise HTTPException(
                status_code=404,
                detail="Patient not found"
            )