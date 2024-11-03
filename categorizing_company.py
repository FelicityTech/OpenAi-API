from openai import OpenAI
client = OpenAI(api_key="<OPENAI_API_TOKEN>")

# Define a prompt for the categorization
prompt = "catergorise these companies into Tech, Energy, Luxury Goods or Investment: Apple, Microsoft, Saudi Aramco, Alphabet, Amazon, Berkshire Hathaway, NVIDIA, Meta, Tesla, LVMH"

# Create a request to the Chat Completions endpoint
response = client.chat.completions.create(
  model="gpt-4o-mini",
  messages=[{"role":"user", "content": prompt}],
  max_tokens=100,
  temperature=0.5
)

print(response.choices[0].message.content)