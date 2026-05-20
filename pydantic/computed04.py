from pydantic import BaseModel,EmailStr,AnyUrl,Field,computed_field
from typing import List,Dict,Optional,Annotated

class patientdata(BaseModel):
    name:Annotated[str,Field(name='Enter the name',description='Name Of the Patient')]
    age:Annotated[int, Field(gt=0,le=115)]
    allergies:Annotated[Optional[List[str]],Field(default=None)]
    married:bool
    height_m:float=Field(gt=0,strict=True)
    weight_in_kg:float
    email:EmailStr
    linkedin:AnyUrl

    @computed_field
    @property
    def bmi(self)->float:
        bmi=round(self.weight_in_kg/self.height_m**2,2)
        return bmi
    

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


def getvalues(val:patientdata):
    print(val.name)
    print(val.age)
    print(val.allergies)
    print(val.height_m)
    print(val.email)
    print(val.linkedin)
    print(f"Bmi is {val.bmi}")
    print(val.final_verdict)

    # this function expects a patientdata object."

data={'name':'Harsh','age':'55','married':True,'height_m':0.75,'weight_in_kg':98,'email':'harsh87@gmai.com.in','linkedin':'https://www.google.com'}
pt1=patientdata(**data)

getvalues(pt1)