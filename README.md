# AI Study Assistant

AI Study Assistant is a simple Python command line project created for a software development coursework task. The system helps students turn plain-text study notes into structured revision material.

The project is designed mainly for first-year and second-year computer science or software engineering students. It can read direct text input or a local `.txt` file, then generate:

- a short summary
- a list of key concepts
- simple quiz questions with short answers

The first version does not use an external AI API. It uses a rule-based assistant agent and internal Python tools.

## Project Goal

The main goal of this project is to help students revise lecture notes more easily. Long notes can be difficult to review before an exam, so this tool tries to convert raw study material into a cleaner and more useful revision format.

The system is not meant to replace a teacher or a full AI tutor. It is a small study support tool that demonstrates an agent-based workflow, tool usage, input/output handling, testing, and basic deployment preparation.

## Main Features

- Accepts direct text input from the command line
- Accepts local `.txt` files as input
- Validates empty and short text input
- Extracts key concepts from study notes
- Generates a short rule-based summary
- Generates simple quiz questions and answers
- Can export the final result into a `.txt` file
- Includes basic automated tests with `pytest`

## Project Structure

```text
ai-study-assistant/
│
├── src/
│   ├── __init__.py
│   ├── main.py
│   ├── cli_interface.py
│   ├── assistant_agent.py
│   ├── file_reader.py
│   ├── input_validator.py
│   ├── text_analyzer.py
│   ├── summary_generator.py
│   ├── quiz_generator.py
│   └── export_handler.py
│
├── tests/
│   └── test_basic_workflow.py
│
├── .gitignore
├── README.md
├── report.md
└── requirements.txt
```

## How the System Works

The project uses a simple rule-based assistant agent. The agent controls the workflow and decides which internal tool should be used at each step.

The basic workflow is:

1. The user enters direct study text or a `.txt` file path.
2. The assistant agent checks the input type.
3. If the input is a file path, the file reader tool reads the file.
4. The input validator checks whether the text is empty, too short, or valid.
5. If the text is valid, the text analyzer extracts key concepts.
6. The summary generator creates a short summary.
7. The quiz generator creates simple revision questions.
8. The final output is shown in the command line.
9. If the user chooses export, the result is saved as a `.txt` file.

## Internal Tools

| Tool | Purpose |
|---|---|
| File Reader | Reads local `.txt` files |
| Input Validator | Checks empty or short input |
| Text Analyzer | Extracts repeated important terms |
| Summary Generator | Creates a short rule-based summary |
| Quiz Generator | Creates simple study questions |
| Export Handler | Saves the final result into a `.txt` file |

## Technologies Used

- Python 3
- Standard Python libraries:
  - `pathlib`
  - `re`
  - `string`
  - `collections.Counter`
- `pytest` for testing
- Git and GitHub for version control

## Installation

Clone the repository:

```bash
git clone https://github.com/FurkanCLL/ai-study-assistant.git
cd ai-study-assistant
```

Create a virtual environment:

```bash
python -m venv .venv
```

Activate the virtual environment.

On Windows:

```bash
.venv\Scripts\activate
```

On macOS/Linux:

```bash
source .venv/bin/activate
```

Install the requirements:

```bash
pip install -r requirements.txt
```

## Running the Program

Run the program from the project root:

```bash
python src/main.py
```

After running the program, you can either paste study text directly or enter a path to a local `.txt` file.

Example direct text input:

```text
Software testing is important because it helps developers find errors before release. Testing improves software quality and reliability. Requirements define what the system should do.
```

Example file input:

```text
notes.txt
```

## Example Output

The program generates an output with three main sections:

```text
AI Study Assistant Output
==============================

Summary:
Software testing is important because it helps developers find errors before release.

Key Concepts:
- testing
- software
- quality
- requirements

Quiz Questions:
1. What does 'testing' refer to in the study material?
   Answer: Software testing is important because it helps developers find errors before release.
```

## Running Tests

The project includes automated tests for the main functionality.

Run tests with:

```bash
pytest
```

The tests check:

- empty input validation
- short input warnings
- key concept extraction
- summary generation
- quiz generation
- direct text workflow
- file reading
- unsupported file type handling
- export functionality

## Deployment Preparation

This project is prepared as a local command-line application. It does not require cloud hosting, API keys, or external services.

A user can run the system by:

1. Cloning the repository
2. Creating a virtual environment
3. Installing dependencies from `requirements.txt`
4. Running `python src/main.py`

This makes the project simple to test and use in a controlled local environment.

## Data Processing

The system receives either direct text or text from a `.txt` file.

The data flow is:

```text
Raw input
→ cleaned text
→ validation result
→ key concepts
→ summary
→ quiz questions
→ formatted output
```

The input validator cleans extra whitespace. The text analyzer converts the cleaned text into a list of key concepts. The summary and quiz tools then use the cleaned text and key concept list to create the final study output.

## Limitations

This project uses rule-based text processing, so the output quality depends on the structure and clarity of the input notes.

Some limitations are:

- summaries may be simple
- quiz questions may not always be deep
- key concepts are based mostly on repeated words
- complex academic texts may need better NLP methods
- the first version only supports plain `.txt` files

These limitations are acceptable for the first version because the main goal is to demonstrate a working agent-based Python system with internal tools.

## Future Improvements

Possible future improvements include:

- better natural language processing
- support for PDF files
- improved quiz question templates
- difficulty levels for quiz questions
- a simple graphical interface
- optional external AI API integration
- saving previous study sessions

## Conclusion

AI Study Assistant is a small but functional Python project. It demonstrates a modular command-line application with an assistant agent, internal tools, input/output handling, testing, and deployment preparation.

The project is intentionally simple, but it satisfies the main goal of transforming study notes into useful revision material.

## Author 

#### Furkan Ciloglu
#### 231ADB104