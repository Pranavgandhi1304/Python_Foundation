from file_handler import load_questions, save_score, load_scores
from quiz_logic import ask_question, check_answer
def run_quiz(name):
    questions = load_questions()
    if not questions:
        print("No questions available. Exiting cleanly.")
        return
    score = 0
    total_questions = len(questions)
    for q in questions:
        user_choice = ask_question(q)

        if user_choice is None:
            print("\nQuiz ended early.")
            break
        if check_answer(q, user_choice):
            print("Correct!\n")
            score += 1
        else:
            print(f"Wrong! Correct answer was: {q['answer']}\n")
    print(f"Quiz completed!\nScore: {score} / {total_questions}")
    save_score(name, score, total_questions)

def view_scores():
    scores = load_scores()
    if not scores:
        print("No previous scores found.")
        return
    print("\nPrevious Scores:")
    for line in scores:
        print(line)
def main():
    while True:
        print("\nQuiz Menu")
        print("1. Start Quiz")
        print("2. View Previous Scores")
        print("3. Exit")
        choice = input("Enter your choice: ").strip()
        if choice == "1":
            name = input("Enter your name: ").strip() or "Anonymous"
            run_quiz(name)
        elif choice == "2":
            view_scores()
        elif choice == "3":
            print("Goodbye!")
            break
        else:
            print("Invalid choice. Please try again.")

if __name__ == "__main__":
    main()
