from fastapi import APIRouter, Request, Form
from fastapi.responses import HTMLResponse
from fastapi.templating import Jinja2Templates
from models.note import NoteBase
from config.db import notes_collection
from schemas.note import note_entity, note_entities

note = APIRouter()
templates = Jinja2Templates(directory="templates")


@note.get("/", response_class=HTMLResponse)
async def read_item(request: Request):
    notes = notes_collection.find({})
    new_notes = []
    for entry in notes:
        title = entry.get("title", "N/A")  # Default to "N/A" if 'title' does not exist
        description = entry.get("description", "N/A")  # Default to "N/A" if 'description' does not exist
        new_notes.append({
            "id": entry["_id"],
            "title": title,
            "description": description
        })
    return templates.TemplateResponse("index.html", {"request": request, "new_notes": new_notes})


@note.post("/")
async def create_item(request: Request, title: str = Form(...), description: str = Form(...)):
    print(f"Received title: {title}, description: {description}")  # Debugging line
    new_entry = {"title": title, "description": description}
    result = notes_collection.insert_one(new_entry)
    return templates.TemplateResponse("index.html", {"request": request, "result": result})


