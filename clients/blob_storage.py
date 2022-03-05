from azure.storage.blob import BlobServiceClient
import logging
import os

class BlobStorageConnectionError(Exception):
    pass


class CustomBlobStorageClient:

    def __init__(self, container_name: str, blob_name: str):
        """connect with the blob storage account

        Args:
            container_name (str): name of the container
            blob_name (str): name of the blob to be created

        Raises:
            BlobStorageConnectionError: If it's not able to connect with the account
        """

        try:
            self.blob_client_object = BlobServiceClient.from_connection_string(
                os.environ.get("BLOB_STORAGE_CONNECTION_STRING"))

            self.container_client = self.blob_client_object.get_container_client(
                container_name)

            self.blob_client = self.container_client.get_blob_client(blob_name)
        except Exception as e:
            logging.exception(f"Error while connecting to Azure Blob Storage {e}")
            raise BlobStorageConnectionError

        logging.info("Successfully connected to blob storage account")

    # just in case if we want to use it externally
    @property
    def get_blob_client(self):
        return self.blob_client


    def upload_image(self, bytes_image: str):
        """ Upload the image to the initalized blob storage account

        Args:
            bytes_image (str): image in bytes
        """

        logging.info("Starting to upload image to blob storage")

        try:
            # upload it to blob storage with the respective client
            self.blob_client.upload_blob(
                bytes_image, overwrite=True, blob_type="BlockBlob")

            logging.info("Successfully uploaded image to blob storage")
        except Exception as e:
            logging.exception(f"Error while uploading image to blob storage \n{e}")
            raise