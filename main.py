import uuid
from fastapi import FastAPI
from pydantic import BaseModel
import dynamodb

def create_id():
    id = uuid.uuid4()
    return str(id)
class Note(BaseModel):
    note_id: str | None = None
    desc: str


app = FastAPI()


# GET - Read all notes
@app.get("/notes")
async def root():
    return dynamodb.get_notes()

# GET - Read a single note 
@app.get("/notes/{note_id}")
async def get_note(note_id):
    try:
        note = dynamodb.get_note(note_id)
    except:
        return {}
    
    return note


# POST - Create a new note
@app.post("/notes/")
async def create_note(note: Note):
    new_note = Note(note_id=create_id(), desc=note.desc)
    try:
        dynamodb.create_note(**new_note.__dict__)
    except:
        print(f'Failed to create note with the ID of: {new_note.note_id} at this time.')
        return {}
    # note_list.append(new_note)
    return new_note