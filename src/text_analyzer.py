import re
import string
from collections import Counter


STOP_WORDS = {
    "the", "and", "or", "but", "if", "then", "this", "that", "these", "those",
    "is", "are", "was", "were", "be", "been", "being", "to", "of", "in", "on",
    "for", "with", "as", "by", "at", "from", "it", "its", "an", "a", "also",
    "can", "will", "should", "would", "could", "may", "might", "not", "into",
    "their", "there", "which", "when", "where", "how", "what", "why", "about",
    "using", "used", "use", "such", "than", "more", "less", "very"
}


def extract_key_concepts(text, max_concepts=10):
    """
    Extracts important repeated terms from study notes.
    """

    if not text:
        return []

    lowered_text = text.lower()
    cleaned_text = lowered_text.translate(str.maketrans("", "", string.punctuation))
    words = re.findall(r"\b[a-zA-Z]{4,}\b", cleaned_text)

    filtered_words = [
        word for word in words
        if word not in STOP_WORDS
    ]

    word_counts = Counter(filtered_words)
    most_common_words = word_counts.most_common(max_concepts)

    return [word for word, count in most_common_words]