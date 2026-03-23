from dotenv import load_dotenv
load_dotenv()

from langchain_groq import ChatGroq

llm = ChatGroq(model = "openai/gpt-oss-120b")

from pydantic import BaseModel

class Schema(BaseModel):
    price: float
    eps: float

resp = llm.invoke("Extract Price and EPS from this report: "
                  "NVIDIA reported quarterly EPS of 2.3 and "
                  "their current price is $100.")

print(resp)