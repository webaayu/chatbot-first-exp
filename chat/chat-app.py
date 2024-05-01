import streamlit as st
import requests

# Remote Ollama API URL
OLLAMA_API_URL = 'http://98.70.81.78:31949/api/generate'

# Function to generate text using the Ollama service
def generate_text(prompt, model):
    try:
        payload = {
            "model": model,
            "prompt": prompt,
            "stream": False
        }
        response = requests.post(OLLAMA_API_URL, json=payload)
        
        # Log the entire response text
       # st.write("Response Text:", response.text)
        
        if response.status_code == 200:
            json_response = response.json()
            generated_text = json_response.get('response', 'Failed to generate text')
            return generated_text
        else:
            return 'Failed to generate text: {}'.format(response.text)
    except Exception as e:
        return 'Error: {}'.format(str(e))

# Streamlit app code
prompt = st.text_input("Enter prompt", value="", key="prompt")
model = st.selectbox("Select model", ["llama2"])

if st.button('Generate Text'):
    if prompt:
        generated_text = generate_text(prompt, model)
        st.markdown('### Generated Text:')
        st.text_area('Generated Text', value=generated_text, height=200)
    else:
        st.warning('Please enter a prompt')
