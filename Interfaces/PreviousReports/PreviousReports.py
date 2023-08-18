import streamlit as st
from engine.PreviousReports.PreviousReports import PreviousReports, callchain


def PreviousReportsInterface():
    print("here")
    PreviousReports()

    selected_option = st.selectbox("Select an option:", ["malwareEvents", "userLogonsEvents"])

    query = st.text_area("Insert your query", key="dhdhjdjiudjd")

    if st.button("Submit Query", type="primary"):
        with st.spinner("Processing your query..."):
            st.write(callchain(selected_option, query))
