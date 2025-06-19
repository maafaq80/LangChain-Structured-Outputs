from langchain_openai import ChatOpenAI
from dotenv import load_dotenv
from typing import TypedDict,Annotated,Optional,Literal
from pydantic import BaseModel,Field,EmailStr

import os 

load_dotenv()
api_key=os.getenv("OPEN_AI_API_KEY")

class Review(TypedDict):
    key_themes:list[str]=Field(description="write down all the themes discussed in the review")
    summary:str= Field(default=None,description="a brief summary of review")
    sentiment:Literal['pos','neg']=Field(description="return the sentiment of review either positive or negative")
    name: Optional[str]=Field(description="write the name of the reviewer if the name of the person is not avaliable in the review ignore this field ")
    
model=ChatOpenAI(model="gpt-4o-mini",
                 openai_api_key=api_key)

structured_model=model.with_structured_output(Review)
result=structured_model.invoke("""
    I recently upgraded to the Samsung Galaxy S24 Ultra, and I must say, it’s an absolute powerhouse! The Snapdragon 8 Gen 3 processor makes everything lightning fast—whether I’m gaming, multitasking, or editing photos. The 5000mAh battery easily lasts a full day even with heavy use, and the 45W fast charging is a lifesaver.

The S-Pen integration is a great touch for note-taking and quick sketches, though I don't use it often. What really blew me away is the 200MP camera—the night mode is stunning, capturing crisp, vibrant images even in low light. Zooming up to 100x actually works well for distant objects, but anything beyond 30x loses quality.

However, the weight and size make it a bit uncomfortable for one-handed use. Also, Samsung’s One UI still comes with bloatware—why do I need five different Samsung apps for things Google already provides? The $1,300 price tag is also a hard pill to swallow.

Pros:
Insanely powerful processor (great for gaming and productivity)
Stunning 200MP camera with incredible zoom capabilities
Long battery life with fast charging
S-Pen support is unique and useful

Review by Muhammad aafaq 
""")

output=dict(result)
print(output)

    
 