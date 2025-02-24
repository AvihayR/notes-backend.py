from fastapi import FastAPI
from pydantic import BaseModel
import uuid

class Note(BaseModel):
    note_id: str | None = None
    desc: str

def create_id():
    id = uuid.uuid4()
    return str(id)

note_list = []
app = FastAPI()


@app.get("/")
async def root():
    return {"notes": note_list}

@app.post("/notes/")
async def create_note(note: Note):
    new_note = Note(note_id=create_id(), desc=note.desc)
    note_list.append(new_note)
    return new_note