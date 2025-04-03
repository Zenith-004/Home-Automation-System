import ollama

client = ollama.Client()

model = "mistral:latest"
prompt ="What is photosynthesis?"

response = client.generate(model=model, prompt=prompt)

print("Response from Ollama:")
print(response.response)