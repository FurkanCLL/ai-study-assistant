from pathlib import Path


def read_text_file(file_path):
    # Reads a local .txt file and returns its content in a small result dictionary.

    input_path = Path(file_path.strip())

    if input_path.suffix.lower() != ".txt":
        return {
            "success": False,
            "text": "",
            "error": "Unsupported file type. Only .txt files are allowed.",
            "error_type": "unsupported_file"
        }

    # First try the path exactly as the user entered it.
    path = input_path

    # If the file is not found from the current working directory,
    # also try the project root folder. This helps when the app is run from src/.
    if not path.exists() and not path.is_absolute():
        project_root = Path(__file__).resolve().parents[1]
        alternative_path = project_root / input_path

        if alternative_path.exists():
            path = alternative_path

    try:
        content = path.read_text(encoding="utf-8")

        return {
            "success": True,
            "text": content,
            "error": None,
            "error_type": None
        }

    except FileNotFoundError:
        return {
            "success": False,
            "text": "",
            "error": "File not found. Please check the file path.",
            "error_type": "file_not_found"
        }

    except OSError:
        return {
            "success": False,
            "text": "",
            "error": "The file could not be opened or read.",
            "error_type": "read_error"
        }