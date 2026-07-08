import google.generativeai as genai
from config import GEMINI_API_KEY

genai.configure(api_key=GEMINI_API_KEY)

model = genai.GenerativeModel("gemini-2.5-flash")


def answer_question(question, dataframe):

    data = dataframe.to_markdown(index=False)

    prompt = f"""
You are an AI Project Management Assistant.

Rules:

1. Answer ONLY using the dataset.

2. Never invent information.

3. If multiple rows match, summarize them.

4. Don't print the dataset.

5. Keep answers short.

Dataset:

{data}

Question:

{question}
"""

    response = model.generate_content(prompt)

    return response.text