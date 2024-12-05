# CareGenie-Chatbot
This is AI Chatbot for Hospital Management built by using `NLP`.
--- 
Project Features
---
## Core Features
- Patient Interaction: CareGenie interacts with patients to answer questions related to hospital services, doctor availability, appointment booking, medical record queries, and more.
- Appointment Scheduling: The chatbot assists patients in scheduling or rescheduling appointments with doctors based on their availability.
- Medical Information: Patients can ask CareGenie about medical services, treatment options, and doctor specialties.
- Query Resolution: CareGenie answers general queries such as operating hours, hospital directions, and provides health tips.
- Conversation History: All user interactions with the chatbot are logged for reference and can be reviewed later.
- Data-Driven Responses: CareGenie leverages a machine learning model trained on labeled intents and entities, ensuring accurate and context-aware responses.
---
## Technology Stack
- Natural Language Processing (NLP): The chatbot uses NLP techniques such as tokenization and TF-IDF for text vectorization to understand and classify user queries.
- Machine Learning: A Logistic Regression classifier is employed to predict the appropriate response based on the user input, which is matched to predefined intents.
- Streamlit: A web-based interface is developed using Streamlit, making it easy for users to interact with the chatbot and for hospital administrators to view conversation histories.
- Python Libraries: Key libraries such as nltk, scikit-learn, and streamlit are used to build, train, and deploy the chatbot.
---
## DataSets
- The dataset used in this project is a collection of labelled intents and entities. The data is stored in a list.
- Intents: The intent of the user input (e.g. "Doctor_Query", "booking", "about_medical_services")
- Entities: The entities extracted from user input (e.g. "Hi", "What is timimg of the doctor?", "Booking_slots")
- Text: The user input text.
---
## Project Breakdown
- Data Collection: The chatbot’s functionality is based on a dataset of labeled intents and their corresponding patterns and responses. These intents include medical queries, appointment bookings, and general hospital information.
- Training Model: The model is trained using the labeled data to classify user input into relevant intents, which are then matched with predefined responses.
- User Interface: The chatbot interface is designed to be user-friendly, featuring text inputs and responses, along with a sidebar that provides easy navigation to features such as "Home," "History," and "About."
- Continuous Improvement: The system logs conversations, which allows for future improvements and fine-tuning of the chatbot by analyzing interactions and refining the response model.

## Installation

### 1. Clone the Repository
```bash
git clone <repository-url>
cd <repository-directory>
```

### 2. Create a Virtual Environment (Optional but Recommended)
```bash
python -m venv venv
source venv/bin/activate  # On Windows use `venv\Scripts\activate`
```

### 3. Install Required Packages
```bash
pip install -r requirements.txt
```

### 4. Download NLTK Data
```python
import nltk
nltk.download('punkt')
```

---

## Usage
To run the chatbot application, execute the following command:
```bash
streamlit run app.py
```

Once the application is running, you can interact with the chatbot through the web interface. Type your message in the input box and press Enter to see the chatbot's response.

---

## Intents Data
The chatbot's behavior is defined by the `intents.json` file, which contains various tags, patterns, and responses. You can modify this file to add new intents or change existing ones.

---

## Conversation History
The chatbot saves the conversation history in a CSV file (`chat_log.csv`). You can view past interactions by selecting the "Conversation History" option in the sidebar.

---

## Contributing
Contributions to this project are welcome! If you have suggestions for improvements or features, feel free to open an issue or submit a pull request.

---

## License
This project is licensed under the MIT License. See the [LICENSE](LICENSE) file for details.

---

## Acknowledgments
- **NLTK** for natural language processing.
- **Scikit-learn** for machine learning algorithms.
- **Streamlit** for building the web interface.

---

Replace `<repository-url>` and `<repository-directory>` with the actual URL of your repository and the name of the directory where the project is located. Adjust any sections as necessary to better fit your project's specifics.
