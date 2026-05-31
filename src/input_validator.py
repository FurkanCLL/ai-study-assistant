def validate_input(text, min_length=100):
    # Checks whether the study material is usable.
    # It also cleans extra spaces so other tools get a cleaner text.

    if text is None:
        return {
            "status": "invalid",
            "reason": "empty_text",
            "text": "",
            "message": "No input was provided."
        }

    cleaned_text = " ".join(text.strip().split())

    if not cleaned_text:
        return {
            "status": "invalid",
            "reason": "empty_text",
            "text": "",
            "message": "The provided text is empty."
        }

    if len(cleaned_text) < min_length:
        return {
            "status": "warning",
            "reason": "too_short",
            "text": cleaned_text,
            "message": "The text is quite short, so summary and quiz quality may be limited."
        }

    return {
        "status": "valid",
        "reason": "ok",
        "text": cleaned_text,
        "message": "Input is valid."
    }