from assistant_agent import AssistantAgent
from export_handler import format_result


def get_user_input():
    # Gets either a .txt file path or direct pasted study text.
    print("AI Study Assistant")
    print("=" * 30)
    print("You can enter a .txt file path or paste study text directly.")
    print("If you paste text, press Enter twice to finish.")
    print("")

    first_line = input("Input: ").strip()

    # If it looks like a text file path, we return it directly.
    if first_line.lower().endswith(".txt"):
        return first_line

    lines = [first_line]

    while True:
        line = input()

        if line.strip() == "":
            break

        lines.append(line)

    return "\n".join(lines)


def ask_export_choice():
    # Asks the user if they want to save the result into a text file.
    choice = input("\nDo you want to export the result to a .txt file? (y/n): ").strip().lower()

    if choice == "y":
        filename = input("Enter filename, or press Enter for study_output.txt: ").strip()

        if not filename:
            filename = "study_output.txt"

        return True, filename

    return False, "study_output.txt"


def print_response(response):
    # Prints either an error or the final formatted study result.
    print("")
    print("=" * 30)

    if not response["success"]:
        print("Error:")
        print(response["error"])
        return

    result = response["result"]

    if result.get("warning"):
        print("Warning:")
        print(result["warning"])
        print("")

    print(format_result(result))

    if response.get("export"):
        print("")
        print(response["export"]["message"])


def main():
    # Runs the full command-line program.
    agent = AssistantAgent()

    user_input = get_user_input()
    export, filename = ask_export_choice()

    response = agent.process(
        user_input=user_input,
        export=export,
        export_filename=filename
    )

    print_response(response)