from pydantic import BaseModel

class address(BaseModel):
    pin:int
    city:str
    state:str

class patientsdata(BaseModel):
    name:str
    age:int
    gender:str
    address_val:address

address_val={'pin':470227,'city':'Rehli','state':'Madhya Pradesh'}
add1=address(**address_val)

data_patients={'name':'Harsh','age':22,'gender':'Male','address_val':add1}
data1=patientsdata(**data_patients)

print(data1.name)
print(data1.address_val.pin)


