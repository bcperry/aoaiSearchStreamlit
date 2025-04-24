# Azure OpenAI RAG for Sovereign Cloud

This repository leverages Azure OpenAI's [built in RAG capability](https://learn.microsoft.com/en-us/azure/ai-services/openai/concepts/use-your-data) feature. and is designed to work from the ground up in Azure sovereign clouds.

## Getting Started

1. This repository has been developed for use within Azure sovereign cloud environments. To use this repository be sure to set the configuration before logging in

    ```
    azd config set cloud.name AzureUSGovernment
    ```

2. Login to your Azure account:
    ```
    azd auth login --use-device-code
    ```
3. Provision Azure resources and deploy the application code:
    ```
    azd up
    ```
    - Enter the environment name, Azure Subscription, and the location of the Azure resources one by one as instructed.


4. Setting Up a Python development environment and running web application:
    ```
    cd app
    streamlit run app.py
    ```
5. Redeploy the updated program:
   ```
   azd deploy
   ```
   Repeat steps 4 and 5 and enjoy your development process!
