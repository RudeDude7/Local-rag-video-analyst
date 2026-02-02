import streamlit as st
import rag_engine # Importing the logic from Section 2

st.set_page_config(page_title="YouTube AI Assistant", page_icon="🎥")

st.title("🎥 YouTube Video AI Assistant")
st.markdown("I can answer questions about any YouTube video!")

# 1. Input: User pastes URL
video_url = st.text_input("Paste YouTube Video URL here:")

# 2. Input: User asks question
query = st.text_input("What do you want to know about the video?")

# 3. Button: Trigger the AI
if st.button("Get Answer"):
    if video_url and query:
        with st.spinner("Analyzing video... (This might take a minute the first time)"):
            try:
                # Call the function from our backend file
                answer = rag_engine.process_video_and_ask(video_url, query)
                st.success("Here is what I found:")
                st.write(answer)
            except Exception as e:
                st.error(f"An error occurred: {e}")
    else:
        st.warning("Please enter both a URL and a question.")