from typing import Optional
from fastapi import FastAPI, Path
from pydantic import BaseModel
from fastapi import FastAPI, Request
from fastapi.responses import FileResponse
import requests

app = FastAPI()


@app.get("/")
async def home():
	return{"1":"GET: /spongebob/text=text",     
		   "2":"GET: /captcha/text=text"}
	return{}
	pass




@app.get("/spongebob/text={text}")
async def spongebob(text):
	url = "https://api.devs-hub.xyz/spongebob-timecard?text={}".format(text)
	response = requests.get(url)

	file = open("image/image.png", "wb")
	file.write(response.content)
	file.close()
	return FileResponse("image/image.png")
	pass

@app.get("/captcha/text={text}")
async def captcha(text):
	url = "https://api.cool-img-api.ml/captcha?text={}".format(text)
	response = requests.get(url)

	file = open("image/image.png", "wb")
	file.write(response.content)
	file.close()
	return FileResponse("image/image.png")
	pass

	