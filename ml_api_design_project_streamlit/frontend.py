import streamlit as st
import requests

api_url="http://127.0.0.1:8000/predict"

st.title("Diabetes Prediction APP")

st.header("Enter The Value Of The Input Features")
f1=st.number_input("How Many Preganancies You had ?", value=0)
f2=st.number_input("Glucose Value",value=148)
f3=st.number_input("Blood Pressure",max_value=140,value=120)
f4=st.number_input("Skin Thickness",value=35)
f5=st.number_input("Insulin",value=0)
f6=st.number_input("BMI Value",value=0)
f8=st.number_input("DiabetesPedigreeFunction")
f9=st.number_input("Enter Your Age",min_value=5, max_value=120)


if st.button('Predict'):
    features={
            'Pregnancies':f1,
            'Glucose':f2,
            'BloodPressure':f3,
            'SkinThickness':f4,
            'Insulin':f5,
            'bmi':f6,
            'DiabetesPedigreeFunction':f8,	
            'Age':f9	
    }

    try:
        response=requests.post(api_url,json=features)
        if response.status_code==201:
            result=response.json()
            st.success(f"Predicted output is :{result}")
        else:
            st.error(f"API Error:{response.status_code}--{response.text}")
    except requests.exceptions.ConnectionError:
        st.error("Could not connect to api servers")