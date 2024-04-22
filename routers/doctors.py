from fastapi import APIRouter, HTTPException, Depends
from pydantic import typing
from schema.doctors import doctors,Doctor,DoctorCreate
from services.doctor import doctor_service



doctor_router = APIRouter()

@doctor_router.get('/',status_code=200)
def list_doctor():
    return {'message': 'list of all doctors','data': doctors}

@doctor_router.post('/',status_code=201)
def create_doctor(payload: DoctorCreate = Depends(doctor_service.validate_if_doctor_is_registered)):
    doctor_id = len(doctors) + 1
    new_doctor = Doctor(
        id=doctor_id,
        name=payload.name,
        specialization=payload.specialization,
        phone=payload.phone,
        is_available=True
    )
    doctors.append(new_doctor)
    return {'message':'doctor registered successfully','data':new_doctor}

@doctor_router.get('/{doctor_id}',status_code=200)
def get_doctor(doctor_id: int):
    for doctor in doctors:
        if doctor.id == doctor_id:
            return doctor
    raise HTTPException(
                status_code=404,
                detail=f"doctor with id {doctor_id} not found",
            )
        
@doctor_router.put('/{doctor_id}',status_code=200)
def update_doctor(doctor_id: int, payload: DoctorCreate = Depends(doctor_service.validate_if_doctor_is_registered) ):
    for doctor in doctors:
        if doctor.id == doctor_id:
            doctor.name = payload.name
            doctor.specialization = payload.specialization
            doctor.phone = payload.phone
            return {'message':'doctor updated successfully','data':doctor}
    raise HTTPException(
                status_code=404,
                detail=f"doctor with id {doctor_id} not found",
            )
        
@doctor_router.delete('/{doctor_id}',status_code=200)
def delete_doctor(doctor_id: int):
    for doctor in doctors:
        if doctor.id == doctor_id:
            doctors.remove(doctor)
            return {'message':'doctor deleted successfully'}
    raise HTTPException(
                status_code=404,
                detail="doctor not found",
            )
        
 
    


# @doctor_router.put('/{doctor_id}', status_code=200)
# def set_availablility_status(doctor_id: int, doctor: typing.Optional[Doctor] = None):  
#     for doc in doctors:
#         if doc.id == doctor_id:
#             doc.is_available = False
#             return {'message': 'Doctor is now unavailable', 'data': doc}
    
#     raise HTTPException(status_code=404, detail="Doctor not found")

@doctor_router.patch('/{doctor_id}',status_code=200)
def set_available(doctor_id:int):
    for doctor in doctors:
        if doctor.id == doctor_id:
            doctor.is_available = False
            return {'message': 'Doctor is now unavailable', 'data': doctor}
    raise HTTPException(status_code=404, detail='doctor not found')