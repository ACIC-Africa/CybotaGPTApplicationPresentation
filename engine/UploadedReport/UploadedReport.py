import streamlit as st
import pandas as pd
import json


def function_for_question(name):
    print(name)


def UploadedReport():
    st.write("Please upload your Weekly Report Here")

    data = st.file_uploader("Upload a Report")

    query = st.text_area("Insert your query")

    # Streamlit UI setup

    st.sidebar.title("Predefined Prompts")

    st.sidebar.markdown("#### Click To Get Response")

    question_list = [
        "what interesting discoveries do you have from the data shared above ?",
        "As A CISO, whst should I be worrid about, if I recieve this report ?",
        "KIndly suggest any stsps I should take to close or investigate any issues ?",
        "What protocols are being used in the data ?",
        "Can you identify any CVEs in the data ?",
        "What security tools are being used in the data?",
        "Are the tools identified below maliciuous and kindly name the tools you will identify ?",
        "What services are running in the data ?",
        "What services are running in the data ?",
        "What recommendadtions do you have ?",
        "what ports are being used kindly give the data in a tabular manner and describe work of the port?",
        "what intelligence can I draw ?",
    ]

    for idx, question in enumerate(question_list):
        # Using an incremental index as a unique key for the button
        if st.sidebar.button(question, key=idx):
            function_for_question(question)
