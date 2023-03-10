from fastapi import FastAPI, File, UploadFile
from starlette.responses import FileResponse
import requests
import os
import sys
from fastapi.staticfiles import StaticFiles

sys.path.append("./src/models/")

from predict_model import predict_garbage
from hyperparameters import hyperparameters

app = FastAPI()

#app.mount("/static/", StaticFiles(directory="./src/interface/",html = True), name="interface")

@app.get("/")
async def read_root():
    return FileResponse('./src/interface/index.html')

@app.post("/predict/")
def predict(url: str):
    # Download and save image
    response = requests.get(url)
    open("/tmp/image.jpg", "wb").write(response.content)

    # Predict class
    class_id = predict_garbage(hyperparameters.deploy_model_path, "/tmp/image.jpg")
    print(class_id)

    class_names = ["cardboard", "glass", "metal", "paper", "plastic", "trash"]

    # Remove image
    os.remove("/tmp/image.jpg")

    return {"class_id": class_id, "class_name": class_names[class_id]}
