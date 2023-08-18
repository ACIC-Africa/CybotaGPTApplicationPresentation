import streamlit as st
from Interfaces.UploadedReport.UploadedReport import UploadedReport
from Interfaces.PreviousReports.PreviousReports import PreviousReportsInterface
from Interfaces.MultipleReports.MultipleReports import MultipleReports
image_url = "/var/www/html/serianu_projects/cveq_database_access_and_transactions_monitoring_application/database-access-monitoring-frontend-vue-js/src/assets/Cybota_Logo-01-01.png"
custom_width = 250  # Set your desired width in pixels
st.image(image_url, width=custom_width)

st.title("👨‍💻 Cybota GPT")

tab1, tab2, tab3 = st.tabs(["Run Against Uploaded Report", "Run Against Previous Reports", "Compare Multiple Reports"])

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

question_list2 = [
    "what interesting discoveries do you have from the data shared above fff ?",
]

with tab1:
    st.header("Run Against Uploaded Report")
    st.sidebar.empty()  # Clear the sidebar
    for idx, question in enumerate(question_list2):
        # Using an incremental index as a unique key for the button
        if st.sidebar.button(question, key=question):
            print(question)
            # function_for_question(question)

    UploadedReport()

with tab2:
    st.sidebar.empty()  # Clear the sidebar
    for idx, question in enumerate(question_list):
        # Using an incremental index as a unique key for the button
        if st.sidebar.button(question, key=idx):
            print(question)
            # function_for_question(question)
    st.header("Run Against Previous Reports")
    PreviousReportsInterface()

with tab3:
    st.header("Compare Multiple Reports")
    MultipleReports()
