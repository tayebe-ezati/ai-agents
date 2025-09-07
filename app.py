import sys
import os
import streamlit as st

# -----------------------------
# اضافه کردن مسیر پروژه به sys.path
# -----------------------------
BASE_DIR = os.path.dirname(os.path.abspath(__file__))
if BASE_DIR not in sys.path:
    sys.path.append(BASE_DIR)

from agents.grammar.grammar_checker import check_and_correct
from agents.data.data_summary import summarize_csv

# -----------------------------
# تنظیمات اولیه Streamlit
# -----------------------------
st.set_page_config(page_title="CodeLingoo Mini-Agent", layout="centered")
st.title("CodeLingoo — Mini Agent (Grammar & Data)")

# -----------------------------
# تب‌ها
# -----------------------------
tabs = st.tabs(["Grammar Helper", "Data Analyzer"])

# -----------------------------
# تب ۱: Grammar Helper
# -----------------------------
with tabs[0]:
    st.header("Grammar Helper")
    text = st.text_area("Paste English text here", height=150)

    if st.button("Check & Correct (Grammar)"):
        if not text.strip():
            st.warning("Please enter some English text.")
        else:
            corrected, issues = check_and_correct(text)

            st.subheader("Corrected Text")
            st.write(corrected)

            st.subheader("Top issues (first 5)")
            for i, it in enumerate(issues[:5], 1):
                st.write(f"{i}. {it['message']} — Suggestions: {it['suggestions']}")

# -----------------------------
# تب ۲: Data Analyzer (CSV)
# -----------------------------
with tabs[1]:
    st.header("Data Analyzer (CSV)")
    uploaded = st.file_uploader("Upload CSV file", type=["csv"])

    if uploaded is not None:
        st.info("Processing CSV...")
        summary = summarize_csv(uploaded)

        st.write("Basic info:")
        st.json({
            "rows": summary["rows"],
            "columns": summary["columns"],
            "head": summary["head"]
        })

        if summary.get("output_plot"):
            st.image(summary["output_plot"], caption="Survival by Sex", use_column_width=True)
