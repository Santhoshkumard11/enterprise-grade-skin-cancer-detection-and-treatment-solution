import os
import logging
import base64
import io
from PIL import Image
from clients.blob_storage import CustomBlobStorageClient, BlobStorageConnectionError
from helpers.predictor import detect_type

def get_image_from_binary_date(raw_image_bytes: str):
    
    return base64.b64decode(raw_image_bytes)


def process_image(raw_image_bytes: str, user_id: str, user_name: str):
    """ Recreate the image from bytes, dected the type and upload it to blob storage

    Args:
        raw_image_bytes (str): image in bytes
        user_id (str): user id for unique identification
        user_name (str): name of the user

    Returns:
        bool, str: returns a tuple of status and the prediction
    """
    logging.info("Started processing the image")

    try:
        
        image_in_bytes = get_image_from_binary_date(raw_image_bytes)
        logging.info("Image converted to bytes")
        
        image_object = Image.open(io.BytesIO(image_in_bytes))
        
        prediction = detect_type("", image_object=image_object, is_object=True)
        
        blob_storage_image_url = f"{user_id}_{user_name}_{prediction}.png"
        
        blob_client = CustomBlobStorageClient(os.environ.get("BLOB_STORAGE_CONTAINER_NAME"),
                                            blob_storage_image_url)
        
        blob_client.upload_image(image_in_bytes)
        
        logging.info("Successfully processed the image")

    except BlobStorageConnectionError:
        raise

    except Exception as e:
        logging.exception(f"Error while processing the image {e}")
        return False, ""

    return True, prediction

    
    