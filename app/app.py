import os
import streamlit as st
from openai import AzureOpenAI
from azure.identity import DefaultAzureCredential, get_bearer_token_provider
from dotenv import load_dotenv

load_dotenv()



st.title('Azure OpenAI On Your Data with Streamlit')

token_provider = get_bearer_token_provider(
    DefaultAzureCredential(),
    "https://cognitiveservices.azure.us/.default"
)
client = AzureOpenAI(
                azure_endpoint=os.environ["AZURE_OPENAI_ENDPOINT"],
                api_key=os.environ["AZURE_OPENAI_API_KEY"],
                api_version=os.environ["OPENAI_API_VERSION"])

if 'messages' not in st.session_state:
    st.session_state.messages = []

for message in st.session_state.messages:
    st.chat_message(message['role']).write(message['content'])

if prompt := st.chat_input('What is up?'):
    st.session_state.messages.append({'role': 'user', 'content': prompt})
    st.chat_message('user').write(prompt)

    stream = client.chat.completions.create(
        model='gpt-4o',
        messages=st.session_state.messages,
        stream=True,
        extra_body={
            'data_sources': [{
                'type': 'azure_search',
                'parameters': {
                    'endpoint': os.getenv('AZURE_SEARCH_ENDPOINT'),
                    'index_name': 'vector-index',
                    'semantic_configuration': 'default',
                    'query_type': 'vector_semantic_hybrid',
                    'authentication': {
                        'type': 'system_assigned_managed_identity'
                    },
                    'embedding_dependency': {
                        'type': 'deployment_name',
                        'deployment_name': 'text-embedding-ada-002'
                    }
                }
            }]
        }
    )
    response = st.chat_message('ai').write_stream(stream)
    st.session_state.messages.append({'role': 'assistant', 'content': response})