client = OpenAI(api_key="<OPENAI_API_TOKEN>")

# Create a request to the Chat Completions endpoint
prompt="write haiku about fast-food"
response = client.chat.completions.create(
  model="gpt-4o-mini",
  messages=[{"role":"user", "content":prompt }],
  max_tokens=100
)

print(response.choices[0].message.content)