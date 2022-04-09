import subprocess
import re
from pydantic import BaseModel
from fastapi import FastAPI


class Control(BaseModel):
    motor: int
    steering: int


app = FastAPI()


@app.get("/")
async def root():
    return {"message": "Hier kommt vielleicht eine Control-Seite hin"}


@app.get("/cpu")
async def get_cpuTemp():
    res: str = subprocess.check_output('sensors')
    #temp = re.findall(r"\d+\.\d+°C", res)
    return {"cpu": res}


@app.post("/controls/")
async def set_controls(control: Control):
    return control
