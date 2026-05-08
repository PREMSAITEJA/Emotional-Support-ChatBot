import spacy
from config import SPACY_MODEL, CRISIS_INDICATORS

def _load_nlp():
    try:
        return spacy.load(SPACY_MODEL)
    except OSError:
        return spacy.blank("en")

nlp = _load_nlp()

def detect_crisis(user_message: str) -> bool:
    doc = nlp(user_message.lower())
    return any(indicator in doc.text for indicator in CRISIS_INDICATORS)

def get_crisis_response() -> str:
    return "I'm really concerned about what you're saying. Please reach out to a crisis helpline immediately. In the US, you can call 1800-599-0019 or text HOME to 988 ."
