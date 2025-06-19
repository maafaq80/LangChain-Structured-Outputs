from langchain_openai import ChatOpenAI
from dotenv import load_dotenv
from typing import TypedDict,Annotated
import os 

load_dotenv()
api_key=os.getenv("OPEN_AI_API_KEY")

class Review(TypedDict):
    summary:Annotated[str,"a brief summary of review"]
    sentiment:Annotated[str,"return the sentiment of review either positive negative or neutrual"]
    
model=ChatOpenAI(model="gpt-4o-mini",
                 openai_api_key=api_key)

structured_model=model.with_structured_output(Review)
result=structured_model.invoke("The hardware is great but the softwaare feels bloated. Thera are too many pre-installed apps that I can't remove. Also the UI tools look outdated compared to the other brands. Hoping for the software update to fix this ")

print(result)

    
