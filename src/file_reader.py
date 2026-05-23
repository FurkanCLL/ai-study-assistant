from pathlib import Path


def read_text_file(file_path):
    """
    Reads a local .txt file and returns its content.
    """

    path = Path(file_path.strip())

    if path.suffix.lower() != ".txt":
        return {
            "success": False,
            "text": "",
            "error": "Unsupported file type. Only .txt files are allowed.",
            "error_type": "unsupported_file"
        }

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