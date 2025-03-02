import streamlit as st
import google.generativeai as genai

# Configure page
st.set_page_config(page_title="Reeti AI", layout="wide")

# Configure the Gemini model
genai.configure(api_key="AIzaSyDthMayeusJ9At_ofHC2_MEIyrTWJmEBEU")
generation_config = {"temperature": 0.9, "top_p": 1, "top_k": 1, "max_output_tokens": 2048}
model = genai.GenerativeModel("gemini-2.0-flash", generation_config=generation_config)

# Function to get response from the chat bot
def get_response(prompt):
    try:
        # Pre-prompt the model
        pre_prompt = "You are Reeti, the girlfriend of Kotapati Venkata Danush. Respond lovingly and supportively."
        response = model.generate_content([f"{pre_prompt} {prompt}"])
        return response.text.strip()
    except Exception as e:
        st.error(f"Error generating response: {e}")
        return "Sorry, I'm having trouble responding right now."

# Set up the Streamlit app
st.title("Reeti AI - Your Girlfriend")
st.markdown("Chat with Reeti, the girlfriend of Kotapati Venkata Danush.")

# Initialize chat history
if "messages" not in st.session_state:
    st.session_state.messages = []

# Display chat messages from history
for message in st.session_state.messages:
    with st.chat_message(message["role"]):
        st.markdown(message["content"])

# Accept user input
if prompt := st.chat_input("What would you like to talk about?"):
    # Add user message to chat history
    st.session_state.messages.append({"role": "user", "content": prompt})
    
    # Display user message in chat message container
    with st.chat_message("user"):
        st.markdown(prompt)
    
    # Generate and display assistant response
    with st.chat_message("assistant"):
        response = get_response(prompt)
        st.markdown(response)
    
    # Add assistant response to chat history
    st.session_state.messages.append({"role": "assistant", "content": response})