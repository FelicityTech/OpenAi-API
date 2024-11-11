client = OpenAI(api_key="<OPENAI_API_TOKEN>")

# Create a request to the Chat Completions endpoint
response = client.chat.completions.create(
  model="gpt-3.5-turbo",
  max_tokens=150,
  messages=[
    {"role": "system", "content": "You are a helpful data science tutor."},
    {"role": "user", "content": "What is the difference between a for loop and a while loop?"}
  ]
)

# Extract the assistant's text response
print(response.choices[0].message.content)