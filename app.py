from flask import Flask, request, render_template
import os
from whisper_utils import transcribe_audio
from notes_generator import generate_notes  # ✅ This is the connection
import tempfile

app = Flask(__name__)

# Your OpenRouter API key
API_KEY = "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"  # 🔐 Paste your key here

@app.route("/", methods=["GET", "POST"])
def index():
    transcript = ""
    notes = ""
    if request.method == "POST":
        if "audio_file" not in request.files:
            return "No file uploaded"

        file = request.files["audio_file"]
        if file.filename == "":
            return "No file selected"

        # Save audio temporarily
        with tempfile.NamedTemporaryFile(delete=False, suffix=".mp3") as temp_audio:
            file.save(temp_audio.name)
            temp_path = temp_audio.name

        # Step 1: Transcribe audio
        transcript = transcribe_audio(temp_path)

        # Step 2: Generate notes from transcript
        notes = generate_notes(transcript, API_KEY)

        # Clean up
        os.remove(temp_path)

    return render_template("index.html", transcript=transcript, notes=notes)
if __name__ == '__main__':
    app.run(debug=False, use_reloader=False)


