import re


def find_sentence_for_concept(text, concept):
    # Finds the first sentence that mentions the selected concept.
    sentences = re.split(r"(?<=[.!?])\s+", text.strip())

    for sentence in sentences:
        if concept.lower() in sentence.lower():
            return sentence.strip()

    return ""


def generate_quiz(text, key_concepts=None, max_questions=5):
    # Generates simple revision questions from key concepts.
    # This is intentionally basic because the project uses rule-based logic.

    if not text:
        return []

    key_concepts = key_concepts or []

    if not key_concepts:
        return [
            {
                "question": "What is the main topic of the provided study material?",
                "answer": "The answer should be based on the main idea of the text."
            }
        ]

    quiz = []

    for concept in key_concepts[:max_questions]:
        sentence = find_sentence_for_concept(text, concept)

        if sentence:
            answer = sentence
        else:
            answer = f"The concept '{concept}' is mentioned in the study material."

        quiz.append({
            "question": f"What does '{concept}' refer to in the study material?",
            "answer": answer
        })

    return quiz