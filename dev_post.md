## Brief Story to start with 🔮
Let's go back in time and think about how sophisticated we are now. In the earlier 1990s, we didn't have enough computing power or as many powerful computers as we do now to do complex operations and not train a machine learning model for sure. You won't be able to sit along and code all day staring at a CTR monitor in front of you. Humans have always been these evolving creatures; How to use things, discover things, think differently of the world. With that said, computer science and technology have been in the boom since we started experimenting and pushing them to their limits. Now here we are in 2022, battling out which is the best editor (`Vim Vs Emacs`) and with cloud empowering people to make digital transformations on all or most physical assets.

## 👨‍💻For people who say, enough of talk - [YouTube Demo Link](https://www.youtube.com/watch?v=9fqYRIaMOa0&ab_channel=LateNightCodewithSanthosh)
 
## 🕵️‍♂️For people who say, just show what you've built - [GitHub Repo Link](https://github.com/Santhoshkumard11/enterprise-grade-skin-cancer-detection-and-treatment-solution)

Here is a small example of how technology can be utilized in the right way to build something for humanity to sustain better in this changing world. When you're talking about cancer, regardless of type, detecting it as early as possible increases the chance of survival. 

## Medical Background 👩‍⚕️👨‍⚕️

> Skin cancer is the most common form of cancer, globally accounting for at least 40% of cancer cases and the most common type is nonmelanoma skin cancer, which occurs in at least 2–3 million people per year. 

