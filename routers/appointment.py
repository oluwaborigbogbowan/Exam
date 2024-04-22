#new route assumes doctor is free upon validation
#create appointment
from fastapi import APIRouter, HTTPException, Depends
from schema.appointment import appointments,Appointment,AppointmentCreate,AppointmentStatus
from schema.doctors import doctors
from services.appointment import appointment_service

appointment_router = APIRouter()


@appointment_router.get('/',status_code=200)
def list_appointment():
    return {'message':'success','data': appointments}

@appointment_router.post('/',status_code=201)
def create_appointment(payload:AppointmentCreate = Depends(appointment_service.validate_appointment)):
    appointment_id = len(appointments) + 1
    doctor__id = appointment_service.find_doctor(doctors)
    new_appointment = Appointment(
        id=appointment_id,
        patient_id=payload.patient_id,
        doctor_id= doctor__id,
        date=payload.date
    )
    appointments.append(new_appointment)

    for doctor in doctors:
        if doctor.id == doctor__id:
            doctor.is_available = False

    return new_appointment

@appointment_router.get('/{appointment_id}',status_code=200)
def get_appointment(appointment_id:int):
    for appointment in appointments:
        if appointment.id == appointment_id:
            return appointment
    raise HTTPException(
                status_code=404,
                detail="appointment not found"
            )
        
@appointment_router.put('/{appointment_id}',status_code=201)
def complete_appointment(appointment_id:int = Depends(appointment_service.does_appointment_exist)):
    for appointment in appointments:
        if appointment.id == appointment_id:
            appointment.status = AppointmentStatus.completed.value
            for doctor in doctors:
                if doctor.id == appointment.doctor_id:
                    doctor.is_available = True
            return {'message': 'Appointment completed successfully'}
        
@appointment_router.patch('/{appointment_id}',status_code=201)
def cancel_appointment(appointment_id:int = Depends(appointment_service.does_appointment_exist)):
    for appointment in appointments:
        if appointment.id == appointment_id:
            appointment.status = AppointmentStatus.cancelled.value
            for doctor in doctors:
                if doctor.id == appointment.doctor_id:
                    doctor.is_available = True
            return {'message': 'Appointment cancelled successfully'}
        

        

        

