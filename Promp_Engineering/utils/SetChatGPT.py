import json
import openai

def load_key() -> str:
    with open("../.env", "r") as jFile:
        chatgpt_key = json.load(jFile)["keys"]["chatgpt"]

    return chatgpt_key

def get_completion(prompt, model="gpt-3.5-turbo"):

    messages = [{"role": "user", "content": prompt}]
    response = openai.ChatCompletion.create(
        model=model,
        messages=messages,
        temperature=0
    )
    
    return response.choices[0].message["content"]

def get_completion_from_messages(messages, model="gpt-3.5-turbo", temperature=0):
    
    response = openai.ChatCompletion.create(
        model=model,
        messages=messages,
        temperature=temperature, # this is the degree of randomness of the model's output
    )

    return response.choices[0].message["content"]

