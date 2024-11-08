# Ensure data security, monitor application performance, and maintain comprehensive logs.

from azure.identity import ManagedIdentityCredential
from azure.keyvault.secrets import SecretClient
import os

def get_secret(secret_name):
    key_vault_name = os.getenv('KEY_VAULT_NAME')
    KVUri = f"https://{key_vault_name}.vault.azure.net"
    
    credential = ManagedIdentityCredential()
    client = SecretClient(vault_url=KVUri, credential=credential)
    
    retrieved_secret = client.get_secret(secret_name)
    return retrieved_secret.value

# Example usage
# openai_api_key = get_secret('OpenAI-API-Key')