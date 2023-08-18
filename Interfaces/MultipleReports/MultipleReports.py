import streamlit as st
from engine.MultipleReports.MultipleReports import MultipleReportsEngine


def MultipleReports():
    st.title("We are Comparing the reports for Cybota DAM Tembo Sacco Wednesday and Sunday")
    query = st.text_area("Insert your query", key="dhdssshjdjiudjd")
    if st.button("Submit Query", type="primary", key="MultipleReportsbutton"):
        with st.spinner("Processing your query..."):
            st.write(MultipleReportsEngine(query))
