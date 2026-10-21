import streamlit as st
import os
from openai import OpenAI
from dotenv import load_dotenv

load_dotenv()

client = OpenAI(
    api_key=os.getenv("GROQ_API_KEY"),
    base_url="https://api.groq.com/openai/v1",
)

MODEL = "openai/gpt-oss-20b"


def call_llm(system_prompt, user_prompt):
    response = client.chat.completions.create(
        model=MODEL,
        messages=[
            {"role": "system", "content": system_prompt},
            {"role": "user", "content": user_prompt},
        ],
        temperature=0.3,
    )
    return response.choices[0].message.content


def zero_shot(question):
    return call_llm("You are a helpful assistant.", question)


def few_shot(question):
    system = """You are a helpful assistant. Answer in a short, direct way.

Examples:
Q: Capital of France?
A: Paris.
Q: What is 5 + 3?
A: 8.
Q: Boiling point of water?
A: 100°C.
"""
    return call_llm(system, f"Q: {question}\nA:")


def chain_of_thought(question):
    return call_llm(
        "You are a logical assistant. Think step-by-step and show your reasoning.",
        question
    )


def role_based(question):
    return call_llm(
        "You are a senior software engineer with 10 years of experience. Explain clearly with examples.",
        question
    )


st.title("🧠 Prompt Engineering Playground")
st.markdown("Compare **4 tareeqe** ek hi sawal par.")

question = st.text_area(
    "Apna sawal likho:",
    placeholder="e.g., REST API kya hai?",
    height=100
)

if st.button("Compare Prompts") and question.strip():
    col1, col2 = st.columns(2)

    with st.spinner("Zero-shot chal raha hai..."):
        zs = zero_shot(question)
    with st.spinner("Few-shot chal raha hai..."):
        fs = few_shot(question)
    with st.spinner("Chain-of-Thought chal raha hai..."):
        cot = chain_of_thought(question)
    with st.spinner("Role-based chal raha hai..."):
        rb = role_based(question)

    with col1:
        st.subheader("1️⃣ Zero-shot")
        st.write(zs)
        st.subheader("2️⃣ Few-shot")
        st.write(fs)

    with col2:
        st.subheader("3️⃣ Chain-of-Thought")
        st.write(cot)
        st.subheader("4️⃣ Role-based")
        st.write(rb)

    st.markdown("---")
    st.caption("Built by [Waseem Saleem]")
