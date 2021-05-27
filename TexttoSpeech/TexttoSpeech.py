import os
from google.cloud import texttospeech

os.environ['GOOGLE_APPLICATION_CREDENTIALS'] = 'C:/Users/Steve/Desktop/Voice and Text/Key API/palesaapi-8d6d5119f293.json'

# Instantiates a client
client = texttospeech.TextToSpeechClient()

# My text that will be converted to speech
text =  "I am Steve Ralephenya from Soshanguve, but the robot is saying this..."


# Set the text input to be synthesized
synthesis_input = texttospeech.SynthesisInput(text=text)

# Build the voice request, select the language code ("en-US") and the ssml
# voice gender ("neutral")
voice = texttospeech.VoiceSelectionParams(
    language_code="en-US", ssml_gender=texttospeech.SsmlVoiceGender.NEUTRAL
)

# Select the type of audio file you want returned
audio_config = texttospeech.AudioConfig(
    audio_encoding=texttospeech.AudioEncoding.MP3
)

# Perform the text-to-speech request on the text input with the selected
# voice parameters and audio file type
response = client.synthesize_speech(
    input=synthesis_input, voice=voice, audio_config=audio_config
)

# The response's audio_content is binary.
with open("output.mp3", "wb") as out:
    # Write the response to the output file.
    out.write(response.audio_content)
    print('Audio content written to file "output.mp3"')
