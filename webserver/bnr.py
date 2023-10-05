import streamlit as st
from businessLogic import transcribeVideoOrchestrator
import os

def main():
    st.title("Video2Text - Offline Mode")

    # User input: Upload video file
    uploaded_file = st.file_uploader("Upload a video file", type=["mp4", "avi", "mkv"])

    # User input: model
    models = ["tiny", "base", "small", "medium", "large"]
    model = st.selectbox("Select Model:", models)
    st.write(
        "If you take a smaller model it is faster but not as accurate, whereas a larger model is slower but more accurate.")

    if uploaded_file:
        # Save the uploaded video to a temporary location
        video_path = os.path.join("temp_videos", uploaded_file.name)
        os.makedirs("temp_videos", exist_ok=True)
        with open(video_path, "wb") as f:
            f.write(uploaded_file.read())

        if st.button("Transcribe"):
            transcript = transcribeVideoOrchestrator(video_path, model)

            if transcript:
                st.subheader("Transcription:")
                st.write(transcript)
            else:
                st.error("Error occurred while transcribing.")
                st.write("Please try again.")

    st.write(
        "If you need help or have questions about Video2Text, feel free to reach out to me.")

    st.write("Please enter your message below:")
    user_message = st.text_area("Your Message:")

    st.markdown(
        f'<a href="mailto:contact@jhayer.tech?subject=Video2Text-Help&body={user_message}">Send Mail</a>', unsafe_allow_html=True)


if __name__ == "__main__":
    main()
