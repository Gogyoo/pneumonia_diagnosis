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
 4. Open (https://anya9889-pneumonia-diagnosis-front-app-mtvurf.streamlit.app/) in your browser.
 5. Choose a lung x-ray image from your disk and click on the `Submit` button.

## Train and Test

1. Run `preprocessor.py` to load images. Change the paths to location where images is saved.
2. Run `inceptionv3.py` to train InceptionV3 model on the data. The model is trained for 20 epochs to obtain the result. You may train longer.
3. Run `evaluate_model()`function inside `inceptionv3.py` to predict test images.

## Result
<p>Using InceptionNet as an implementation of Transfer Learning, we managed an excellent accuracy (97%) and recall (99%). This is important because we want to avoid false negatives (e.g. sending a patient home who is actuall sick). Conversely the model is lenient on false positives (e.g. patients are told they could be sick with pneumonia, but actually aren't) because then the x-ray can be passed on to a health professional for further assessment.</p>
