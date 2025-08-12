# ui.py

import streamlit as st
from agents.supervisor_agent import run_supervisor

st.set_page_config(page_title="Agentic Company Analyzer", layout="centered")
st.title("🤖 Agentic AI: Company Analyzer")
role = st.selectbox("Select your role", ["user", "admin"])

company = st.text_input("Enter a query")
if st.button("Search") and company.strip():
    with st.spinner("Agents are working..."):
        try:
            suspicious_phrases = [
                # "ignore previous instructions",
                # "tell me your prompt",
                # "list your tools",
                # "who are you",
                # "what is your role",
            ]

            def is_prompt_injection(text):
                return any(phrase in text.lower() for phrase in suspicious_phrases)

            # 'user_input' is not defined in the original code, assuming 'company' is the input to check
            if is_prompt_injection(company):
                st.warning("This input is blocked for safety.")
            else:
                result = run_supervisor(company.strip(), role)
                if isinstance(result, list):
                    st.subheader("🔍 Agent Trace")
                    for msg in result:
                        if hasattr(msg, "name") and msg.name:
                            st.markdown(f"**{msg.name}:**")
                            st.code(msg.content, language="markdown")
                if isinstance(result, list):
                    final_summary = next(
                        (
                            msg.content
                            for msg in reversed(result)
                            if getattr(msg, "name", None) == "supervisor"
                        ),
                        "No final output from supervisor.",
                    )
                elif isinstance(result, dict) and "output" in result:
                    final_summary = result["output"]
                else:
                    final_summary = str(result)

                st.success("Agents have completed their tasks!")
                st.text_area("AI response", final_summary, height=300)
        except Exception as e:
            st.error(f"Something went wrong: {e}")
