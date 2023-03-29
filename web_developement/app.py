import streamlit as st
import json
import requests
import base64
from pathlib import Path
# from multiapp import MultiApp
# from pages import home, about, contact

# app = MultiApp()

# app.add_app("Home", home.app)
# app.add_app("About", about.app)
# app.add_app("Contact", contact.app)

# Defining the functions

def load_lottiefile(filepath : str):
    with open(filepath, "r") as f:
        return json.load(f)


def load_lottieurl(url: str):
    r = requests.get(url)
    if r.status_code != 200:
        return None
    return r.json()


# The top of LungDetect website

st.set_page_config(page_title='Welcome to LungDetect', page_icon=':sparkles:',
                   layout='wide')

# Header section
col1, col2 = st.columns((2, 1))
with col1:
    with st.container():
        st.header('Welcome to LungDetect :sparkles:')

# Subheader
with col2:
    def img_to_bytes(img_path):
        img_bytes = Path(img_path).read_bytes()
        encoded = base64.b64encode(img_bytes).decode()
        return encoded

    def img_to_html(img_path):
        img_html = "<img src='data:image/png;base64,{}' class='img-fluid'>".format(
        img_to_bytes(img_path)
        )
        return img_html

    st.markdown("<p style='text-align: center ; color: grey;'>"+
                img_to_html('web_developement/88293-lungs.gif')
                +"</p>", unsafe_allow_html=True)
# About us and our project

# Add text to the left column
with st.container():
    st.subheader('We are making lung diseases detection easier')
    st.write('Just upload an image of your chest X-ray and get a result in less than a minute!')


# File uploader
uploaded_file = st.file_uploader("Choose an image...", type=["jpg", "jpeg", "png"])
submit_button = st.button('Submit')

if submit_button:
    st.success('The result is ready!', icon="✅")
    response = requests.post(url = 'http://127.0.0.1:8000/predict',
              files={'img': uploaded_file.getvalue()})


    st.write(response.json())

# Add more text

with st.container():
    st.write('---')
    st.header('Overview')
    st.write('##')
    st.write('''
            Pneumonia is an infection that inflames the air sacs in one or both lungs. The air sacs may fill with fluid or pus (purulent material), causing cough with phlegm or pus, fever, chills, and difficulty breathing. A variety of organisms, including bacteria, viruses and fungi, can cause pneumonia.

            Pneumonia can range in seriousness from mild to life-threatening. It is most serious for infants and young children, people older than age 65, and people with health problems or weakened immune systems.
            ''')


# Next section of the website
with st.container():
    st.write('---')
    st.header('The purpose of LungDetect')
    st.write('##')
    st.write('''
            The diagnosis of pneumonia requires a review of chest radiography (CXR) by a highly qualified specialist, laboratory tests, vital signs, and clinical history, which makes its detection a difficult task. It normally presents as an area of increased opacity within the CXR. Even so, the identification of the diagnosis of pneumonia is complex due to other pulmonary conditions such as hemorrhages, lung cancer, postsurgical changes, pulmonary edema, atelectasis, or collapse. The comparison of CRX performed at different times and the relationship with the clinical history is essential for diagnosis.

            This project seeks to design an application for the automatic detection of pneumonia, which may be appropriate in regions where health professionals do not arrive or as support when defining a diagnosis to reduce the mortality rate associated with Pneumonia.
            ''')
