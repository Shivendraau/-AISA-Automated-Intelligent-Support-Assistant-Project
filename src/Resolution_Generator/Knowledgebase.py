# Maintain an up-to-date knowledge base that includes documentation, previous solutions, and troubleshooting techniques.

from azure.storage.blob import BlobServiceClient, BlobClient, ContainerClient
import os

def upload_to_blob(container_name, file_path, blob_name):
    connect_str = os.getenv('AZURE_STORAGE_CONNECTION_STRING')
    blob_service_client = BlobServiceClient.from_connection_string(connect_str)
    blob_client = blob_service_client.get_blob_client(container=container_name, blob=blob_name)

    with open(file_path, "rb") as data:
        blob_client.upload_blob(data, overwrite=True)
    print(f"Uploaded {blob_name} to {container_name}")

# Example usage
# upload_to_blob('knowledgebase', 'path_to_article.txt', 'article1.txt')