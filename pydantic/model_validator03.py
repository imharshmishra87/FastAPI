from pydantic import BaseModel,model_validator
from typing import Dict

class data(BaseModel):
    name:str
    age:int
    contact:Dict[str,str]

    @model_validator(mode='after')
    def validation(data):
        if data.age>60 and 'emergency' not in data.contact:
            raise ValueError('Patient elder than 60 should have an emrgency contact number')
        return data



def getdata(val:data):
    print(val.name)
    print(val.age)
    print(val.contact)
    

info={'name':'Harsh','age':25,'contact':{'emergency':'5689755445','address':'rehli'}}
obj=data(**info)
getdata(obj)