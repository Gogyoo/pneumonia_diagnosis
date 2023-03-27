from fastapi import FastAPI, UploadFile, File
from tensorflow.keras.utils import load_img
from tensorflow.keras import Model

app = FastAPI()

@app.get("/")
def index():
    return {"OK":True}



@app.post('/predict')
# input: X-ray image, or nothing, and we
# tell the function to sample randomly
# from the test subset

# output: Normal/Negative or Pneumonia/Positive,
# perhaps even with confidence of the model attached to this result

async def detect_faces(img: UploadFile=File(...)):
    # Receiving and decoding the image
    tested = await img.read()
    pre_trained = Model.load_weights("gs://pneumonia-models/model.h5")
    verdict = pre_trained.predict(tested)
    return {"Prediction": verdict}
