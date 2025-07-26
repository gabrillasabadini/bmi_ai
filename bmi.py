import os
import streamlit as st
from dotenv import load_dotenv
load_dotenv()
import pandas as pd
import google.generativeai as genai


# Configure the api key

key = os.getenv('GOOGLE_API_KEY')
genai.configure(api_key=key)

# STRUCTURING THE APP
st.header("👨‍⚕️ Healthcare :blue[Advisor] ⚕️", divider="green")

# Sidebar for input
st.sidebar.header('Enter Height and Weight here')
height_input = st.sidebar.text_input('Enter your height in meters:')
weight_input = st.sidebar.text_input('Enter your weight in kgs:')

# Try to convert input and calculate BMI
try:
    height = pd.to_numeric(height_input)
    weight = pd.to_numeric(weight_input)
    if height > 0 and weight > 0:
        bmi = weight / (height ** 2)
        st.sidebar.success(f"✅ Your BMI is: {bmi:.2f}")
    else:
        st.sidebar.write(" Please enter positive values for height and weight.")
except:
    st.sidebar.info("ℹ️ Please enter numeric values to calculate BMI.")

st.subheader('Enter height and weight values in sidebar.')

input = st.text_input('Enter your question here')

submit = st.button('Submit')
model = genai.GenerativeModel('gemini-1.5-flash')
def generate_info(input):
    
    if input is not None:
        
        prompt = f'''You are an Health and Fitness assistance you should help the user 
        and gudie them for their fitness and diet. Answer the question in such a way 
        that absed on bmi {bmi} state the conditions and suggest them the diet. If any questions
        comes for medications mention them that always need to get doctors guidence before
        any medications'''
        
        
        result = model.generate_content(input + prompt)
        
        return result.text   
        
if submit:
    with st.spinner('Result is loading...'):
        response = generate_info(input)
    st.subheader(':red[Result]')
    st.write(response)
    
    

