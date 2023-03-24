import streamlit as st
import json
import requests
from streamlit_lottie import st_lottie

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

with st.container():
    st.header('Welcome to LungDetect :sparkles:')

# Subheader

with st.container():
    st.subheader('We are making lung diseases detection easier')
    st.write('Just upload an image of your chest X-ray and get a result in less than a minute!')
    # st.write('[Learn more >]link to our github/some research papers?')

# About us and our project

with st.container():
    st.write('---')
    left_column, right_column = st.columns(2)
    with left_column:
        st.header('Overview')
        st.write('##')
        st.write('''
                 Pneumonia is an infection that inflames the air sacs in one or both lungs. The air sacs may fill with fluid or pus (purulent material), causing cough with phlegm or pus, fever, chills, and difficulty breathing. A variety of organisms, including bacteria, viruses and fungi, can cause pneumonia.

                Pneumonia can range in seriousness from mild to life-threatening. It is most serious for infants and young children, people older than age 65, and people with health problems or weakened immune systems.
                 ''')

with st.container():
    st.write('---')
    left_column, right_column = st.columns(2)
    with left_column:
        st.header('The purpose of LungDetect')
        st.write('##')
        st.write('''
                 The diagnosis of pneumonia requires a review of chest radiography (CXR) by a highly qualified specialist, laboratory tests, vital signs, and clinical history, which makes its detection a difficult task. It normally presents as an area of increased opacity within the CXR. Even so, the identification of the diagnosis of pneumonia is complex due to other pulmonary conditions such as hemorrhages, lung cancer, postsurgical changes, pulmonary edema, atelectasis, or collapse. The comparison of CRX performed at different times and the relationship with the clinical history is essential for diagnosis.

                This project seeks to design an application for the automatic detection of pneumonia, which may be appropriate in regions where health professionals do not arrive or as support when defining a diagnosis to reduce the mortality rate associated with Pneumonia.
                 ''')


# Inserting an image of lungs

lottie_coding = load_lottieurl('https://assets4.lottiefiles.com/packages/lf20_0l21klz3.json')
# hello_lottie = load_lottieurl('https://assets4.lottiefiles.com/packages/lf20_0l21klz3.json')
st_lottie(lottie_coding, speed = 1)

# Use st_css to change the size and position of the animation
st.write('<style>div.WidgetBox.stLottie{width:50px !important;height:50px !important;margin:0 auto;}</style>', unsafe_allow_html=True)

# Section where a user can drop an image and get a result
uploaded_file = st.file_uploader("Choose a chest X-ray image", type=["jpg", "jpeg", "png"])
