
import streamlit as st
import re

st.title("🛡️ Simple Guardrail Chat")

blocked_words = ["kill", "bomb", "steal"]

def is_blocked(prompt):
    pattern = r"\b(" + "|".join(re.escape(w) for w in blocked_words) + r")\b"
    return re.search(pattern, prompt.lower()) is not None

prompt = st.text_input("Enter your prompt:")
if prompt:
    if is_blocked(prompt):
        st.error("❌ Prompt blocked by guardrail!")
    else:
        st.success("✅ Prompt passed! (This is where LLM response would go)")
