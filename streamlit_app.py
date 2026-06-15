import tempfile

import streamlit as st
st.set_page_config(page_title="Deepfake Audio Detection", layout="wide")
st.title("Deepfake Audio Detection")
st.divider()
st.write ("Upload an audio file to check if it's a deepfake or not. Supported formats: .wav files only")
uploaded_file = st.file_uploader("Choose an audio file", type=["wav"])
if uploaded_file is not None:
    st.success("File uploaded successfully! Processing...")
    st.audio(uploaded_file)
    with tempfile.NamedTemporaryFile(delete=False, suffix=".wav") as temp_file:
        temp_file.write(uploaded_file.read())
        temp_file_path = temp_file.name
    st.write(f"File name: {uploaded_file.name}")    
    st.write("Processing the audio file...")
    if st.button("Run Detection"):
        with st.spinner("Running deepfake detection..."):
            # Here you would call your deepfake detection function, e.g.:
            # result = run_deepfake_detection(temp_file_path)
            # For demonstration, we'll just show a placeholder result
            import time
            time.sleep(2)  # Simulate processing time
            result = "Real"  # Placeholder result
