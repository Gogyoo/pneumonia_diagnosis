from fastapi import FastAPI

app = FastAPI()

@app.get("/")
def index():
    return {"OK":True}



@app.get('/predict')
# input: X-ray image, or nothing, and we
# tell the function to sample randomly
# from the test subset

# output: Normal/Negative or Pneumonia/Positive,
# perhaps even with confidence of the model attached to this result


def predict(image):
    # convert image to jpeg if provided
    # turn it into a tfds
    # load our best model
    # predict method on that image
    return {'wait': "Diagnostic: Pneumonia"}
