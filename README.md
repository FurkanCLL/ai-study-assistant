# AI Study Assistant

This project is being developed for the Applied System Software course. The main idea is to create a Python-based assistant that can help a user work with study notes. The system will take text input or a text file, analyze the content, and return useful results such as a short summary, key concepts, and possible quiz questions.

The project is currently in the planning stage. More implementation details, tests, and deployment instructions will be added step by step during the development process.

## Planned Goal

The goal of this system is to make studying from raw notes easier. Instead of reading long text without structure, the user will be able to give the system some study material and receive a more organized output.

The assistant should be able to:

- read user input or a local text file,
- process the content,
- extract important words or concepts,
- generate a simple summary,
- create basic quiz questions,
- return the result in a clear format.

## Planned System Type

The project will be implemented as a simple command-line Python application. It will use an agent-based structure where the main assistant controls the workflow and calls different tools when needed.

For example, the assistant may call a file reading tool to load study notes, then use a text analysis tool to process the content, and finally use a quiz generation tool to prepare questions.

## Planned Tools

The planned tools are:

1. File Reader Tool  
   Reads study notes from a local `.txt` file.

2. Text Analysis Tool  
   Extracts important words and basic concepts from the input text.

3. Summary Tool  
   Creates a short summary from the provided notes.

4. Quiz Generator Tool  
   Generates simple study questions from the processed text.

5. Export Tool  
   Saves the final result into a text file if the user wants.

## Technologies

The project will use:

- Python
- pytest for testing
- Git and GitHub for version control
- requirements.txt for dependency management

## Current Status

Step 1 is completed as the initial project plan. The next step will be to start implementing the project structure, agent workflow, and basic tools.