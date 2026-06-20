from google import genai
from config import GEMINI_API_KEY

client = genai.Client(api_key=GEMINI_API_KEY)

def generate_question(domain):

    prompt = f"""
    You are an expert interviewer.

    Conduct a {domain} interview.

    Ask only ONE interview question.

    Do not provide explanation.
    Do not provide answer.
    """

    response = client.models.generate_content(
        model="gemini-2.5-flash",
        contents=prompt
    )

    return response.text