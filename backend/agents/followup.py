from google import genai
from config import GEMINI_API_KEY

client = genai.Client(api_key=GEMINI_API_KEY)


def generate_followup(question, answer):

    prompt = f"""
    You are an expert technical interviewer.

    Original Question:
    {question}

    Candidate Answer:
    {answer}

    Generate ONE follow-up question based on the candidate's answer.

    Rules:
    - Ask only one question.
    - Make it deeper.
    - Do not evaluate.
    - Do not provide explanations.
    - Sound like a real interviewer.
    """

    response = client.models.generate_content(
        model="gemini-2.0-flash",
        contents=prompt
    )

    return response.text