from typing import List, Union
from pydantic import BaseModel

class Order(BaseModel):
	zipcode: str
	service: str
	project: str
	describe: str
	emergency: str
	repair: List[str] = []
	replace: List[str] = []
	location: str
	status: str
	completed: str
	street: str
	city: str
	f_name: str
	l_name: str
	phone: str
	email: str

external_data = {
    "zipcode": "37915",
    "service": "plumbing",
    "descrepair": ["not work", "leaking pipe", "slow drain"]
}

#order = Order(**external_data)
#print(order.service)

class Item(BaseModel):
    name: str
    price: float
    is_offer: Union[bool, None] = None
