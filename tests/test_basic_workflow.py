import sys
from pathlib import Path

PROJECT_ROOT = Path(__file__).resolve().parents[1]
SRC_PATH = PROJECT_ROOT / "src"
sys.path.insert(0, str(SRC_PATH))

from assistant_agent import AssistantAgent
from input_validator import validate_input
from text_analyzer import extract_key_concepts
from summary_generator import generate_summary
from quiz_generator import generate_quiz
from file_reader import read_text_file
from export_handler import export_result


def test_validate_empty_input():
    result = validate_input("")

    assert result["status"] == "invalid"
    assert result["reason"] == "empty_text"


def test_validate_short_input():
    result = validate_input("Short text.")

    assert result["status"] == "warning"
    assert result["reason"] == "too_short"


def test_extract_key_concepts():
    text = (
        "Software testing improves software quality. "
        "Testing helps developers find errors. "
        "Software quality depends on testing and validation."
    )

    concepts = extract_key_concepts(text)

    assert isinstance(concepts, list)
    assert "testing" in concepts


def test_generate_summary():
    text = (
        "Software testing is important for quality. "
        "Testing helps find errors before release. "
        "Validation checks whether the system meets requirements. "
        "Good testing improves reliability."
    )

    summary = generate_summary(text, ["testing", "quality"], max_sentences=2)

    assert isinstance(summary, str)
    assert len(summary) > 0


def test_generate_quiz():
    text = (
        "Software testing is used to find errors. "
        "Validation checks whether the system meets requirements."
    )

    quiz = generate_quiz(text, ["testing", "validation"])

    assert isinstance(quiz, list)
    assert len(quiz) > 0
    assert "question" in quiz[0]
    assert "answer" in quiz[0]


def test_agent_process_direct_text():
    text = (
        "Software engineering is the process of designing, developing, testing, "
        "and maintaining software systems. Testing improves software quality and "
        "helps developers find errors before deployment. Requirements define what "
        "the system should do and guide the development process."
    )

    agent = AssistantAgent()
    response = agent.process(text)

    assert response["success"] is True
    assert response["result"] is not None
    assert "summary" in response["result"]
    assert "key_concepts" in response["result"]
    assert "quiz_questions" in response["result"]


def test_agent_process_short_text_with_warning():
    agent = AssistantAgent()
    response = agent.process("Testing is useful.")

    assert response["success"] is True
    assert response["result"]["warning"] is not None


def test_file_reader_success(tmp_path):
    file_path = tmp_path / "notes.txt"
    file_path.write_text("This is a test note about software testing.", encoding="utf-8")

    result = read_text_file(str(file_path))

    assert result["success"] is True
    assert "software testing" in result["text"]


def test_file_reader_not_found():
    result = read_text_file("missing_file.txt")

    assert result["success"] is False
    assert result["error_type"] == "file_not_found"


def test_file_reader_rejects_wrong_file_type():
    result = read_text_file("notes.pdf")

    assert result["success"] is False
    assert result["error_type"] == "unsupported_file"


def test_export_result(tmp_path):
    output_file = tmp_path / "study_output.txt"

    result_data = {
        "summary": "This is a summary.",
        "key_concepts": ["testing", "software"],
        "quiz_questions": [
            {
                "question": "What is testing?",
                "answer": "Testing is used to find errors."
            }
        ]
    }

    result = export_result(result_data, str(output_file))

    assert result["success"] is True
    assert output_file.exists()