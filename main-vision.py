import os
from openai import OpenAI
import streamlit as st
import mimetypes
from io import BytesIO
import base64

st.title("Grok Chatbot")

client = OpenAI(api_key=st.secrets["XAI_API_KEY"])

client = OpenAI(
    api_key=os.getenv("XAI_API_KEY"),
    base_url="https://api.x.ai/v1",
)

if "openai_model" not in st.session_state:
    st.session_state["openai_model"] = "grok-vision-beta"

if "messages" not in st.session_state:
    st.session_state.messages = [
        {"role": "system", "content": "You are Grok, a chatbot inspired by the Hitchhikers Guide to the Galaxy."}
    ]

# Add file uploader
uploaded_file = st.file_uploader("Upload a document or image", type=["txt", "pdf", "png", "jpg", "jpeg"])

# Process uploaded file
file_content = None
if uploaded_file is not None:
    mime_type = mimetypes.guess_type(uploaded_file.name)[0]
    
    if mime_type and mime_type.startswith('image/'):
        # Handle images
        file_bytes = uploaded_file.getvalue()
        base64_image = base64.b64encode(file_bytes).decode('utf-8')
        file_content = {
            "type": "image_url",
            "image_url": {
                "url": f"data:{mime_type};base64,{base64_image}"
            }
        }
    elif mime_type and mime_type.startswith('text/'):
        # Handle text files only
        try:
            file_content = {
                "type": "text",
                "text": uploaded_file.getvalue().decode('utf-8')
            }
        except UnicodeDecodeError:
            st.error("Unable to decode the text file. Please ensure it's a valid text file.")
    else:
        # Handle other file types (like PDFs)
        st.error(f"File type {mime_type} is not currently supported.")

for message in st.session_state.messages:
    with st.chat_message(message["role"]):
        # Handle different message content types
        if isinstance(message["content"], list):
            # Only display the text portion of the message
            text_content = next((item["text"] for item in message["content"] 
                               if item["type"] == "text"), "")
            st.markdown(text_content)
        else:
            st.markdown(message["content"])

if prompt := st.chat_input("What is up?"):
    # Modify message construction to include file content if present
    user_message = {"role": "user", "content": prompt}
    if file_content and uploaded_file.name not in [m.get("file_name", "") for m in st.session_state.messages]:
        user_message["content"] = [file_content, {"type": "text", "text": prompt}]
        user_message["file_name"] = uploaded_file.name
    
    st.session_state.messages.append(user_message)
    with st.chat_message("user"):
        # For display purposes, only show the text prompt
        st.markdown(prompt)
        # Only show the uploaded file for the first message that references it
        if uploaded_file and mime_type and uploaded_file.name not in [m.get("file_name", "") for m in st.session_state.messages[:-1]]:
            if mime_type.startswith('image/'):
                st.image(uploaded_file)
            elif 'text' in file_content:
                st.text(file_content["text"])

    with st.chat_message("assistant"):
        message_placeholder = st.empty()
        full_response = ""
        
        # For API calls, we need to format the messages differently
        api_messages = []
        for m in st.session_state.messages:
            if isinstance(m["content"], list):
                # Keep the full content (including image) for API calls
                api_messages.append({"role": m["role"], "content": m["content"]})
            else:
                # For text-only messages, pass them as is
                api_messages.append({"role": m["role"], "content": m["content"]})
        
        stream = client.chat.completions.create(
            model=st.session_state["openai_model"],
            messages=api_messages,
            stream=True,
        )
        
        for chunk in stream:
            if chunk.choices[0].delta.content is not None:
                full_response += chunk.choices[0].delta.content
                message_placeholder.markdown(full_response + "▌")
        
        message_placeholder.markdown(full_response)
        st.session_state.messages.append({"role": "assistant", "content": full_response})
