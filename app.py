#hii this is testinggg
#hi

def make_quiz(notes):
    lines = [line.strip() for line in notes.split("\n") if line.strip()]
    questions = []

    for i, line in enumerate(lines, start=1):
        questions.append(f"Q{i}. What is the main idea of this point?\n   {line}")

    return questions

def main():
    try:
        with open("notes.txt", "r", encoding="utf-8") as file:
            notes = file.read()
    except FileNotFoundError:
        print("notes.txt not found. Create it in the same folder as app.py.")
        return

    print("Study Buddy — Quiz Questions\n")
    for question in make_quiz(notes):
        print(question)
        print()

if __name__ == "__main__":
    main()