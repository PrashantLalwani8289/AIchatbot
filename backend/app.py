from fastapi import FastAPI
from openai import OpenAI
from typing import Any

app = FastAPI();
from os import environ

import openai 
from openai import RateLimitError


environ["OPENAI_API_KEY"] = "sk-proj-5M4Lv5VET8yXb5kMCBfKT3BlbkFJPoJJX6vLykG3LP3FiaqK"


client = openai.AsyncOpenAI(
    api_key="sk-proj-5M4Lv5VET8yXb5kMCBfKT3BlbkFJPoJJX6vLykG3LP3FiaqK",
)


import google.generativeai as genai



genai.configure(api_key="AIzaSyA49LZ1-L4_QwCqTLo2Y8Yybisxhe2YiYo")
model = genai.GenerativeModel('gemini-pro')


class ChatHistory:
    history = []
    def __init__(self):
        self.history = []

    def add_message(self, user, message):
        self.history.append({"user": user, "message": message})

    def get_history(self):
        return self.history

chat_history = ChatHistory()

chat_history.add_message("User", "Hello!")
chat_history.add_message("Bot", "Hi there!")









def chatbot_response(history, user_message):
    # Simulate chatbot processing using history
    response =  model.generate_content(f" here is chat history {history} and {always} {user_message}", stream=True)
    return response










always = "You are a Bot and you can answer on you own and can take help from previous chat history if you don't know the answer and analyze it"


@app.get('/{text}')
def to_markdown(text:str):
    message = text
    response = chatbot_response(chat_history,message)
    data = ""
    for chunk in response:
        print(chunk.text)
        temp = chunk.text
        for ch in temp:
            if ch == "\n":
                data += ""
            else:
                data += ch
    chat_history.add_message(message,data)
        # print("_"*80)
        # print(data)
    l = chat_history.history
    for i in range(len(l)):
        chat = l[i]
        print(chat)
        print("\n")
        
    return {"response" : data}
  




# completion = client.chat.completions.create(
#   model="gpt-3.5-turbo",
#   messages=[
#     {"role": "system", "content": "You are a poetic assistant, skilled in explaining complex programming concepts with creative flair."},
#     {"role": "user", "content": "Compose a poem that explains the concept of recursion in programming."}
#   ]
# )






