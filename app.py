from ollama import chat

response = chat(
    model='gemma3:latest',
    messages=[{'role': 'user', 'content': 'hello!'}],
)
print(response.message.content)