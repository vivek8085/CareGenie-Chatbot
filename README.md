# CareGenie-Chatbot
This is AI Chatbot for Hospital Management built by using NLP.
Project Features:->
_________________________________________________________________________________________
## Core Features:-
Patient Interaction: CareGenie interacts with patients to answer questions related to hospital services, doctor availability, appointment booking, medical record queries, and more.
Appointment Scheduling: The chatbot assists patients in scheduling or rescheduling appointments with doctors based on their availability.
Medical Information: Patients can ask CareGenie about medical services, treatment options, and doctor specialties.
Query Resolution: CareGenie answers general queries such as operating hours, hospital directions, and provides health tips.
Conversation History: All user interactions with the chatbot are logged for reference and can be reviewed later.
Data-Driven Responses: CareGenie leverages a machine learning model trained on labeled intents and entities, ensuring accurate and context-aware responses.
__________________________________________________________________________________________
## Technology Stack:
Natural Language Processing (NLP): The chatbot uses NLP techniques such as tokenization and TF-IDF for text vectorization to understand and classify user queries.
Machine Learning: A Logistic Regression classifier is employed to predict the appropriate response based on the user input, which is matched to predefined intents.
Streamlit: A web-based interface is developed using Streamlit, making it easy for users to interact with the chatbot and for hospital administrators to view conversation histories.
Python Libraries: Key libraries such as nltk, scikit-learn, and streamlit are used to build, train, and deploy the chatbot.
__________________________________________________________________________________________
## DataSets:-
The dataset used in this project is a collection of labelled intents and entities. The data is stored in a list.
Intents: The intent of the user input (e.g. "Doctor_Query", "booking", "about_medical_services")
Entities: The entities extracted from user input (e.g. "Hi", "What is timimg of the doctor?", "Booking_slots")
Text: The user input text.
__________________________________________________________________________________________
## Project Breakdown:
Data Collection: The chatbot’s functionality is based on a dataset of labeled intents and their corresponding patterns and responses. These intents include medical queries, appointment bookings, and general hospital information.
Training Model: The model is trained using the labeled data to classify user input into relevant intents, which are then matched with predefined responses.
User Interface: The chatbot interface is designed to be user-friendly, featuring text inputs and responses, along with a sidebar that provides easy navigation to features such as "Home," "History," and "About."
Continuous Improvement: The system logs conversations, which allows for future improvements and fine-tuning of the chatbot by analyzing interactions and refining the response model.
