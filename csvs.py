import csv
from fastapi import FastAPI
from pydantic import BaseModel

app = FastAPI()
class Person (BaseModel):
    id:int
    email:str
    name:str
    
@app.post("/person/")
async def create_person (person: Person):
    with open("new.csv","a",newline='') as file:
        writer =csv.writer(file)
        writer.writerow([person.id, person.email, person.name ])
    return {"message": "person created successfully","data":person}












