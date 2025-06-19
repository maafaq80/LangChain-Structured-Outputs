from pydantic import BaseModel

class Student(BaseModel):
    
    name:str = "aafaq"
    
    
new_student={}  # it will throw an error if you dont follow u the define format 
student=Student(**new_student)

print(student)