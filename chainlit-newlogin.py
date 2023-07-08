import chainlit as cl
from constants import greeting, name_check, change_name
import requests

@cl.on_message
async def retrieve_documents(message: str):
    message_low = message.lower()

    

    response = requests.post("http://localhost:8080/retrieve", json=data)
    print(response.json())

    if message_low in greeting:
        res = "Hi ! Welcome to AI-Bot"
    elif message_low in name_check:
        res = "I am AI-Bot . Machine learning model"
    elif message_low.startswith(tuple(change_name)):
        res = "Sorry i can't change my name as i am machine learning model"
    else:
        data = {"query": message_low, "collection_name": "my_collection"}
        endpoint = "http://34.18.51.93:8080/retrieve"
        response = requests.post(endpoint, params=data)


    await cl.Message(
        content=f"Received: {res}",
    ).send()
