from google import genai
from config import GEMINI_API_KEY

client = genai.Client(api_key=GEMINI_API_KEY)


def evaluate_answer(question, answer):

    prompt = f"""
    You are an expert technical interviewer.

    Question:
    {question}

    Candidate Answer:
    {answer}

    Evaluate the answer and provide:

    1. Score out of 10
    2. Strengths
    3. Weaknesses
    4. Improved Answer

    Be concise and professional.
    """

    try:
        response = client.models.generate_content(
            model="gemini-2.5-flash",
            contents=prompt
        )

        return response.text
    except Exception as e:
        print(f"Gemini Error: {e}")
        return "Unable to evaluate answer right now."