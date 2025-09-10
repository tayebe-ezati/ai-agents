import streamlit as st
from grammar_checker import grammar_agent
from data_summary import data_agent
from general_agent import general_agent

st.set_page_config(page_title="CodeLingoo — Mini Agent", layout="wide")

st.title("CodeLingoo — Mini Agent (Grammar, Data & Q&A)")

# Sidebar info
st.sidebar.header("About")
st.sidebar.info(
    "🚀 A simple AI agent app with three tools:\n\n"
    "- ✏️ Grammar Helper\n"
    "- 📊 Data Analyzer\n"
    "- ❓ Q&A Agent"
)

# Tabs
tab1, tab2, tab3 = st.tabs(["Grammar Helper", "Data Analyzer", "Q&A Agent"])

# Tab 1: Grammar Helper
with tab1:
    st.subheader("Grammar Helper")
    text_input = st.text_area("Enter text to check grammar:")
    if st.button("Check Grammar", key="grammar"):
        if text_input.strip():
            result = grammar_agent(text_input)
            st.write("### ✅ Corrected Text:")
            st.success(result)
        else:
            st.warning("Please enter some text!")

# Tab 2: Data Analyzer
with tab2:
    st.subheader("Data Analyzer")
    uploaded_file = st.file_uploader("Upload a CSV file", type=["csv"])
    if uploaded_file is not None:
        result = data_agent(uploaded_file)
        st.write("### 📊 Data Summary:")
        st.write(result)

# Tab 3: Q&A Agent
with tab3:
    st.subheader("Q&A Agent")
    question = st.text_input("Ask a question (e.g. 'Who is Ada Lovelace?')")
    if st.button("Ask", key="qa"):
        if question.strip():
            answer = general_agent(question)
            st.write("### 🤖 Answer:")
            st.info(answer)
        else:
            st.warning("Please enter a question!")
