from fastapi import FastAPI

app = FastAPI()

@app.get("/")
def index():
    return {"OK":True}

@app.get('/predict')
# input: X-ray image
# output: Normal/Negative or Pneumonia/Positive,
# perhaps even with confidence of the model attached to this result
def predict(image):
    return {'wait': "Diagnostic: Pneumonia"}
