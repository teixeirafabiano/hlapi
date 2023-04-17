import random
import json
from datetime import datetime
from dto.hlDto import *
from dlo.HlDLO import *
from dlo.ServiceDLO import *
from dlo.TypeDLO import *
from typing import List, Union

from fastapi import FastAPI, Request, Response
from fastapi.encoders import jsonable_encoder
from fastapi.openapi.docs import get_swagger_ui_html
from fastapi.staticfiles import StaticFiles

from pydantic import BaseModel


class Api(BaseModel):
    title: str = "Hub for Labor API"
    description: str = "Live"


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

@app.get("/workers/service/{service_str}/zipcode/{zipcode_str}")
def searchWorkers(service_str: str, zipcode_str: str):
    nm_service = service_str
    tx_zipcode = zipcode_str
    try:
        objDlo = HlDLO()
        #amount = random.randint(1, 5)
        print("==========", nm_service, tx_zipcode)
        amount = objDlo.selectWorkerByService(nm_service, tx_zipcode)
        print("==========", nm_service, tx_zipcode, amount)

        worker = [{"amount": str(amount), "service": str(nm_service), "zipcode": str(tx_zipcode)}]
        #body = {"worker": worker}
        #json_str = json.dumps(body)
        return worker #body #Response(content=json_str, media_type='application/json')
    except Exception as exc:
        return Response(content="Error when searching for workers", media_type='application/json')

# array = '{"params": ["tbl_service", "nu_id", 1]}'

@app.post("/searchService/")
async def selectService(service_str: str, zipcode_str: str, params_json: str):
    p_json = params_json
    nm_service = service_str
    tx_zipcode = zipcode_str
    print(p_json)
    try:
        objDlo = ServiceDLO()
        #client_host = request.client.host
        register = datetime.today()
        data = json.loads(p_json)
        params = data['params']
        print(params)
        srvc = objDlo.selectService(params)
        print(srvc)
        #header = [{"client_host": client_host, "register": register, "preOrder": str(hash(str(client_host)+str(register)))}]
        header = [{"register": register}]
        service = [{"services": srvc}]

        worker = searchWorkers(nm_service, tx_zipcode)

        body = {"header": header, "service": service, "worker": worker}
        return body
    except Exception as exc:
        return 400

@app.post("/insertService/")
async def insertService(service_str: str, zipcode_str: str, params_json: str):
    p_json = params_json
    nm_service = service_str
    tx_zipcode = zipcode_str
    nu_id = 0
    print(p_json)
    try:
        objDlo = ServiceDLO()
        #client_host = request.client.host
        register = datetime.today()
        nu_id = objDlo.insertService(service_str, p_json)
        #header = [{"client_host": client_host, "register": register, "preOrder": str(hash(str(client_host)+str(register)))}]
        #header = [{"register": register, "preOrder": str(hash(str(nu_id)+str(register)))}]
        service = [{"service_id": nu_id}]

        worker = searchWorkers(nm_service, tx_zipcode)

        body = {"service": service, "worker": worker}
        return body
    except Exception as exc:
        return 400

@app.post("/listAllType/")
async def selectAllType():
    try:
        objDlo = TypeDLO()
        types = objDlo.selectAllType()
        types = [{"types": types}]

        body = {"types": types}
        return body
    except Exception as exc:
        return 400

@app.post("/listTypeByCategory/")
async def selectTypeByCategoryId(id_category: str):
    try:
        objDlo = TypeDLO()
        types = objDlo.selectTypeById(id_category)
        types = [{"types": types}]

        body = {"types": types}
        return body
    except Exception as exc:
        return 400


#@app.post("/")
#async def read_root():
#    return {"Hello": "World"}
#
#@app.get("/")
#async def read_root():
#    return {"Hello": "World"}

@app.get("/status/")
def status(request: Request):
    target = True
    try:
        client_host = request.client.host
        body = [{"client_host": client_host, "target": target}]
        json_str = json.dumps(body)
        return Response(content=json_str, media_type='application/json')
    except Exception as exc:
        target = False
        body = [{"client_host": client_host, "target": target}]
        json_str = json.dumps(body)
        return Response(content=json_str, media_type='application/json')

#@app.post("/status/{status_id}")
#def status(status_id: str, request: Request):
#    client_host = request.client.host
#    return {"client_host": client_host, "status_id": status_id}

@app.post("/service/")
async def service(order: Order, request: Request):
    try:
        client_host = request.client.host
        register = datetime.today()
        header = [{"client_host": client_host, "register": register, "preOrder": str(hash(str(client_host)+str(register)))}]
        service = [{"order": order}]
        worker = searchWorkers("Plumbing", "37915")

        body = {"header": header, "service": service, "worker": worker}
        return body
    except Exception as exc:
        return 400



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
