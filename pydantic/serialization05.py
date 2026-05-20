from pydantic import BaseModel

class address(BaseModel):
    pin:int=470228
    city:str
    state:str

class patientsdata(BaseModel):
    name:str
    age:int
    gender:str
    address_val:address

address_val={'city':'Rehli','state':'Madhya Pradesh'}
add1=address(**address_val)

data_patients={'name':'Harsh','age':22,'gender':'Male','address_val':add1}
data1=patientsdata(**data_patients)

temp=data1.model_dump(exclude_unset=True) # model_dump() is used to convert the object into a dictionary.
temp1=data1.model_dump_json(exclude={'address_val':'state'}) # model_dump_json() is used to convert the object into a json.



print(temp)


