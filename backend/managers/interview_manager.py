from agents.interviewer import generate_question
from agents.evaluator import evaluate_answer
from agents.followup import generate_followup

def conduct_interview(domain):

    for i in range(3):

        print(f"\n----- Question {i+1} -----")

        # Main Question
        question = generate_question(domain)

        print("\nMain Question:")
        print(question)

        answer = input("\nYour Answer: ")

        feedback = evaluate_answer(question, answer)

        print("\nEvaluation:")
        print(feedback)

        # Follow-up Question
        followup_question = generate_followup(
            question,
            answer
        )

        print("\nFollow-Up Question:")
        print(followup_question)

        followup_answer = input("\nYour Answer: ")

        followup_feedback = evaluate_answer(
            followup_question,
            followup_answer
        )

        print("\nFollow-Up Evaluation:")
        print(followup_feedback)