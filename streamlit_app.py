import streamlit as st

# st.title("🧪 💊 Brown's Deprescribing Assurer 🧪 💊 ")
st.write(
    "This tool aims to provide a guide on relevant points to consider when deprescribing a medication. "+
    "While it offers insights into whether deprescribing may be appropriate or inappropriate based on your responses, it cannot provide a definitive answer. "+
    "Each patient's situation is unique, and not all variables can be accounted for in this tool - human clinical judgment is final!"
)

drug = st.selectbox("Select Medication:", ["Antidepressant", "Benzodiazepine", "Laxative", "Opioid", "PPI"])

if drug == "PPI":
    duration = st.selectbox("How long has the patient been on the PPI?", ["< 6 months", "6-12 months", "> 12 months"])
    side_effects = st.checkbox("Is the patient experiencing side effects?")