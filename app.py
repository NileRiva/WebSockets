# app.py
import uvicorn
from fastapi import FastAPI, WebSocket
from fastapi import FastAPI,HTTPException,Request
from datetime import datetime
from timeit import default_timer as timer
import csv


file = open('data.csv', 'w', newline='')
writer = csv.writer(file)

app = FastAPI()
@app.websocket("/test")
async def test(websocket: WebSocket):
    file = open('data.csv', 'w', newline='')
    writer = csv.writer(file)  
    start = timer()
    await websocket.accept()
    end = timer()
    print(end - start)    
    while True:
        #receive a json object
        start = timer()
        request = await websocket.receive_json()
        end = timer()
        writer.writerow([end-start])
        print(end - start)


if __name__ == "__main__":
    uvicorn.run("app:app",host="0.0.0.0")

#Store up in array and add up if certain number reached

