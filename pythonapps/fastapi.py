import json

from fastapi import FastAPI, Request, status, Response
from fastapi.responses import JSONResponse
#from concurrent.futures import ThreadPoolExecutor
import uvicorn

app = FastAPI()

@app.get("/hello")
def ping():
    resp = {"Hello":"Rushikesh"}
    return JSONResponse(resp)

@app.post("/callback/{client_id}")
async def callback(client_id:str,request:Request):
    # awaiting on the request data
    data = await request.json()
    client_data = data.get(client_id,"")

    resp = {"client_data":client_data}

    return Response(content=json.dumps(resp),status_code=status.HTTP_200_OK,media_type="application/json")

if __name__ == "__main__":
    uvicorn.run("main:app", host="0.0.0.0", port=80)