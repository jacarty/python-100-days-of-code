import requests
import base64
from google.auth import default
from google.auth.transport.requests import Request
import pdfplumber

tables = []
images = []

# Extract text from pdf
with pdfplumber.open("python_poem.pdf") as pdf:
    text = "\n".join([page.extract_text() for page in pdf.pages if page.extract_text()])

    for page in pdf.pages:
        tables.extend(page.extract_tables())
        images.extend(page.images)

# Add table summary if tables exist
if tables:
    text += f"\n\nThe document contains {len(tables)} table(s) with data."

# Add image summary if images exist
if images:
    text += f"\n\nThe document contains {len(images)} image(s)."

# Get Google Cloud credentials
credentials, project_id = default()
credentials.refresh(Request())
access_token = credentials.token

# Text-to-Speech API endpoint
tts_url = "https://texttospeech.googleapis.com/v1/text:synthesize"

# Request headers
headers = {
    "Authorization": f"Bearer {access_token}",
    "x-goog-user-project": project_id,
    "Content-Type": "application/json; charset=utf-8"
}

# Request payload
payload = {
    "input": {
        "text": text
    },
    "voice": {
        "languageCode": "en-gb",
        "name": "en-GB-Chirp3-HD-Charon"
    },
    "audioConfig": {
        "audioEncoding": "MP3"
    }
}

try:
    response = requests.post(url=tts_url, headers=headers, json=payload)
    response.raise_for_status()
    
    # The response contains base64-encoded audio
    audio_content = response.json()["audioContent"]
    
    # Decode and save the audio file
    audio_data = base64.b64decode(audio_content)
    
    output_file = "output_speech.mp3"
    with open(output_file, "wb") as out:
        out.write(audio_data)
    
    print(f"Audio saved to {output_file}")
    
except requests.exceptions.RequestException as e:
    print(f"API request failed: {e}")
except KeyError as e:
    print(f"Unexpected response structure: {e}")
