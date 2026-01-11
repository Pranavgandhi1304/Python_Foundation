import os
def load_questions():
    questions_file = os.path.join(os.path.dirname(__file__), "data", "questions.txt")
    if not os.path.exists(questions_file):
        return []
    with open(questions_file, "r", encoding="utf-8") as f:
        content = f.read().strip()
    if not content:
        return []
    blocks = [b for b in content.split("\n\n") if b.strip()]
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
def save_score(name, score, total):
    scores_file = os.path.join(os.path.dirname(__file__), "data", "scores.txt")
    try:
        with open(scores_file, "a", encoding="utf-8") as f:
            f.write(f"Name: {name} | Score: {score}/{total}\n")
    except Exception:
        pass
def load_scores():
    scores_file = os.path.join(os.path.dirname(__file__), "data", "scores.txt")
    if not os.path.exists(scores_file):
        return []
    with open(scores_file, "r", encoding="utf-8") as f:
        lines = [line.strip() for line in f if line.strip()]
    return lines
