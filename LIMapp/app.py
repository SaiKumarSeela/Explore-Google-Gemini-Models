from dotenv import load_dotenv
import os
import streamlit as st               
import google.generativeai as genai      
load_dotenv()

google_api_key = os.getenv("GOOGLE_API_KEY")

genai.configure(api_key=google_api_key)

# load gemini pro model and get reponse
model = genai.GenerativeModel('gemini-pro')
def get_gemini_response(question):
    response = model.generate_content(question)
    return response.text

# initialize streamlit
st.set_page_config(page_title="Q&A Demo")
st.header("Gemini LLM application")

input = st.text_input("Input:", key="input")
submit = st.button("Ask the question")

if submit:
    response = get_gemini_response(input)
    st.subheader("The response is")
    st.write(response)
    

