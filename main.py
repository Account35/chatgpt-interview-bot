from fastapi import FastAPI, UploadFile
from dotenv import load_dotenv

import openai
import os

load_dotenv()

openai.api_key = os.getenv("OPENAI_AI_KEY")
openai.organization = os.getenv("OPEN_AI_ORG")

app = FastAPI()


@app.post("/talk")
async def post_audio(file: UploadFile):
    audio_file= open(file.filename, "rb")
    transcription = open.audio.transcriptions.create( model="whisper-1", file=audio_file) 
    print(transcription)
   

