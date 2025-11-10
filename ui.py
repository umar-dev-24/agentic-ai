import streamlit as st
from agents.supervisor_agent import run_supervisor

st.set_page_config(page_title="Agentic Company Analyzer", layout="centered")
st.title("🤖 Agentic AI: Company Analyzer")

company = st.text_input("Enter a query")
if st.button("Search") and company.strip():
    with st.spinner("Agents are working..."):
        try:
            result = run_supervisor(company.strip())
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
