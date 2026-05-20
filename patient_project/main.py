from fastapi import FastAPI,Path,HTTPException,Query
from pydantic import BaseModel,computed_field, model_validator,Field,field_validator
from fastapi.responses import JSONResponse
from typing import Annotated,Literal,Optional
import json

app=FastAPI()


class model(BaseModel):
    id:Annotated[str,Field(..., description="Enter The ID of the Patient",examples=['P1001'])]
    name:Annotated[str,Field(...,description="Enter The Name Of The Patient")]
    city:Annotated[str,Field(...,description="Enter The City Of The Patient")]
    age:Annotated[int,Field(...,description="Enter The Age Of The Patient",gt=0 , le=120)]
    gender:Annotated[Literal['Male','Female','Other'],Field(...,description="Enter The Gender Of The Patient")]
    height_cm:Annotated[float,Field(...,description="Enter The height_cm Of The Patient",gt=0)]
    weight_kg:Annotated[float,Field(...,description="Enter The weight_kg Of The Patient",gt=0)]

    @field_validator('name')
    @classmethod
    def validatenames(cls,value):
        return value.title()
    

    @field_validator('city')
    @classmethod
    def validatecity(cls,value1):
        return value1.title()

    @computed_field
    @property
    def bmi(self)->int:
        return round(self.weight_kg*10000 / self.height_cm**2,2)
    
    @computed_field
    @property
    def final_verdict(self)->str:
            if self.bmi < 18.5:
                return "Underweight"
            elif self.bmi < 25:
                return "Healthy"
            elif self.bmi < 30:
                return "Overweight"
            elif self.bmi < 35:
                return "Obese"
            elif self.bmi < 40:
                return "Critical Obesity"
            else:
                return "Severe Obesity"
            
class update_model(BaseModel):

    name:Annotated[Optional[str],Field(default=None)]
    city:Annotated[Optional[str],Field(default=None)]
    age:Annotated[Optional[int],Field(t=0 , le=120,default=None)]
    gender:Annotated[Optional[Literal['Male','Female','Other']],Field(default=None)]
    height_cm:Annotated[Optional[float],Field(default=None)]
    weight_kg:Annotated[Optional[float],Field(default=None)]

def load_data():
    with open('patients.json','r') as f:
        data=json.load(f)
    return data

def save_data(data):
    with open('patients.json','w') as f:
        json.dump(data,f)

@app.get("/")
def say_hello():
    return {"say:":"hello harsh"}


@app.get("/view")
def view_data():
    data=load_data()
    return data


@app.get('/patients/{patient_id}')
def load_patient(patient_id:str=Path(..., description="Enter The patient id",examples='P1001')):
    data=load_data()
    # for i in data.keys():
    #     if i==patient_id:
    #         return data.get(i)

    if patient_id in data:
        return data[patient_id]
    raise HTTPException(status_code=401,detail="Patient id does not exists")


@app.get('/sort')
def querypara(sort_by:str=Query(..., description='Sort the details by Height, Weight or BMI'),order_by:str=Query('asc',description="Order the data by asending or descending")):
    val=["height_cm","bmi","city"]
    order=["asc","desc"]
    dataval=load_data()


    if sort_by not in val:
        raise HTTPException(status_code=400,detail='Invalid String provided')
    
    if order_by not in order:
        raise HTTPException(status_code=400,detail='Invalid String provided')

    
    sorted_order=True if order_by =='desc' else False
    
    return sorted(dataval.values(),key=lambda x:x.get(sort_by,0),reverse=sorted_order)


@app.post('/create')
def uplaod(patient:model):
    data=load_data()
    if patient.id in data:
        raise HTTPException(status_code=400,detail="Patient already exists in the database")
    
    data[patient.id]=patient.model_dump(exclude=['id'])

    save_data(data)

    return JSONResponse(status_code=201, content="Data Submmited successfully")

@app.put('/update/{patient_id}')
def update(patient_id:str,data:update_model):

    dataloaded=load_data()
    if patient_id not in dataloaded:
        raise HTTPException(status_code=404, detail="Patient id doesn't exits")
    
    filtered_data=dataloaded.get(patient_id)
    data_to_update=data.model_dump(exclude_unset=True)

    for i in data_to_update:
        if i in filtered_data:
            filtered_data[i]=data_to_update.get(i)

    filtered_data['id']=patient_id
    obj2=model(**filtered_data)
    new_validated_data=obj2.model_dump(exclude=['id'])

    dataloaded[patient_id]=new_validated_data
    save_data(dataloaded)

    return JSONResponse(status_code=201,content={'message':'Patient data updated successfully'})


@app.delete('/delete/{patient_id}')
def deletedata(patient_id:str):
    data=load_data()

    if patient_id not in data:
        raise HTTPException(status_code=404, detail="patient_id doesn't exists")
    
    del data[patient_id]

    save_data(data)
    return JSONResponse(status_code=202, content="Successfully deleted")
    

    