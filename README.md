# Enterprise grade skin cancer detection and treatment solution

This solution is completely built by leveraging __Low code/No code platforms__ such as Power Apps and Power Automate, as well as Azure serverless offerings.
The flow goes something like this, employee/nurse in the hospital can add new patient into the system and upload their skin sample image into the system which then goes through the ML model for initial
screening and the result is send to a dermatologist for closure. Once this is done then an appointment is scheduled automatically if cancer is detected and the treatment plan is created in the backend and updated in the SharePoint List. The dermatologist can view the slots booked and the patient details.

## Dev Blog Post 📑
### [Click here to read the dev.to blog post](https://dev.to/sandy_codes_py/enterprise-grade-skin-cancer-detection-and-treatment-solution-using-power-platform-microsoft-azure-cloud-963)

## YouTube Demo Video 📺📺
### [Click here to watch the Power Apps walk-through and working demo.](https://www.youtube.com/watch?v=9fqYRIaMOa0&ab_channel=LateNightCodewithSanthosh)


<a href="https://youtu.be/9fqYRIaMOa0">
  <img src="https://img.youtube.com/vi/9fqYRIaMOa0/hqdefault.jpg" alt="video">
</a>


### How to Upload the Power Apps to your environment

1. Download the Power App ZIP file from Power Platform Services folder in the repo

2. Go to your Power Apps portal, click on import canvas app

3. Upload the zip file and wait for it to upload

4. Replace the connectors of SharePoint and Outlook to make it working.

You can also upload the Power Automate flows separately if you want.

## Architecture Diagram
<img src="https://github.com/Santhoshkumard11/enterprise-grade-skin-cancer-detection-and-treatment-solution/raw/ml-model-dev/images/architecture_diagram_full.png" alt="architecture diagram">


![Architecture Diagram Flow](https://github.com/Santhoshkumard11/enterprise-grade-skin-cancer-detection-and-treatment-solution/raw/ml-model-dev/images/architecture_diagram_flow.png)

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


### Azure Resource Group
<img src="https://github.com/Santhoshkumard11/enterprise-grade-skin-cancer-detection-and-treatment-solution/raw/ml-model-dev/images/resource_group.jpg" alt="Azure resource group">

## Power Apps Images
### Dashboard - Light/Dark themes
<img src="https://github.com/Santhoshkumard11/enterprise-grade-skin-cancer-detection-and-treatment-solution/raw/ml-model-dev/images/dashboard_light.jpg" alt="dashboard of Power Apps light">

<img src="https://github.com/Santhoshkumard11/enterprise-grade-skin-cancer-detection-and-treatment-solution/raw/ml-model-dev/images/dashboard_dark.jpg" alt="dashboard of Power Apps dark">

### Patient Details List - with search enabled
<img src="https://github.com/Santhoshkumard11/enterprise-grade-skin-cancer-detection-and-treatment-solution/raw/ml-model-dev/images/patient_details.jpg" alt="Patient details list">

### Doctor Home
<img src="https://github.com/Santhoshkumard11/enterprise-grade-skin-cancer-detection-and-treatment-solution/raw/ml-model-dev/images/doctor_profile.jpg" alt="doctor home">

### Patient Profile
<img src="https://github.com/Santhoshkumard11/enterprise-grade-skin-cancer-detection-and-treatment-solution/raw/ml-model-dev/images/patient_profile.jpg" alt="patient profile">

## Power Apps Versions
![Power Apps Versions](https://github.com/Santhoshkumard11/enterprise-grade-skin-cancer-detection-and-treatment-solution/raw/ml-model-dev/images/power-apps-version-view.gif)

## About the ML model used
- Model trained with images from the dataset [here](https://www.kaggle.com/nodoubttome/skin-cancer9-classesisic)
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
- Live Chat assistance through Virtual Agents