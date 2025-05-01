import json

from fastapi import FastAPI, Request
from fastapi.templating import Jinja2Templates



app = FastAPI()
templates = Jinja2Templates(directory="templates")

def load_data():
    with open("data/atp_mentoday.json") as f:
        return json.load(f)

@app.get("/")
async def read_root(request: Request):
    data = load_data()
    return templates.TemplateResponse(
        "index.html",
        {"request": request, "data": data}
    )

print(load_data())

for i in load_data():
    print(i.get("m_name"))