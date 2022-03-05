import logging
import azure.functions as func


def main(req: func.HttpRequest) -> func.HttpResponse:
    logging.info("Skin Cancer detection endpoint called")
    
    # set the image name to default for testing
    test_image_path = "images/test.png"
    if req.method == "GET":
            
        image_name = req.params.get('image_name')
        if image_name == "null":
            return func.HttpResponse("""Thanks for checking out the api. It works!!
                                     You can pass image_name with test.png as params to get a sample detection of the model.""", status_code=200)
        else:
            return func.HttpResponse(
                f"Image name - {image_name} dummy result",
                status_code=200
            )

    else:
        # get the binary image from the request body
        req_body = req.get_json()
        image_binary = req_body.get('image_binary')["$content"]

        try:
            # call the detection model method
            # test_result = detect(image_binary)
            logging.info(f"Binary image data {str(image_binary)[:100]}")

        except Exception as e:
            logging.exception(f"Here is the error: \n{e}")
            return func.HttpResponse("Something went wrong during detection")
    
    logging.info("Skin Cancer detection ended")
    
    return func.HttpResponse(
                "dummy result from post method",
                status_code=200
            )
        
