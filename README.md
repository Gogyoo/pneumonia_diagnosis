# Final_project
# Detect Pneumonia from X-ray Scans

<p>We are using  [Chest X-Ray Images (Pneumonia)](https://www.kaggle.com/datasets/paultimothymooney/chest-xray-pneumonia) dataset from Kaggel to train a CNN model for pneumonia detection. The dataset splits pneumonia into two categories: Bacteria and Viral.
The model does not differentiate between these two categories.</p>

### X-ray image
<img src='images/xray.jpeg' width='100'>

## Model Deployment
<p>Classification model is deployed with FastAPI and Docker. The endpoint accepts uploaded files and concludes from the image whether it has pneumonia or is normal.
Streamlit is used to create web application for the API.</p>

## Run the Detection API on LocalHost
<ol>
 <li>Clone this repository to your local disk.</li>
 <li>Run the **requirements.txt** file using **pip install -r requirements.txt**.</li>
 <li>Run the **fastapi.py** script using **<COMMAND>**.</li>
 <li>Open **127.0.0.1:12000** in your browser.</li>
 <li>Choose a lung x-ray image from your disk and click on the **Predict** button.</li>

## Train and Test
<ul>
<li>Run **preprocessor.py** to load images.Change the paths to location where images is saved.</li>
<li>Run **inceptionv3.py** to train InceptionV3 model on the data. The model is trained for 20 epochs to obtain the result. You may train longer.</li>
<li>Run **evaluate_model()** function inside **inceptionv3.py** to predict test images.

## Result
<p>[==============================] - 8s 389ms/step - loss: 0.7281 - accuracy: 0.8394 - recall: 0.9846 <== That is great! That means we can focus on predicting actual positive cases.
Test Accuracy: 83.94%
Found 4716 files belonging to 2 classes.
148/148 [==============================] - 56s 377ms/step - loss: 0.0470 - accuracy: 0.9811 - recall: 0.9764
Train Accuracy: 98.11%</p>
