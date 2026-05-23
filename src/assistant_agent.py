from pathlib import Path

from file_reader import read_text_file
from input_validator import validate_input
from text_analyzer import extract_key_concepts
from summary_generator import generate_summary
from quiz_generator import generate_quiz
from export_handler import export_result


class AssistantAgent:
    """
    Main rule-based controller for the AI Study Assistant.
    """

    def __init__(self):
        self.last_result = None

    def detect_input_type(self, user_input):
        """
        Detects whether the user input is a .txt file path or direct text.
        """

        possible_path = Path(user_input.strip())

        if possible_path.suffix.lower() == ".txt":
            return "file"

        return "text"

    def process(self, user_input, export=False, export_filename="study_output.txt"):
        """
        Runs the full study assistant workflow.
        """

        if not user_input or not user_input.strip():
            return {
                "success": False,
                "error": "Input is empty.",
                "result": None
            }

        input_type = self.detect_input_type(user_input)

        if input_type == "file":
            file_result = read_text_file(user_input)

            if not file_result["success"]:
                return {
                    "success": False,
                    "error": file_result["error"],
                    "result": None
                }

            raw_text = file_result["text"]
        else:
            raw_text = user_input

        validation = validate_input(raw_text)

        if validation["status"] == "invalid":
            return {
                "success": False,
                "error": validation["message"],
                "result": None
            }

        warning_message = None

        if validation["status"] == "warning":
            warning_message = validation["message"]

        cleaned_text = validation["text"]

        key_concepts = extract_key_concepts(cleaned_text)
        summary = generate_summary(cleaned_text, key_concepts)
        quiz_questions = generate_quiz(cleaned_text, key_concepts)

        final_result = {
            "summary": summary,
            "key_concepts": key_concepts,
            "quiz_questions": quiz_questions,
            "warning": warning_message
        }

        self.last_result = final_result

        response = {
            "success": True,
            "error": None,
            "result": final_result
        }

        if export:
            response["export"] = export_result(final_result, export_filename)

        return response