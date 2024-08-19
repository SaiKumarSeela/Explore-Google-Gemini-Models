import PIL.Image
from dotenv import load_dotenv
import os
import streamlit as st               
import google.generativeai as genai      
load_dotenv()
import PIL

google_api_key = os.getenv("GOOGLE_API_KEY")

genai.configure(api_key=google_api_key)

# load gemini pro model and get reponse
model = genai.GenerativeModel('gemini-1.5-flash')
def get_gemini_response(input, image):
    if input!="":
        response = model.generate_content([input,image])
    else:
        response = model.generate_content(image)
    return response.text


# initialize streamlit
st.set_page_config(page_title="Gemini image demo")
st.header("Gemini LIM application")

input = st.text_input("Input:", key="input")

uploaded_file = st.file_uploader("Choose an image..", type=["jpg","jpeg","png"])
image = ""
if uploaded_file is not None:
    image = PIL.Image.open(uploaded_file)
    st.image(image, caption='Uploaded Image', use_column_width= True)


submit = st.button("Tell me about the image")

if submit:
    response = get_gemini_response(input,image)
    st.subheader("The Response is")
    st.write(response)

    

