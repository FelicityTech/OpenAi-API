# Create the OpenAI client
client = OpenAI(api_key="<OPENAI_API_TOKEN>")

# Create a request to the Chat Completions endpoint
response = client.chat.completions.create(
  # Specify the correct model
  model="gpt-4o-mini",
  # Specify the message keys
  messages=[{"role": "user", "content": "Who developed ChatGPT?"}]
)

print(response)
print(response.choices[0].message.content)