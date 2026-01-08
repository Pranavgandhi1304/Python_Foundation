from file_handler import load_questions
from quiz_logic import ask_question, check_answe
def main():
    questions = load_questions()

    if not questions:
        print("No questions available. Exiting cleanly.")
        return
    score = 0
    
    for q in questions:
        user_choice = ask_question(q)
        if check_answer(q, user_choice):
            print("Correct!\n")
            score += 1
        else:
            print(f"Wrong! Correct answer was: {q['answer']}\n")
if __name__ == "__main__":

    main()
