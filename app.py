{
 "cells": [
  {
   "cell_type": "code",
   "execution_count": null,
   "id": "bbb3e898",
   "metadata": {
    "vscode": {
     "languageId": "plaintext"
    }
   },
   "outputs": [],
   "source": [
    "# app.py\n",
    "import streamlit as st\n",
    "from grammar_checker import check_and_correct\n",
    "from data_summary import summarize_csv\n",
    "from pathlib import Path\n",
    "\n",
    "st.set_page_config(page_title=\"CodeLingoo Mini-Agent\", layout=\"centered\")\n",
    "st.title(\"CodeLingoo — Mini Agent (Grammar & Data)\")\n",
    "tab = st.tabs([\"Grammar Helper\", \"Data Analyzer\"])\n",
    "\n",
    "with tab[0]:\n",
    "    st.header(\"Grammar Helper\")\n",
    "    text = st.text_area(\"Paste English text here\", height=150)\n",
    "    if st.button(\"Check & Correct (Grammar)\"):\n",
    "        if not text.strip():\n",
    "            st.warning(\"Please enter some English text.\")\n",
    "        else:\n",
    "            corrected, issues = check_and_correct(text)\n",
    "            st.subheader(\"Corrected Text\")\n",
    "            st.write(corrected)\n",
    "            st.subheader(\"Top issues (first 5)\")\n",
    "            for i, it in enumerate(issues[:5], 1):\n",
    "                st.write(f\"{i}. {it['message']} — Suggestions: {it['suggestions']}\")\n",
    "\n",
    "with tab[1]:\n",
    "    st.header(\"Data Analyzer (CSV)\")\n",
    "    uploaded = st.file_uploader(\"Upload CSV file\", type=[\"csv\"])\n",
    "    if uploaded is not None:\n",
    "        st.info(\"Processing CSV...\")\n",
    "        summary = summarize_csv(uploaded)\n",
    "        st.write(\"Basic info:\")\n",
    "        st.json(summary)\n",
    "        if summary.get(\"output_plot\"):\n",
    "            st.image(summary[\"output_plot\"], caption=\"Survival by Sex\", use_column_width=True)\n"
   ]
  }
 ],
 "metadata": {
  "language_info": {
   "name": "python"
  }
 },
 "nbformat": 4,
 "nbformat_minor": 5
}
