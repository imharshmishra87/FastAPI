from pydantic import BaseModel,EmailStr,AnyUrl,Field,field_validator
from typing import List,Dict,Optional,Annotated


class patientdata(BaseModel):
    name:Annotated[str,Field(name='Enter the name',description='Name Of the Patient')]
    age:Annotated[int, Field(gt=0,le=115)]
    allergies:Optional[List[str]]=None
    married:bool
    height_cm:float=Field(gt=0,strict=True)
    email:EmailStr
    linkedin:AnyUrl

    @field_validator('email')
    @classmethod
    def validateemail(cls,value):
        valid_emails=['icici.com','kotak.com','pnb.com','axis.com']
        val=value.split('@')[-1]
        if val not in valid_emails:
            raise ValueError('Invalid email')
        return value
    
    @field_validator('name')
    @classmethod
    def uppername(cls,value):
       return value.title()

def getvalues(val:patientdata):
    print(val.name)
    print(val.age)
    print(val.allergies)
    print(val.height_cm)
    print(val.email)
    print(val.linkedin)

    # this function expects a patientdata object."

data={'name':'harsh mishra','age':'55','married':True,'height_cm':175,'email':'harsh87@pnb.com','linkedin':'https://www.google.com'}
pt1=patientdata(**data)

getvalues(pt1)