import requests

def generate_notes(transcript, api_key):
    prompt = f"""
    You are a helpful assistant. A user has uploaded a transcript of an audio file.
    Please extract detailed notes from this transcript, covering all important points without missing anything.

    Transcript:
    {transcript}

    Notes:
    """

    headers = {
        "Authorization": f"Bearer {api_key}",
        "HTTP-Referer": "https://yourdomain.com",  # Put your site if hosted
        "X-Title": "Whisper Notes App"
    }

    response = requests.post("https://openrouter.ai/api/v1/chat/completions", json={
        "model": "mistralai/mixtral-8x7b",
        "messages": [{"role": "user", "content": prompt}],
    }, headers=headers)

    result = response.json()
    return result["choices"][0]["message"]["content"]
