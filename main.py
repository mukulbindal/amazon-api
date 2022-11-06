import json
from fastapi import FastAPI, HTTPException

from amazon.GetPage import GetPage
from amazon.PageParser import parse

app = FastAPI()

@app.get("/")
async def root():
    return {"name":"Hellow world"}

@app.get("/api/v1/search/{key}")
def search_product(key):
    amazon_page = GetPage()
    amazon_html = amazon_page.get_page()
    response = parse(amazon_html)
    return response

     