from fastapi import FastAPI
from pydantic import BaseModel
from typing import List

app=FastAPI()
class prac(BaseModel):
    id: int 
    name : str
    origin: str

parray: List[prac]=[]
#basically this is defining our structure we use dpydsantuc an dtypiin here 

@app.get("/")
def read_root():
    return{"message": "practice fastapi"}
@app.get("/prac")
def get_parray():
    return parray

@app.post("/parray")
def add_prac(pracpost: prac):
    parray.append(pracpost)
    return pracpost

@app.put("/parray/{parray_id}")
def update_prac(parray_id : int, updated_prac:prac):
    for index, pracpost in enumerate(parray):
        if pracpost.id== parray_id:
            parray[index]= updated_prac
            return update_prac
        return{"error":"id not found"}

@app.delete("/parray/{parray_id}")
def delete_prac(parray_id: int):
    for index, pracpost in enumerate(parray):
        if pracpost.id== parray_id:
            parray.pop(index)
            return {"message": "deleted"}  # ✅ Add return after pop
    return {"error": "id not found"}


