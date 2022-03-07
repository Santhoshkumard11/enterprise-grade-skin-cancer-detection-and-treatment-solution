# Enterprise grade skin cancer detection and treatment solution

This solution is completely built by leveraging __Low code/No code platforms__ such as Power Apps and Power Automate, as well as Azure serverless offerings.
The flow goes something like this, employee/nurse in the hospital can add new patient into the system and upload their skin sample image into the system which then goes through the ML model for initial
screening and the result is send to a dermatologist for closure. Once this is done then an appointment is scheduled automatically if cancer is detected and the treatment plan is created in the backend and updated in the SharePoint List. The dermatologist can view the slots booked and the patient details.

## YouTube Demo Video 📺📺
### [Click here to watch the Power Apps walk-through and working demo.](https://www.youtube.com/watch?v=DFKe5eMj2_c&ab_channel=LateNightCodewithSanthosh)


<a href="https://youtu.be/DFKe5eMj2_c">
  <img src="https://img.youtube.com/vi/DFKe5eMj2_c/hqdefault.jpg" width="600" height="370" alt="video">
</a>


## Architecture Diagram
<img src="https://github.com/Santhoshkumard11/enterprise-grade-skin-cancer-detection-and-treatment-solution/blob/main/images/architecture_diagram.jpg" height="380" width="1300" alt="architecture diagram">

## Services Used
- __Power Apps__ as UI
- __Power Automate__ for flow triggers
- __SharePoint__ as database
- Azure Functions for exposing model endpoint and upload image to blob storage
- Logic Apps for receiving response from Adaptive Card
- Azure Blob Storage for storing predicted images
- Azure DevOps keeping track of False positive images
- Adaptive Cards (Outlook Actionable Message)

## Power Automate Flows
1. #### Detect Sample Image

    - Send the image as bytes to the Azure Function where it reconstructs the image, predicts the type of cancer and sends a json payload to Power Automate. Then the __CancerType__ column is updated in the SharePoint List

2. #### Send Email to Dermatologist

    - Gets the dermatologist details, create a  __slot list item__, compose the adaptive card with all the above details and send it to the dermatologist

## Logic Apps Flow
1. #### Response from Adaptive Card
    - Once the dermatologist confirms the appointment and submits the card. The details is recorded and the Patient item list and slot item list are updated with the details, finally a mail is triggered to the patient with the appointment date and time 
## Power Apps Images
<img src="https://github.com/Santhoshkumard11/enterprise-grade-skin-cancer-detection-and-treatment-solution/blob/main/images/dashboard.jpg" height="580" alt="dashboard of Power Apps">

## About the ML model used
- Model trained with images from the dataset (here)[https://www.kaggle.com/nodoubttome/skin-cancer9-classesisic]
- It gives out the following labels,
    - basal 
    - Dermatofibrosarcoma protuberans
    - cutaneous
    - Merkel
    - melanoma
    - squamous cell carcinoma
    - Negative
- Accuracy of 95% trained over 35 epochs

## TODO:
- Auto select the dermatologist based on the availability and critical care needed for the patient
- Send an Calendar invite instead of the plain text email when the dermatologist confirm the appointment
- Setup a retraining mechanism which trains the model with the latest images per month in Azure Machine Learning (designer)