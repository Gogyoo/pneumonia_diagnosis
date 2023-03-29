from fastapi import FastAPI, UploadFile, File
from starlette.responses import Response
import numpy as np

from google.cloud import storage
from pneumonia.params import *

from tensorflow.keras import models
from tensorflow.io import decode_image
from tensorflow.image import resize
from tensorflow import reshape

app = FastAPI()

client = storage.Client()

# Loading the model in memory once the page is loaded. It takes me about 10s for an +- 100MB h5 model.
# But then each call to predict based on a test image is almost instantaneous
bloblist = [blob for blob in client.list_blobs(MODEL_BUCKET_NAME)]
print(bloblist)
latest_model_path_to_save = os.path.join(LOCAL_REGISTRY_PATH, "model.h5")
bloblist[-1].download_to_filename(latest_model_path_to_save)
pre_trained = models.load_model(latest_model_path_to_save)


@app.get("/")
def index():
    return {"OK":True}

@app.post('/predict')
# input: X-ray image

# output: Normal/Negative or Pneumonia/Positive,
# perhaps even with confidence of the model attached to this result

async def predict(img: UploadFile=File(...)):
    # Receiving and decoding the image
    tested = await img.read()

    decoded = decode_image(tested, channels=3)
    resized = resize(decoded, size=(256,256))
    tupled = reshape(resized, shape=(-1,256,256,3))
    verdict = pre_trained.predict(tupled)


    return {"Results": f"Patient has a {str(round(verdict[0][0]*100,2))}% chance of having pneumonia."}
