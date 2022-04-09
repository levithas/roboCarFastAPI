from pydantic import BaseModel
from fastapi import FastAPI


class Control(BaseModel):
    motor: int
    steering: int


app = FastAPI()


@app.get("/")
async def root():
    return {"message": "Hier kommt vielleicht eine Control-Seite hin"}


@app.post("/controls/")
async def set_controls(control: Control):
    return control
