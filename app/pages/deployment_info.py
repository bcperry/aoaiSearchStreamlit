import streamlit as st
import os
st.title("Deployment Information")

deployment_info = {
    "Azure OpenAI Endpoint": os.environ.get("AZURE_OPENAI_ENDPOINT", "Not Set"),
    "Azure OpenAI Model": os.environ.get("AZURE_OPENAI_MODEL", "Not Set"),
    "OpenAI API Version": os.environ.get("OPENAI_API_VERSION", "Not Set"),
    "Azure Search Endpoint": os.environ.get("AZURE_SEARCH_ENDPOINT", "Not Set"),
    "Azure Search Index": os.environ.get("AZURE_SEARCH_INDEX", "Not Set")
    }

for key, value in deployment_info.items():
    st.write(f"**{key}:** {value}")