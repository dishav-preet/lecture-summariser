# transcriber.py
import whisper
import warnings

warnings.filterwarnings("ignore", message="FP16 is not supported on CPU")
model = whisper.load_model("medium")

def transcribe_audio(filepath):
    result = model.transcribe(filepath , verbose=False)
    text = " ".join([segment['text'] for segment in result['segments']])
    return text
