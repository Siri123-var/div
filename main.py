from fastapi import FastAPI, HTTPException
from pydantic import BaseModel, EmailStr
from typing import List

app = FastAPI()

# Define the DataModel to handle the incoming data structure
class DataModel(BaseModel):
    System_Name: str
    Supplier_Number: int
    Credit_Number: int
    Email: List[EmailStr]  # Use EmailStr to automatically validate email format

# Create a POST endpoint to accept the data
@app.post("/submit-data")
async def submit_data(data: List[DataModel]):
    # Validate if data is empty
    if not data:
        raise HTTPException(status_code=400, detail="No data provided")

    # Process the received data
    for record in data:
        print(f"Received Data: {record}")
        
        # Here, emails are validated automatically using EmailStr
        # Any invalid email in the request would raise a validation error from Pydantic

    return {"message": "Data received successfully", "data": data}








