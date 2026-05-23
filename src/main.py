from assistant_agent import AssistantAgent
from export_handler import format_result


def get_user_input():
    """
    Gets direct text or a .txt file path from the user.
    """

    print("AI Study Assistant")
    print("=" * 30)
    print("Enter a .txt file path or paste study text.")
    print("If you paste text, press Enter twice to finish.")
    print("")

    first_line = input("Input: ").strip()

    if first_line.endswith(".txt"):
        return first_line

    lines = [first_line]

    while True:
        line = input()

        if line.strip() == "":
            break

        lines.append(line)

    return "\n".join(lines)


def ask_export_choice():
    """
    Asks whether the user wants to export the result.
    """

    choice = input("Do you want to export the result to a .txt file? (y/n): ").strip().lower()

    if choice == "y":
        filename = input("Enter filename, or press Enter for study_output.txt: ").strip()

        if not filename:
            filename = "study_output.txt"

        return True, filename

    return False, "study_output.txt"


def main():
    """
    Starts the command-line interface.
    """

    agent = AssistantAgent()

    user_input = get_user_input()
    export, filename = ask_export_choice()

    response = agent.process(user_input, export=export, export_filename=filename)

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

    if export and "export" in response:
        print("")
        print(response["export"]["message"])


if __name__ == "__main__":
    main()