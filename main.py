import json
from difflib import get_close_matches
from chatbot import main_menu

def load_knowledge_base(file_path: str) -> dict:
    try:
        with open(file_path) as file:
            data = json.load(file)
            return data
    except FileNotFoundError:
        return {"questions": []}
    except json.JSONDecodeError:
        return {"questions": []}

def save_knowledge_base(file_path: str, data: dict):
    with open(file_path, 'w') as file:
        json.dump(data, file, indent=2)

def find_best_match(user_question: str, questions: list[str]) -> str | None:
    matches = get_close_matches(user_question, questions, n=1, cutoff=0.6)
    return matches[0] if matches else None

def get_answer_for_question(question: str, knowledge_base: dict) -> str | None:
    for q in knowledge_base["questions"]:
        if q["question"] == question:
            return q["answer"]

def chatbot():
    knowledge_base: dict = load_knowledge_base("knowledge_base.json")
    while True:
        user_input = input("You: ")
        if user_input.lower() == "quit":
            break
        best_match: str | None = find_best_match(user_input, [q["question"] for q in knowledge_base["questions"]])
        if best_match:
            answer: str | None = get_answer_for_question(best_match, knowledge_base)
            if answer:
                print(f'Nova: {answer}')
            else:
                print("Nova: I don't have an answer for that question. But I know the question.")

        elif user_input.lower() == "solve math":
                print("ok here is the main menu",main_menu())


        else:
            print("Nova: I don't have an answer for that question. Can you teach me?")
            new_answer: str = input('Type the answer or type "skip" to skip: ')
            if new_answer.lower() == "skip":
                print('Okay, I will skip this question.')
            else:
                knowledge_base["questions"].append({"question": user_input, "answer": new_answer})
                save_knowledge_base("knowledge_base.json", knowledge_base)
                print("Nova: Thank you for teaching me! I am excited to use it next time!")

if __name__ == "__main__":
    chatbot()
