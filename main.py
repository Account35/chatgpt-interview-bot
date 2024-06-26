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
   user_message = transcribe_audio(file)
   chat_response = get_chat_response(user_message)

# function
def transcribe_audio(file):
    #audio_file= open(file.filename, "rb")
    #transcription = open.audio.transcriptions.create( model="whisper-1", file=audio_file) 
    transcription = {"role": "user", "content": "Hello"}
    print(transcription)
    return{"message": "Audio has been transcribed"}

def get_chat_response(user_message):
    messages = load_messages()
    messages.append(user_message)


def load_messages():
    messages = []
    file = 'database.json'

    empty = os.stat(file).st_size == 0

    if not empty:
        with open(file) as db_file:
        data = json.load(db_file)
        for item in data:
            messages.append(item)
        
    else:
        messages.append(
            {"role": "system", "content": "You are  a searche engine assistant. Ask short question to get clear response. Your name is Greg. Keep responses 30minutes and be funny sometimes"}
        )

    return messages



   

