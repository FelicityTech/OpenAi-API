client = OpenAI(api_key="<OPENAI_API_TOKEN>")

response = client.chat.completions.create(
    model="gpt-4o-mini",
    # Write your prompt
    messages=[{"role": "user", "content": "who are  the paypal mafia?"}],
    max_tokens=200
)

print(response.choices[0].message.content)