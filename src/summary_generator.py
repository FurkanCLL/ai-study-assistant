import re
from collections import Counter


def split_sentences(text):
    """
    Splits text into simple sentences.
    """

    sentences = re.split(r"(?<=[.!?])\s+", text.strip())
    return [sentence.strip() for sentence in sentences if sentence.strip()]


def generate_summary(text, key_concepts=None, max_sentences=3):
    """
    Generates a short rule-based summary from study material.
    """

    if not text:
        return "No summary could be generated because the text is empty."

    sentences = split_sentences(text)

    if len(sentences) <= max_sentences:
        return " ".join(sentences)

    key_concepts = key_concepts or []
    lower_concepts = [concept.lower() for concept in key_concepts]

    word_counter = Counter(re.findall(r"\b[a-zA-Z]{4,}\b", text.lower()))
    scored_sentences = []

    for index, sentence in enumerate(sentences):
        sentence_lower = sentence.lower()
        score = 0

        for concept in lower_concepts:
            if concept in sentence_lower:
                score += 3

        for word in re.findall(r"\b[a-zA-Z]{4,}\b", sentence_lower):
            score += word_counter[word]

        scored_sentences.append((score, index, sentence))

    selected_sentences = sorted(scored_sentences, reverse=True)[:max_sentences]
    selected_sentences = sorted(selected_sentences, key=lambda item: item[1])

    return " ".join(sentence for score, index, sentence in selected_sentences)