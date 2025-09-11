import streamlit as st
from agents.grammar.grammar_checker import check_and_correct as grammar_agent
from agents.data.data_summary import summarize_csv as data_agent
from general_agent import general_agent
import logging

# Set up logging
logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)

st.set_page_config(page_title="CodeLingoo — Mini Agent", layout="wide")
st.title("CodeLingoo — Mini Agent (Grammar, Data & Q&A)")

tab1, tab2, tab3 = st.tabs(["Grammar Helper", "Data Analyzer", "Q&A Agent"])

with tab1:
    st.header("Grammar Helper")
    logger.info("Rendering Grammar Helper tab")
    text_input = st.text_area("Enter text to check grammar:", "I has two cat.")
    if st.button("Check Grammar"):
        logger.info(f"Checking grammar for: {text_input}")
        try:
            corrected_text, issues = grammar_agent(text_input)
            st.write("**Corrected Text**:")
            st.write(corrected_text)
            st.write("**Issues Found**:")
            for issue in issues:
                st.write(f"- {issue}")
        except Exception as e:
            logger.error(f"Grammar check failed: {str(e)}")
            st.error(f"Grammar check failed: {str(e)}")

with tab2:
    st.header("Data Analyzer")
    logger.info("Rendering Data Analyzer tab")
    uploaded_file = st.file_uploader("Upload a CSV file", type=["csv"])
    if uploaded_file:
        logger.info(f"Processing uploaded file: {uploaded_file.name}")
        try:
            summary, fig = data_agent(uploaded_file)
            st.write("**Summary**:")
            st.write(summary)
            st.pyplot(fig)
        except Exception as e:
            logger.error(f"Data analysis failed: {str(e)}")
            st.error(f"Data analysis failed: {str(e)}")

with tab3:
    st.header("Q&A Agent")
    logger.info("Rendering Q&A Agent tab")
    question = st.text_input("Ask a question:", "Who is Ada Lovelace?")
    context = st.text_area("Optional context:", "Ada Lovelace was a mathematician...")
    if st.button("Get Answer (Q&A Agent)"):
        logger.info(f"Processing Q&A: question={question}, context={context}")
        try:
            answer = general_agent(question, context)
            st.write(f"**Answer**: {answer}")
        except Exception as e:
            logger.error(f"Q&A failed: {str(e)}")
            st.error(f"Q&A failed: {str(e)}")