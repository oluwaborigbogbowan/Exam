from fastapi import FastAPI
from routers.patient import patient_router
from routers.doctors import doctor_router
from routers.appointment import appointment_router


app = FastAPI()

app.include_router( patient_router,prefix='/patient', tags=['patient'])
app.include_router(doctor_router,prefix='/doctors', tags=['doctor'])
app.include_router(appointment_router,prefix='/appointment', tags=['appointment'])