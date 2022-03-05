import logging
import azure.functions as func
from helpers.predictor import detect_type
from detect_type.utils import process_image

def main(req: func.HttpRequest) -> func.HttpResponse:
    logging.info("Skin Cancer detection endpoint called..")

    # set the image name to default for testing
    test_image_path = "images/test.png"
    prediction = ""
    if req.method == "GET":
            
        image_name = req.params.get('image_name')
        if image_name == "null":
            return func.HttpResponse("""Thanks for checking out the api. It works!!
                                     You can pass image_name with test.png as params to get a sample detection of the model.""", status_code=200)
        else:

            prediction_result = detect_type(test_image_path, None, False)
            
            return func.HttpResponse(
                f"The prediction has been made - it's {prediction_result}",
                status_code=200
            )

    else:
        # get the binary image from the request body
        req_body = req.get_json()
        image_binary = req_body.get('image_binary')["$content"]
        user_id = req_body.get("user_id", "")
        user_name = req_body.get("user_name", "")

        try:
            status, prediction = process_image(image_binary, user_id, user_name)

            if not status or prediction is "":
                return func.HttpResponse(
                "Something went wrong during processing. Check the Application logs for more info",
                status_code=200
            )

        except Exception as e:
            logging.exception(f"Here is the error: \n{e}")
            return func.HttpResponse("Something went wrong during detection")
    
    logging.info("Skin Cancer detection ended")
    
    return func.HttpResponse(
                prediction,
                status_code=200
            )
        
