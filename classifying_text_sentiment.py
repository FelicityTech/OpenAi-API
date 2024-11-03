client = OpenAI(api_key="<OPENAI_API_TOKEN>")

# Define a multi-line prompt to classify sentiment
prompt = "Classify the sentiment of the following statements to either negative, positive or neutral: Unbelievably good!. Shoes fell appart on the second use. The shoes look nice, but they aren't very comfortable. Can't wait to show them off!."

# Create a request to the Chat Completions endpoint
response = client.chat.completions.create(
  model="gpt-4o-mini",
  messages=[{"role":"user", "content":prompt}],
  max_tokens=100
)

print(response.choices[0].message.content)