client = OpenAI(api_key="<OPENAI_API_TOKEN>")

# Open the audio.wav file
audio_file = open("audio.wav", "rb")

# Write an appropriate prompt to help the model
prompt = "Audio relates to the recent World Bank report"

# Create a translation from the audio file
response = client.audio.translations.create(model="whisper-1", file=audio_file, prompt=prompt)

print(response.text)