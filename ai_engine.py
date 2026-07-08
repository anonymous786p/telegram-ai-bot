import google.generativeai as genai
import pandas as pd

from config import GEMINI_API_KEY

genai.configure(api_key=GEMINI_API_KEY)

model = genai.GenerativeModel("gemini-2.5-flash")


def dataframe_to_text(df):

    if len(df) == 0:
        return "I could not find that information."

    answer = ""

    for _, row in df.iterrows():

        answer += "\n"

        for col in df.columns:
            answer += f"{col}: {row[col]}\n"

        answer += "-" * 30 + "\n"

    return answer


def answer_question(question, dataframe):

    prompt = f"""
You are an AI Project Management Assistant.

Answer ONLY using the dataset below.

If the answer is unavailable, reply:

"I could not find that information."

Dataset:

{dataframe.to_string(index=False)}

Question:

{question}
"""

    try:

        response = model.generate_content(prompt)

        return response.text

    except Exception as e:

        print("Gemini Error:", e)

        return (
            "⚠️ AI service is temporarily unavailable.\n\n"
            "Showing data directly from the dataset:\n\n"
            + dataframe_to_text(dataframe)
        )