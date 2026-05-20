from pydantic import BaseModel,EmailStr,AnyUrl,Field
from typing import List,Dict,Optional,Annotated

class patientdata(BaseModel):
    name:Annotated[str,Field(name='Enter the name',description='Name Of the Patient')]
    age:Annotated[int, Field(gt=0,le=115)]
    allergies:Annotated[Optional[List[str]],Field(default=None)]
    married:bool
    height_cm:float=Field(gt=0,strict=True)
    email:EmailStr
    linkedin:AnyUrl

def getvalues(val:patientdata):
    print(val.name)
    print(val.age)
    print(val.allergies)
    print(val.height_cm)
    print(val.email)
    print(val.linkedin)

    # this function expects a patientdata object."

data={'name':'Harsh','age':'55','married':True,'height_cm':175,'email':'harsh87@gmai.com.in','linkedin':'https://www.google.com'}
pt1=patientdata(**data)

getvalues(pt1)