
import pandas as pd


import easyocr as ocr  #OCR
import streamlit as st  #Web App

import pandas as pd
from PIL import Image #Image Processing
import numpy as np #Image Processing 

#title
st.title("BizCard - Extract Text from Business Cards")

#subtitle
st.markdown("## Optical Character Recognition - Using `easyocr`, `streamlit`")

st.markdown("")

#image uploader
image = st.file_uploader(label = "Upload your image here",type=['png','jpg','jpeg'])
submitted1 = input_form.form_submit_button("Save to Database")


def load_model(): 
    reader = ocr.Reader(['en'],model_storage_directory='.')
    return reader 

reader = load_model() #load model
input_form = st.form("input_form")

if image is not None:

    input_image = Image.open(image) #read image
    st.image(input_image) #display image

    with st.spinner("🤖 AI is at Work! "):
        

        result = reader.readtext(np.array(input_image))

        result_text = [] #empty list for results
        

        for text in result:
            result_text.append(text[1])

        st.write(result_text)
    #st.success("Here you go!")
    st.balloons()

else:
    st.write("Upload an Image")
if submitted1 is True:
    # Making a Connection to MongoClient
        client = pym.MongoClient("mongodb+srv://Sree:Sree123@cluster0.j4yl447.mongodb.net/?retryWrites=true&w=majority")

     # CREATING A DATABASE:
        db = client["BizCard"]
