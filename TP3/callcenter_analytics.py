import os
import re
import json
from typing import Dict, Any, List, Tuple
from collections import Counter

EMAIL_RE = re.compile(r"([A-Za-z0-9._%+-]+)@([A-Za-z0-9.-]+)\.([A-Za-z]{2,})")
# Téléphone US simplifié (ex: 555 0199, 555-0199, 5550199). On masque large.
PHONE_RE = re.compile(r"\b(\d[\d\-\s]{5,}\d)\b")

INTENTS = {
    "refund_or_replacement": ["refund", "replacement", "damaged", "cracked", "broken"],
    "delivery_issue": ["delivered", "package", "arrived", "yesterday", "order"],
    "general_support": ["help", "support", "thank you", "calling"],
}

STOPWORDS = set([
    "the","a","an","and","or","to","for","of","in","on","is","it","i","you","we","my","your",
    "was","were","be","as","at","but","this","that","with","about","today"
])

def redact_pii(text: str) -> Tuple[str, Dict[str, int]]:
    stats = {"emails": 0, "phones": 0}

    # TODO: masquer emails
    def _email_sub(m):
        stats["emails"] += 1
        return "[REDACTED_EMAIL]"

    text = EMAIL_RE.sub(_email_sub, text)

    # TODO: masquer téléphones
    def _phone_sub(m):
        stats["phones"] += 1
        return "[REDACTED_PHONE]"

    text = PHONE_RE.sub(_phone_sub, text)
    return text, stats

def normalize(text: str) -> str:
    # minuscule + espaces
    t = text.lower()
    t = re.sub(r"\s+", " ", t).strip()
    return t

def tokenize(text: str) -> List[str]:
    # tokens alphabétiques simples
    toks = re.findall(r"[a-z]+", text.lower())
    return [w for w in toks if w not in STOPWORDS and len(w) > 2]

def score_intents(text: str) -> Dict[str, int]:
    t = normalize(text)
    scores: Dict[str, int] = {}
    for intent, kws in INTENTS.items():
        s = 0
        for kw in kws:
            # TODO: compter occurrences naïvement
            s += t.count(kw)
        scores[intent] = s
    return scores

def pick_intent(scores: Dict[str, int]) -> str:
    # intention avec meilleur score ; fallback si tous à 0
    best_intent = max(scores.items(), key=lambda kv: kv[1])[0]
    if scores[best_intent] == 0:
        return "unknown"
    return best_intent

def main():
    in_path = "TP3/outputs/asr_call_01.json"
    out_path = "TP3/outputs/call_summary_call_01.json"
    os.makedirs("TP3/outputs", exist_ok=True)

    with open(in_path, "r", encoding="utf-8") as f:
        asr = json.load(f)

    full_text = asr["full_text"]
    redacted_text, pii_stats = redact_pii(full_text)

    tokens = tokenize(redacted_text)
    top_terms = Counter(tokens).most_common(10)

    intent_scores = score_intents(redacted_text)
    intent = pick_intent(intent_scores)

    summary = {
        "audio_path": asr["audio_path"],
        "model_id": asr["model_id"],
        "device": asr["device"],
        "audio_duration_s": asr["audio_duration_s"],
        "elapsed_s": asr["elapsed_s"],
        "rtf": asr["rtf"],
        "pii_stats": pii_stats,
        "intent_scores": intent_scores,
        "intent": intent,
        "top_terms": top_terms,
        "redacted_text": redacted_text
    }

    with open(out_path, "w", encoding="utf-8") as f:
        json.dump(summary, f, indent=2)

    print("intent:", intent)
    print("pii_stats:", pii_stats)
    print("top_terms:", top_terms[:5])
    print("saved:", out_path)

if __name__ == "__main__":
    main()