from fastapi import FastAPI, File, UploadFile, HTTPException, Form
from fastapi.responses import JSONResponse
from io import BytesIO
import os
import json

def frame_extraction(file):
    try:
        print(type(file))
        # print("Ts")
    except Exception as e:
        print(e)
    pass

app = FastAPI()
@app.post("/upload/")
async def upload_file_and_json(file: UploadFile = File(...), info: str = Form(...)):
    # Read the JSON data
    json_data = json.loads(info)
    
    # Process the uploaded file
    file_content = await file.read()
    frame_extraction(file)
    # Do something with the file and JSON data
    # For demonstration, let's just print them
    print("Uploaded file:", file.filename)
    print("JSON data:", json_data)
    
    # Here, you can manipulate the file_content or json_data as needed
    
    # You can also return a response or perform any other actions
    
    return {"file_uploaded": file.filename, "json_data": json_data}
