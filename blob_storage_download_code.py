# Python program to bulk download blob files from azure storage

import os
from azure.storage.blob import BlobServiceClient, BlobClient
from azure.storage.blob import ContentSettings, ContainerClient
 
# IMPORTANT: Replace connection string with your storage account connection string
# Usually starts with DefaultEndpointsProtocol=https;...
MY_CONNECTION_STRING = "DefaultEndpointsProtocol=https;AccountName=robotblobstorage;AccountKey=RCFmar+aazCbwZh8mb05CLoURy3pyg+mKNOWes7byOrUhFXmqgMECSFBQwFXmaYjVo5Dotd+x2PccK9NLiLypA==;EndpointSuffix=core.windows.net"
 
# Replace with blob container
MY_BLOB_CONTAINER = "sewerpipelinepictures"
 
# Replace with the local folder where you want files to be downloaded
LOCAL_BLOB_PATH = "download_images"
 
class AzureBlobFileDownloader:
  def __init__(self):
    print("Intializing Azure Blob File Downloader Hello")
 
    # Initialize the connection to Azure storage account
    self.blob_service_client =  BlobServiceClient.from_connection_string(MY_CONNECTION_STRING)
    self.my_container = self.blob_service_client.get_container_client(MY_BLOB_CONTAINER)
 
 
  def save_blob(self,file_name,file_content):
    # Get full path to the file
    download_file_path = os.path.join(LOCAL_BLOB_PATH, file_name)
 
    # for nested blobs, create local path as well!
    os.makedirs(os.path.dirname(download_file_path), exist_ok=True)
 
    with open(download_file_path, "wb") as file:
      file.write(file_content)
 
  def download_all_blobs_in_container(self):
    my_blobs = self.my_container.list_blobs()
    for blob in my_blobs:
      print("Downloading file - " + blob.name)
      bytes = self.my_container.get_blob_client(blob).download_blob().readall()
      self.save_blob(blob.name, bytes)
 
# Initialize class and upload files
azure_blob_file_downloader = AzureBlobFileDownloader()
azure_blob_file_downloader.download_all_blobs_in_container()
