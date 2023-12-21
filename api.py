from fastapi import FastAPI, HTTPException
from pydantic import BaseModel
import model


app = FastAPI()

class Request(BaseModel):
    text: str

class Response(BaseModel):
    response: str

@app.post("/tokenizer", response_model=Response)
async def tokenizer(request: Request):
    try:
        response = model.get_json(request.text)
        return {"response": response}
    except Exception as e:
        raise HTTPException(status_code=500, detail="Internal Server Error")
