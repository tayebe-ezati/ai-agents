import streamlit as st
from agents.grammar.grammar_checker import check_and_correct as grammar_agent
from agents.data.data_summary import summarize_csv as data_agent
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
            try:
                corrected, issues = grammar_agent(text_input)
                st.write("### ✅ Corrected Text:")
                st.success(corrected)
                if issues:
                    st.write("### ⚠️ Grammar Issues:")
                    for issue in issues:
                        st.write(f"- {issue['message']}: Suggestions: {', '.join(issue['suggestions']) or 'None'}")
                else:
                    st.info("No grammar issues found!")
            except Exception as e:
                st.error(f"Error checking grammar: {str(e)}")
        else:
            st.warning("Please enter some text!")

# Tab 2: Data Analyzer
with tab2:
    st.subheader("Data Analyzer")
    uploaded_file = st.file_uploader("Upload a CSV file", type=["csv"])
    if uploaded_file is not None:
        try:
            result = data_agent(uploaded_file)
            st.write("### 📊 Data Summary:")
            st.write(f"**Rows:** {result['rows']}")
            st.write(f"**Columns:** {result['columns']}")
            st.write("**First 3 Rows:**")
            st.write(result['head'])
            if "output_plot" in result:
                st.image(result["output_plot"], caption="Data Visualization")
            else:
                st.info("No visualization generated for this dataset.")
        except Exception as e:
            st.error(f"Error processing CSV file: {str(e)}")

# Tab 3: Q&A Agent
with tab3:
    st.subheader("Q&A Agent")
    question = st.text_input("Ask a question (e.g. 'Who is Ada Lovelace?')")
    if st.button("Ask", key="qa"):
        if question.strip():
            try:
                answer = general_agent(question)
                st.write("### 🤖 Answer:")
                st.info(answer)
            except Exception as e:
                st.error(f"Error answering question: {str(e)}")
        else:
            st.warning("Please enter a question!")