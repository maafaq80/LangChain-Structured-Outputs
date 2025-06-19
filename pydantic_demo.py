from pydantic import BaseModel

class Student(BaseModel):
    
    name:str 
    
    
new_student={'name':'aafaq'}  # it will throw an error if you dont follow u the define format 
student=Student(**new_student)

print(student)