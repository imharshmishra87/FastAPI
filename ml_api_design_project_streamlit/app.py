from fastapi import FastAPI
from fastapi.responses import JSONResponse
from pydantic import BaseModel,Field,computed_field
from typing import Annotated
import pickle
import pandas as pd
import sklearn 


app=FastAPI()

with open('model.pkl','rb') as f:
    model=pickle.load(f)

class data(BaseModel):
    Pregnancies:Annotated[int,Field(..., description="Enter The pregnancies Value")]
    Glucose:Annotated[int,Field(..., description="Enter The Glucose Value")]
    BloodPressure:Annotated[int,Field(..., description="Enter The Blood Pressure Value")]
    SkinThickness:Annotated[int,Field(..., description="Enter The Skin Thickness Value")]
    Insulin:Annotated[int,Field(..., description="Enter The Insulin Value")]
    bmi:Annotated[float,Field(...,description="Enter The BMI value" ,gt=0)]

    DiabetesPedigreeFunction:Annotated[float,Field(..., description="Enter The DPF value")]
    Age:Annotated[int,Field(..., description="Enter The age",gt=0, le=120)]


    

@app.post('/predict')
def predict_output(value:data):
    dataframe=pd.DataFrame([{
        'Pregnancies':value.Pregnancies,
        'Glucose':value.Glucose,
        'BloodPressure':value.BloodPressure,
        'SkinThickness':value.SkinThickness,
        'Insulin':value.Insulin,
        'BMI':value.bmi,
        'DiabetesPedigreeFunction':value.DiabetesPedigreeFunction,
        'Age':value.Age
    }])

    predicted=model.predict(dataframe)[0].item()
    return JSONResponse(status_code=201, content={'Predicted Output':predicted})








    