from openai import OpenAI
from . import config

# API Token
client = OpenAI(
  api_key=config.API_KEY,
)


def generate_questions(text):

    # Define your prompt for generating questions
    prompt = f"Create a practice test with multiple choice questions on the following text:\n{text}\n\n" \
             f"Each question should be on a different line. Each question should have 4 possible answers. " \
             f"Under the possible answers we should have the correct answer."

    # Generate questions using the ChatGPT API
    response = client.chat.completions.create(
        model="gpt-3.5-turbo",
        messages=[{"role": "user", "content": f"{prompt}"}],
        max_tokens = 3500,
        stop = None,
        temperature = 0.7
    )

    # Extract the generated questions from the API response
    questions = response.choices[0].message.content

    return questions