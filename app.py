import streamlit as st
from dotenv import load_dotenv
import controller as controller
from streamlit_chat import message as messageUi

load_dotenv()

st.set_page_config(
    page_title="Interview Practice App",
    layout="wide",
)



def main():
    st.title("Interview Practice App")

    with st.container(height=500, border=True):
        for message in controller.messages:
            if message["role"] == "assistant":
                messageUi(message['content'], is_user=False)
            else:
                messageUi(message['content'], is_user=True)

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
                controller.on_prompt_entered(st.session_state.message_input)
                st.session_state.message_input = ""

if __name__ == "__main__":
    main()