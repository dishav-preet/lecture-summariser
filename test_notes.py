from notes_generator import generate_notes

api_key = "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"  # Paste your API key here
transcript = """This is where you paste the transcription from your audio file."""

notes = generate_notes(transcript, api_key)
print("Generated Notes:\n", notes)
