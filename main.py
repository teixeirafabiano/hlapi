import random
from datetime import datetime
from dto.hlDto import *
from typing import List, Union

from fastapi import FastAPI, Request
from fastapi.openapi.docs import get_swagger_ui_html
from fastapi.staticfiles import StaticFiles

from pydantic import BaseModel

app = FastAPI(    
	title="Hub for Labor API",
    description="This API has the necessary CRUD to manipulate HL platform services.",
    version="0.0.1",
    terms_of_service="https://hubforlabor.com/terms/",
    contact={
        "name": "Teixeira, Fabiano",
        "url": "https://hubforlabor.com/contact/",
        "email": "teixeirafabiano@gmail.com",
    }
)

#@app.post("/")
#async def read_root():
#    return {"Hello": "World"}
#
#@app.get("/")
#async def read_root():
#    return {"Hello": "World"}

@app.get("/status/{status_id}")
def status(status_id: str, request: Request):
    client_host = request.client.host
    return {"client_host": client_host, "status_id": status_id}

@app.post("/status/{status_id}")
def status(status_id: str, request: Request):
    client_host = request.client.host
    return {"client_host": client_host, "status_id": status_id}

@app.post("/services/")
async def order(order: Order, request: Request):
    client_host = request.client.host
    worker = random.randint(1, 5)
    register = datetime.today()
    return {"client_host": client_host, "order": order, "workers_found": worker, "register": register, "preOrder": str(hash(str(client_host)+str(register)))}

#@app.post("/order/{order_id}")
#def read_root(order_id: str, request: Request):
#    client_host = request.client.host
#    return {"client_host": client_host, "order_id": order_id}
#
#@app.get("/items/{item_id}")
#async def read_item(item_id: int, q: Union[str, None] = None):
#    return {"item_id": item_id, "q": q}

#@app.put("/items/{item_id}")
#async def update_item(item_id: int, item: Item):
#    return {"item_name": item.name, "item_id": item_id}

#@app.get("/orders/{order_id}")
#async def read_item(item_id: int, q: Union[str, None] = None):
#    return {"item_id": item_id, "q": q}