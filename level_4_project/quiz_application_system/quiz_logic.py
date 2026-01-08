import random
def ask_question(question_dict):
    question = question_dict["question"]
    correct = question_dict["answer"]
    wrongs = question_dict["wrong_answers"]

    options = wrongs + [correct]
    random.shuffle(options)

    print(f"\n{question}")
    for idx, opt in enumerate(options, start=1):
        print(f"{idx}. {opt}")
    while True:
        try:
            choice = int(input("Enter your choice (number): "))
            if 1 <= choice <= len(options):
                return options[choice - 1]
            else:
                print("Invalid option number. Try again.")
        except ValueError:
            print("Invalid input. Please enter a number.")


def check_answer(question_dict, user_choice):
    return user_choice == question_dict["answer"]