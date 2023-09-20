from fastapi import FastAPI, Request
from fastapi.responses import HTMLResponse
from fastapi.staticfiles import StaticFiles
from fastapi.templating import Jinja2Templates
from pymongo import MongoClient

app = FastAPI()

app.mount("/static", StaticFiles(directory="static"), name="static")


templates = Jinja2Templates(directory="templates")

connection = MongoClient("mongodb://localhost:27017/")
db = connection.get_database("notesApp")
notes_collection = db.get_collection("notesApp")


@app.get("/", response_class=HTMLResponse)
async def read_item(request: Request):
    notes = notes_collection.find({})
    new_notes = []
    for note in notes:
        new_notes.append({
            "id": note["_id"],
            "note": note["note"]
        })
    return templates.TemplateResponse("index.html", {"request": request, "new_notes": new_notes})
