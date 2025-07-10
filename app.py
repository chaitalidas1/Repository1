import streamlit as st

st.title("Upload a File")

uploaded_file = st.file_uploader("Choose a file", type=["csv", "txt", "pdf", "png", "jpg"])
if uploaded_file is not None:
    st.success(f"Uploaded: {uploaded_file.name}")
    # To save:
    with open(uploaded_file.name, "wb") as f:
        f.write(uploaded_file.getbuffer())
    st.info("File saved locally.")