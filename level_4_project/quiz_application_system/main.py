from file_handler import load_questions

def main():
    questions = load_questions()

    if not questions:
        print("No questions available. Exiting cleanly.")
        return

    print("Loaded Questions:\n")
    for idx, q in enumerate(questions, start=1):
        print(f"Q{idx}: {q['question']}")
        print(f"   Correct Answer: {q['answer']}")
        print(f"   Wrong Answers: {', '.join(q['wrong_answers'])}")
        print()

if __name__ == "__main__":
    main()