[Source: Wikipedia](https://en.wikipedia.org/wiki/Skin_cancer)

## Solution 🧩

Seeing this and I thought why don't we solve something this bad, **leveraging Power Platform** for its simplicity and rapid development ability.

This solution is completely built by leveraging Low code/No code platforms such as Power Apps and Power Automate, as well as Azure serverless offerings. The flow goes something like this, employees/nurses in the hospital can add new patients into the system and upload their skin sample image which then goes through the ML model for initial screening, and the result is sent to a dermatologist for closure. Once this is done then an appointment is scheduled automatically if cancer is detected by the model and the dermatologist confirms the same. The desired treatment plan is created in the backend and updated in the SharePoint List which can be viewed by the patients through Power Apps. The dermatologist can view the slots booked and the patient details.

I've used Python in Azure Function, feel free to replicate the same in your favorite language. 🐱‍👤


## Azure Services Used
1. __Power Apps__ as UI
2. __Power Automate__ for flow triggers
3. __SharePoint__ as database
4. Azure Functions for exposing model endpoint and uploading an image to blob storage
5. Logic Apps for receiving the response from Adaptive Card
6. Azure Blob Storage for storing predicted images
7. Azure DevOps keeping track of False-positive images
8. Adaptive Cards (Outlook Actionable Message)

## Architecture Diagram

![Architecture Diagram](https://dev-to-uploads.s3.amazonaws.com/uploads/articles/38v7r05tqlhpokf1pcnb.png)

![Architecture Diagram Flow](https://github.com/Santhoshkumard11/enterprise-grade-skin-cancer-detection-and-treatment-solution/raw/ml-model-dev/images/architecture_diagram_flow.png)


## Azure Resource Group
Peek look at how the Azure Resource Group.

![Azure Resource Group](https://github.com/Santhoshkumard11/enterprise-grade-skin-cancer-detection-and-treatment-solution/raw/ml-model-dev/images/resource_group.jpg)

Enough of talk! Let’s see things in action, shall we?🤹‍♀️

## Patient Details Screen
With features like searching a patient based on Name, editing patient details, and adding new patients
![Patient Details](https://github.com/Santhoshkumard11/enterprise-grade-skin-cancer-detection-and-treatment-solution/raw/ml-model-dev/images/patient_details.jpg)

## Detect cancer type with ML model
As you see below we select the patient name from the dropdown, choose the image, and hit upload, a cool loader shows up to let you know that the image is sent to Azure Function, this triggers `DetectSampleImage` Power Automate flow. This **returns the detected cancer type**, **uploads the image to blob storage** for future reference, and updates the patient list item in SharePoint.

> The biggest part in doing this simple thing is how to send the image bytes to the flow and reconstruct the same in Azure Function

![Prediction Screen](https://github.com/Santhoshkumard11/enterprise-grade-skin-cancer-detection-and-treatment-solution/raw/ml-model-dev/images/detect_loading.jpg)

## Send an adaptive card to the dermatologist

Once this is done, you can choose the dermatologist from the dropdown and send this report via Adaptive Card Actionable item, this triggers the `SendEmailToDoctor` power automate flow and the step level is set to 1 now. 
![Detection Screen](https://github.com/Santhoshkumard11/enterprise-grade-skin-cancer-detection-and-treatment-solution/raw/ml-model-dev/images/detection_screen.jpg)

## Adaptive Card reply
Now the dermatologist receives the card as shown below. He/she can choose to reply at any time. Once submitted, it hits the `Logic Apps receiver endpoint` and the flow continues.
![Adaptive Card](https://github.com/Santhoshkumard11/enterprise-grade-skin-cancer-detection-and-treatment-solution/raw/ml-model-dev/images/adaptive_card.jpg)


## Logic App receiver
This gets the dermatologist's prediction type, appointment date, and time and updates it to the patient details list, and confirms the slot of the appointment. In the end, this also sends a card response to the dermatologist notifying that the details are saved successfully.
![Logic App response flow](https://github.com/Santhoshkumard11/enterprise-grade-skin-cancer-detection-and-treatment-solution/raw/ml-model-dev/images/receive_flow.jpg)


## Patient Receives appointment confirmation

After this, the patient receives the appointment date and time and the link to the Power Apps where he/she can track their progress. The step level is set to 2 now.
![Patient Receives the slot](https://github.com/Santhoshkumard11/enterprise-grade-skin-cancer-detection-and-treatment-solution/raw/ml-model-dev/images/patient_receive.jpg)


## Track details in Power Apps

Once the slot is booked the patient can track their progress with the timeline shown below their profile.
![Patient Details](https://github.com/Santhoshkumard11/enterprise-grade-skin-cancer-detection-and-treatment-solution/raw/ml-model-dev/images/patient_profile.jpg)


## Dermatologist's view

After the flow is complete the `slot requested` and `slots booked` will be updated with appropriate values.
![Dermatologist Profile](https://github.com/Santhoshkumard11/enterprise-grade-skin-cancer-detection-and-treatment-solution/raw/ml-model-dev/images/doctor_profile.jpg)


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
- You can find the model in the GitHub repo.

## Power Apps Versions - 30 versions to make it work as expected
![Power Apps Versions](https://github.com/Santhoshkumard11/enterprise-grade-skin-cancer-detection-and-treatment-solution/raw/ml-model-dev/images/power-apps-version-view.gif)

## VS Code with Azure Extension gets the job done
![VS Code editor](https://github.com/Santhoshkumard11/enterprise-grade-skin-cancer-detection-and-treatment-solution/raw/ml-model-dev/images/code.jpg)

## Future work/score:
- Auto-select the dermatologist based on the availability and critical care needed for the patient
- Send a Calendar invite instead of the plain text email when the dermatologist confirm the appointment
- Setup a retraining mechanism that trains the model with the latest images per month in Azure Machine Learning (designer)
- Live Chat assistance through Virtual Agents
- Set up a treatment plan for each patient who is diagnosed

Feel free to reach out if you need any further clarification on the implementation. I would be more than happy to answer those. 🤝

Looking forward to hearing from you and improvements via Comments or PRs are most welcomed.🙏

Congratulations!! 🎉you have completed reading this huge blog.🤩
Thanks a lot for reading out till the end.👓

Let’s connect if you want to collaborate on further work or a quick catch up.🤝
## References
#### [Connect on LinkedIn](https://linkedin.com/in/santhosh-kumard)

#### [Connect on Instagram](https://www.instagram.com/santhoshgoku)

#### [Connect on Twitter](https://twitter.com/sandy_codes_py)

{% embed https://dev.to/sandy_codes_py %}

{% embed https://github.com/Santhoshkumard11/enterprise-grade-skin-cancer-detection-and-treatment-solution %}