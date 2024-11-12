client = OpenAI(api_key="<OPENAI_API_TOKEN>")

# Open the datacamp-q2-roadmap.mp3 file
audio_file = open("datacamp-q2-roadmap.mp3", 'rb')

# Create a transcription request using audio_file
audio_response = client.audio.transcriptions.create(model="whisper-1", file=audio_file)
transcript = audio_response.text

# Create a request to the API to summarize the transcript into bullet points
prompt = "Summarise the transcript into bullet points"
chat_response = client.chat.completions.create(model="gpt-4o-mini", 
messages=[
    {"role": "user", "content":prompt + transcript}]
)
print(chat_response.choices[0].message.content)