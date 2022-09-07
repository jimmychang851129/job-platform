from fastapi import FastAPI, Response, status, HTTPException
from .database import engine, SessionLocal
from . import schemas, models
from .schemas import Engineer
from .models import Engineer as Eng
from typing import Optional
app = FastAPI()
models.Base.metadata.create_all(engine)
session = SessionLocal()

@app.get('/positions')
def index():
	return {"data": "now we good."}	


@app.post('/positions', status_code=status.HTTP_201_CREATED)
def create_positions(engineer: Engineer):
	#to do : add the new data to table
	engi_dict = engineer.dict()
	print(engi_dict)
	add_engineer = Eng(engi_dict)
	session.add(add_engineer)
	session.commit()
	return {"data":"create new position successfully."}

@app.get('/positions/all')
def return_all_positions():
	ret = []
	for instance in session.query(Eng).order_by(Eng.id):
		# print(instance.returnData())
		ret.append(instance.returnData())
	return {"data": ret}
	
@app.delete('/positions/{id}')
def delete_position(id:int):
	#todo:delete the specific data
	data = session.query(Eng).get(id)
	session.delete(data)
	session.commit()
	return {"data": f"delete the index {id}"}
