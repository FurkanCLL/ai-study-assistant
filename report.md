# Project Report and Development Journal

## Project Title

AI Study Assistant

## Step 1 – Initial Project Plan

### 1. Short Description of the Planned System and Its Goal

The planned system is a Python-based AI study assistant. The purpose of the system is to help users work with study notes in a more organized way.

The user will be able to enter text manually or provide a local text file. The system will process the input and return useful study material, such as a short summary, important concepts, and possible quiz questions.

The main goal of this project is not to build a very large application, but to create a clear and working software system that shows implementation, tool usage, testing, version control, and deployment preparation.

### 2. AI or Agent-Based Approach

The system will use a simple agent-based approach. There will be one main assistant agent that controls the workflow.

The assistant agent will:

1. receive input from the user,
2. check what kind of input was provided,
3. call the required tools,
4. process the returned data,
5. prepare the final output for the user.

The agent itself will not do everything directly. Instead, it will use separate tools for specific tasks. This makes the system easier to understand, test, and improve later.

For example, if the user gives a file path, the assistant will use a file reader tool. After that, it can use a text analysis tool, a summary tool, and a quiz generator tool.

### 3. Planned Tools Used in the System

The system will use several tools during execution.

#### File Reader Tool

This tool will read text from a local `.txt` file. It will be used when the user wants to analyze study notes stored in a file.

#### Text Analysis Tool

This tool will process the text and extract important words or concepts. It may use simple text processing methods such as removing punctuation, splitting words, counting word frequency, and ignoring very common words.

#### Summary Tool

This tool will create a short summary from the input text. In the first version, the summary can be based on simple rules, such as selecting the most relevant sentences.

#### Quiz Generator Tool

This tool will generate basic quiz questions from the processed content. The questions will be simple, but they will help demonstrate how the assistant can transform input data into study material.

#### Export Tool

This tool will save the final result into a local output file. This is useful if the user wants to keep the generated summary or quiz questions.

### 4. Preliminary List of Programming Concepts

The project will require several programming concepts.

#### Functions

Functions will be used to divide the system into smaller parts. Each tool will have its own function or group of functions.

#### Classes

Classes may be used for the assistant agent and for organizing the main workflow. This will make the project structure cleaner.

#### Modules

The source code will be divided into separate modules. For example, the agent logic and tool logic will be placed in different files.

#### File Handling

The system will read input from text files and may also write results into output files.

#### Lists and Dictionaries

Lists and dictionaries will be used to store words, sentences, extracted concepts, generated questions, and final results.

#### Input Validation

The system will check user input before processing it. For example, it should handle empty input or missing files.

#### Exception Handling

Exception handling will be used to manage errors such as invalid file paths or unreadable files.

#### Testing

The project will include tests for the main workflow and tools. pytest will probably be used for this.

#### Version Control

Git and GitHub will be used to track the development process. Commits will show how the project changes during each stage.

### 5. Current Project Status

At this stage, the project idea has been selected and the initial structure has been created. The repository contains the basic folders for source code, tests, documentation, and dependency management.

The next step will be to implement the first working version of the assistant and connect the basic tools to the main workflow.