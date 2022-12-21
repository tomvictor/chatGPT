'''
Here is an example of a WebSocket program using FastAPI in
Python that outputs "hello" when a client connects:


This code creates a FastAPI app and mounts static files from the
"static" directory. It also defines a WebSocket endpoint at "/ws"
using the @app.websocket decorator. When a client connects to the WebSocket, the
websocket_endpoint function is called and the hello message
is sent to the client using the send_text method.

'''
from fastapi import FastAPI
from fastapi.responses import HTMLResponse
from fastapi.staticfiles import StaticFiles
from fastapi.templating import Jinja2Templates
from fastapi.websockets import WebSocket

app = FastAPI()
templates = Jinja2Templates(directory="templates")
app.mount("/static", StaticFiles(directory="static"), name="static")

@app.websocket("/ws")
async def websocket_endpoint(websocket: WebSocket):
    await websocket.accept()
    await websocket.send_text("hello")

@app.get("/")
def read_root(request):
    return templates.TemplateResponse("index.html", {"request": request})
