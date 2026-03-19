import google.genai as genai

def create_client(api_key):
    client = genai.Client(api_key=api_key)
    return client
