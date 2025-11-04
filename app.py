import streamlit as st
from openai import OpenAI

# Set page config
st.set_page_config(page_title="Chatbot", page_icon="💬", layout="centered")

# Initialize the OpenAI client (make sure your OPENAI_API_KEY is set as an environment variable)
client = OpenAI()

# Title
st.title("💬 Chat with AI")
st.caption("Built with Streamlit and OpenAI GPT-5")

# Initialize session state for chat history
if "messages" not in st.session_state:
    st.session_state["messages"] = [
        {"role": "system", "content": "You are a helpful assistant."}
    ]

# Display the chat history
for msg in st.session_state.messages[1:]:  # skip the system message
    if msg["role"] == "user":
        st.chat_message("user").markdown(msg["content"])
    else:
        st.chat_message("assistant").markdown(msg["content"])

# User input
if prompt := st.chat_input("Type your message..."):
    # Display user message
    st.chat_message("user").markdown(prompt)
    st.session_state.messages.append({"role": "user", "content": prompt})

    # Generate response
    with st.chat_message("assistant"):
        with st.spinner("Thinking..."):
            response = client.chat.completions.create(
                model="gpt-4o-mini",  # use GPT-5 if available for your account
                messages=st.session_state.messages,
            )
            msg = response.choices[0].message.content
            st.markdown(msg)
    st.session_state.messages.append({"role": "assistant", "content": msg})
