from pathlib import Path


def format_result(result):
    # Converts the result dictionary into readable text for CLI and export.

    lines = []

    lines.append("AI Study Assistant Output")
    lines.append("=" * 30)
    lines.append("")

    lines.append("Summary:")
    lines.append(result.get("summary", "No summary available."))
    lines.append("")

    lines.append("Key Concepts:")
    key_concepts = result.get("key_concepts", [])

    if key_concepts:
        for concept in key_concepts:
            lines.append(f"- {concept}")
    else:
        lines.append("- No key concepts found.")

    lines.append("")

    lines.append("Quiz Questions:")
    quiz_questions = result.get("quiz_questions", [])

    if quiz_questions:
        for index, item in enumerate(quiz_questions, start=1):
            lines.append(f"{index}. {item.get('question', '')}")
            lines.append(f"   Answer: {item.get('answer', '')}")
    else:
        lines.append("No quiz questions generated.")

    return "\n".join(lines)


def export_result(result, filename="study_output.txt"):
    # Saves the final study output into a local .txt file.

    try:
        path = Path(filename)

        if path.suffix.lower() != ".txt":
            path = path.with_suffix(".txt")

        output_text = format_result(result)
        path.write_text(output_text, encoding="utf-8")

        return {
            "success": True,
            "message": f"Result exported successfully to {path}"
        }

    except OSError:
        return {
            "success": False,
            "message": "Export failed because the file could not be written."
        }