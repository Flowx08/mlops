from fastapi import FastAPI, File, UploadFile
import requests
import os
import sys

sys.path.append("./src/models/")

from predict_model import predict_garbage

app = FastAPI()

@app.get("/")
def read_root():
   return {"Hello": "World"}

@app.post("/predict/")
def predict(url:str):
    # Download and save image
    response = requests.get(url)
    open("/tmp/image.jpg", "wb").write(response.content)

    # Predict class
    class_id = predict_garbage("./models/model.pth", "/tmp/image.jpg")
    print(class_id)

    class_names = ['cardboard', 'glass', 'metal', 'paper', 'plastic', 'trash']

    # Remove image
    os.remove("/tmp/image.jpg")

    return {"class_id": class_id,
            "class_name": class_names[class_id]}
