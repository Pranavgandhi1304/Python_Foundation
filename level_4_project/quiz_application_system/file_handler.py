import os
def load_questions():
    questions_file = os.path.join(os.path.dirname(__file__), "data", "questions.txt")

    if not os.path.exists(questions_file):
        return []  # File not found → return empty list

    with open(questions_file, "r", encoding="utf-8") as f:
        content = f.read().strip()

    if not content:
        return []  

    blocks = content.split("\n\n")
    questions = []

    for block in blocks:
        lines = block.strip().split("\n")
        if len(lines) == 3:
            question_text = lines[0].strip()
            correct_answer = lines[1].strip()
            wrong_answers = [ans.strip() for ans in lines[2].split(",")]
            questions.append({
                "question": question_text,
                "answer": correct_answer,
                "wrong_answers": wrong_answers
            })

    return questions