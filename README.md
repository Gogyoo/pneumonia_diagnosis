# Detect Pneumonia from X-ray Scans

We are using [Chest X-Ray Images- Pneumonia](https://www.kaggle.com/datasets/paultimothymooney/chest-xray-pneumonia”) dataset from Kaggel to train a CNN model for pneumonia detection. The dataset splits pneumonia into two categories: Bacteria and Viral.
The model does not differentiate between these two categories.

### X-ray image
<img src='images/xray.jpeg'>

## Model Deployment
Classification model is deployed with FastAPI and Docker. The endpoint accepts uploaded files and concludes from the image whether it has pneumonia or is normal.
Streamlit is used to create web application for the API. URL to the api is https://api-cwtil3b3qq-ew.a.run.app/

## Run the Detection API on LocalHost

 1. Clone this repository to your local disk.
 2. Run the `requirements.txt` file using `pip install -r requirements.txt`.
 3. Run the `fastapi.py` script using `uvicorn pneumonia.api.fastapi:app --reload`.
 4. Open `127.0.0.1:8000` in your browser.
 5. Choose a lung x-ray image from your disk and click on the `Submit` button.

## Train and Test

1. Run `preprocessor.py` to load images. Change the paths to location where images is saved.
2. Run `inceptionv3.py` to train InceptionV3 model on the data. The model is trained for 20 epochs to obtain the result. You may train longer.
3. Run `evaluate_model()`function inside `inceptionv3.py` to predict test images.

## Result
<p>[==============================] - 8s 389ms/step - loss: 0.7281 - accuracy: 0.8394 - recall: 0.9846 <== That is great! That means we can focus on predicting actual positive cases.
Test Accuracy: 83.94%
Found 4716 files belonging to 2 classes.
148/148 [==============================] - 56s 377ms/step - loss: 0.0470 - accuracy: 0.9811 - recall: 0.9764
Train Accuracy: 98.11%</p>
