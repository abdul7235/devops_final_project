from fastapi import FastAPI
import os
from fastapi.responses import JSONResponse
from dotenv import load_dotenv
from utils.constants import DIR,FILE_NAME
from utils.random_file_generator import random_file_generator
from utils.calculate_checksum import calculate_checksum


app = FastAPI()

@app.get("/generate_random_file_with_checksum/",)
async def generate_random_file_with_checksum():
    
    random_data = random_file_generator()
    checksum = calculate_checksum()
    
    response_data = {"file": random_data, "checksum": checksum}

    return JSONResponse(content=response_data)

    
