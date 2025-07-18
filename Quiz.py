def run_quiz():
    questions = [
        {
            "question": "What is the capital of France?",
            "answer": "paris"
        },
        {
            "question": "What is 5 multiplied by 6?",
            "answer": "30"
        },
        {
            "question": "What planet do we live on?",
            "answer": "earth"
        },
        {
            "question": "Who wrote 'Romeo and Juliet'?",
            "answer": "shakespeare"
        },
        {
            "question": "How many days are there in a leap year?",
            "answer": "366"
        },
        {
            "question": "What is the chemical symbol for water?",
            "answer": "h2o"
        },
        {
            "question": "What is the square root of 64?",
            "answer": "8"
        },
    ]

    score = 0

    print("🧠 Welcome to the Quiz Game!")
    print("Answer the following 7 questions:\n")

    for i, q in enumerate(questions):
        user_answer = input(f"Q{i+1}: {q['question']} ").strip().lower()
        if user_answer == q["answer"]:
            print("✅ Correct!\n")
            score += 1
        else:
            print(f"❌ Wrong. The correct answer was: {q['answer']}\n")

    print(f"🏁 Quiz finished! Your score: {score} / 7")

if __name__ == "__main__":
    run_quiz()
