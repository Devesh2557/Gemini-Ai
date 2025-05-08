from dotenv import load_dotenv
load_dotenv()
import streamlit as st
import os 
import google.generativeai as genai


genai.configure(api_key=os.getenv("GOOGLE-API-KEY"))

model=genai.GenerativeModel("gemini-2.0-flash")

def my_output(query):
    response=model.generate_content(query)
    return response.text

# Ui development using streamlit

st.set_page_config(page_title="Gemini-AI")
st.header("Gemini-AI")
input=st.text_input("Input",key="Input")
submit=st.button("Enter")

if submit:
    response=my_output(input)
    st.write(response)