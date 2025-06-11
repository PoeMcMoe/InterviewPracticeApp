import streamlit as st
from dotenv import load_dotenv
import gpt_helper as gpt_helper
from streamlit_chat import message as messageUi

load_dotenv()

st.set_page_config(
    page_title="Interview Practice App",
    layout="wide",
)



def main():
    st.title("Interview Practice App")

    with st.container(height=500, border=True):
        for i, message in enumerate(gpt_helper.messages):
            if message["role"] == "assistant":
                messageUi(message['content'], is_user=False, key=i)
            else:
                messageUi(message['content'], is_user=True, key=i)

    st.session_state.spinner_container = st.empty()
    
    st.text_input(
        "Message", 
        key="message_input",
        on_change=handle_input,
        placeholder="Type your message and press Enter..."
    )
    

    
def handle_input():
    if st.session_state.message_input.strip():
        with st.session_state.spinner_container:
            with st.spinner('Processing your message...'):
                gpt_helper.on_prompt_entered(st.session_state.message_input)
                st.session_state.message_input = ""

if __name__ == "__main__":
    main()