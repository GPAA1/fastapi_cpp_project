from fastapi import FastAPI
from pydantic import BaseModel
import ctypes

calc_lib = ctypes.CDLL('./calc.dll')

operations = {
    "add": calc_lib.add,
    "sub": calc_lib.sub
}

class CalcInput(BaseModel):
    type: str
    a: int
    b: int

app = FastAPI()

@app.post("/calc")
async def calculate(input: CalcInput):
    if input.type not in operations:
        return {"error": "Invalid operation"}
    operation = operations[input.type]
    result = operation(input.a, input.b)
    return {"result": result}
