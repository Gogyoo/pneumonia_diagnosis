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

with st.container:
    st.subheader('We are making lung diseases detection easier')
    st.write('Just upload an image of your chest X-ray and get a result in less than a minute')
    st.write('[Learn more >]'('link to our github/some research papers?'))

# About us and our project

with st.container:
    st.write('---')
    left_column, right_column = st.columns(2)
    with left_column:
        st.header('What we do')
        st.write('##')
        st.write('''
                 We are a team of 4 people etc...
                 ''')

# Inserting an image of lungs

lottie_coding = load_lottiefile('https://assets4.lottiefiles.com/packages/lf20_0l21klz3.json')
hello_lottie = load_lottieurl('https://assets4.lottiefiles.com/packages/lf20_0l21klz3.json')
st_lottie(lottie_coding, speed = 1)

# Section where a user can drop an image and get a result
