from google import genai
from config import GEMINI_API_KEY

client = genai.Client(api_key=GEMINI_API_KEY)


def generate_question(domain, history):

    history_text = ""

    for item in history:

        history_text += f"""
        Previous Question:
        {item['question']}

        Candidate Answer:
        {item['answer']}
        """

    prompt = f"""
    You are an expert interviewer.

    Interview Domain:
    {domain}

    Previous Interview History:
    {history_text}

    Rules:
    1. Do NOT repeat previous questions.
    2. Increase difficulty gradually.
    3. Ask only ONE question.
    4. Keep it interview style.
    5. Focus on technical depth.

    Generate the next interview question.
    """

    response = client.models.generate_content(
        model="gemini-2.0-flash",
        contents=prompt
    )

    return response.text