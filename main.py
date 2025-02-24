from fastapi import FastAPI
from pydantic import BaseModel

class Note(BaseModel):
    note_id: str | None = None
    desc: str

note_list = []

app = FastAPI()


@app.get("/")
async def root():
    return {"notes": note_list}
