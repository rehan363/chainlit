import chainlit as cl
from openai import AsyncOpenAI
from dotenv import load_dotenv
import os 
load_dotenv()

@cl.on_chat_end
async def on_chat_end():
    await cl.Message(
        content="Goodbye! Have a great day!",
    ).send()

@cl.set_starters
async def set_starter():
    return[
        cl.Starter(
            label= "brain stroming",
            message= "brain strom on ternding AI topics",
            
        ),

        cl.Starter(
            label= "help",
            message= "I can help you with AI topics",
            
        ),
        cl.Starter(
            label="Python script for daily email reports",
            message="Write a script to automate sending daily email reports in Python, and walk me through how I would set it up.",
            
            ),
        cl.Starter(
            label="Text inviting friend to wedding",
            message="Write a text asking a friend to be my plus-one at a wedding next month. I want to keep it super short and casual, and offer an out.",
            ),
                    ]


# 
client= AsyncOpenAI(
    api_key=os.getenv("GEMINI_API_KEY"),
)

cl.instrument_openai()

settings= {
    "model": "gemini/gemini-1.5-pro"
}

@cl.on_message
async def on_message(message: cl.Message):
   response= await client.chat.completions.create(
       messages=[
           {"content": "you are a helpful AI assistant answering user quries smoothly", 
            "role": "system"},
            {
                "content": message.content,
                "role": "user"
            }
       ],
       **settings
    )
   await cl.Message(content= response.choices[0].message.content).send()