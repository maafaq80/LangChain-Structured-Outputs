from pydantic import BaseModel,EmailStr,Field
from typing import Optional

class Student(BaseModel):
    
    name:str = "aafaq"
    age:Optional[int]
    email:EmailStr
    cgpa:float=Field(gt=0,lt=10,default=5,description="a floating point number to represent grade of a student ")
    
    
new_student={'age':32,'email':"abc@gmail.com"}  # it will throw an error if you dont follow u the define format 
student=Student(**new_student)

print(student)