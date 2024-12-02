import os
import json
import datetime
import csv
import nltk
import ssl
import streamlit as st
import random
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.linear_model import LogisticRegression

ssl._create_default_https_context = ssl._create_unverified_context
nltk.data.path.append(os.path.abspath("nltk_data"))
nltk.download('punkt')

file_path = os.path.abspath("./intents.json")
with open(file_path, "r") as file:
    intents = json.load(file)

vectorizer = TfidfVectorizer(ngram_range=(1, 4))
clf = LogisticRegression(random_state=0, max_iter=10000)

tags = []
patterns = []
for intent in intents:
    for pattern in intent['patterns']:
        tags.append(intent['tag'])
        patterns.append(pattern)

# training the model
x = vectorizer.fit_transform(patterns)
y = tags
clf.fit(x, y)


st.markdown(
    """
    <style>
    [data-testid="stAppViewContainer"] {
        background: linear-gradient(120deg, #1e3c72, #2a5298, #0f2027);
        background-size: 400% 400%;
        animation: gradientShift 10s ease infinite;
        height: 100vh;
        padding: 0;
        margin: 0;
    }
    @keyframes gradientShift {
        0% { background-position: 0% 50%; }
        50% { background-position: 100% 50%; }
        100% { background-position: 0% 50%; }
    }
    @media (max-width: 768px) {
        [data-testid="stAppViewContainer"] {
            background: linear-gradient(120deg, #6a11cb, #2575fc);
        }
    }
    </style>
    """,
    unsafe_allow_html=True
)

st.markdown(
    """
    <style>
    [data-testid="stSidebar"] {
        background: linear-gradient(90deg, rgba(0, 36, 61, 1) 0%, rgba(0, 128, 255, 0.9) 50%, rgba(0, 212, 255, 1) 100%);
        color: smoke;
        animation: pulse 3s infinite;
        padding: 20px;
    }
    @keyframes pulse {
        0% { background-color: rgba(0, 128, 255, 0.9); }
        50% { background-color: rgba(0, 212, 255, 1); }
        100% { background-color: rgba(0, 128, 255, 0.9); }
    }
    .emoji {
        font-size: 3.5rem;
        margin-right: 10px;
        animation: bounce 1.5s infinite;
    }
    @keyframes bounce {
        0%, 20%, 50%, 80%, 100% { transform: translateY(0); }
        40% { transform: translateY(-10px); }
        60% { transform: translateY(-5px); }
    }
    </style>
    """,
    unsafe_allow_html=True
)

# st.markdown(
#     """
#     <style>
#     [data-testid="stSidebar"] {
#         background: linear-gradient(90deg, rgba(169, 241, 182, 1) 0%, rgba(255, 239, 153, 1) 100%);
#         color: black;
#         animation: pulse 3s infinite;
#         padding: 20px;
#     }
#     @keyframes pulse {
#         0% { background-color: rgba(169, 241, 182, 1); }
#         50% { background-color: rgba(255, 239, 153, 1); }
#         100% { background-color: rgba(169, 241, 182, 1); }
#     }
#     .emoji {
#         font-size: 3.5rem;
#         margin-right: 10px;
#         animation: bounce 1.5s infinite;
#     }
#     @keyframes bounce {
#         0%, 20%, 50%, 80%, 100% { transform: translateY(0); }
#         40% { transform: translateY(-10px); }
#         60% { transform: translateY(-5px); }
#     }
#     </style>
#     """,
#     unsafe_allow_html=True
# )
# st.sidebar.markdown("""🚀 The CareGenie Chatbot""")
st.sidebar.markdown('<div class="pink-subheader">🚀 CareGenie</div>', unsafe_allow_html=True)
st.sidebar.markdown('<div class="yel-col">✨ KeyFeatures</div>', unsafe_allow_html=True)
st.sidebar.markdown("""
- 🏠 **Home**: Chat with CareGenie.  
- 📜 **History**: View previous conversations.  
- ℹ️ **About**: Learn about the project.
""")


st.markdown(
    """
    <style>
    .yel-col{
        color:yellow;
        font-weight: bold;
        font-size: 1.0rem;
        # animation: glow 1.5s infinite;
        align-content: center;
    }
    
    .pink-subheader {
        color: pink;
        font-weight: bold;
        font-size: 1.5rem;
        animation: glow 1.5s infinite;
        align-content: center;
    }
    .yellow-subheader {
        color: yellow;
        font-weight: bold;
        font-size: 1.5rem;
        animation: glow 1.5s infinite;
    }

    @keyframes glow {
        0% {
            text-shadow: 0 0 5px #ffd700, 0 0 10px #ffd700, 0 0 15px #ffd700;
        }
        50% {
            text-shadow: 0 0 10px #ffd700, 0 0 20px #ffd700, 0 0 30px #ffd700;
        }
        100% {
            text-shadow: 0 0 5px #ffd700, 0 0 10px #ffd700, 0 0 15px #ffd700;
        }
    }
    </style>
    """,
    unsafe_allow_html=True
)


st.markdown(
    """
    <style>
    .animated-heading {
        position:relative;
        font-size: 2.0rem;
        font-weight: bold;
        color: red;
        left:100px;
        text-shadow: 2px 2px 5px rgba(0, 0, 0, 0.3);
        animation: slideIn 3s ease-in-out infinite alternate;
    }

    @keyframes slideIn {
        0% {
            transform: translateX(-10px);
            color: #f39c12;
        }
        50% {
            transform: translateX(10px);
            color: #e74c3c;
        }
        100% {
            transform: translateX(-10px);
            color: #3498db;
        }
    }
    </style>
    """,
    unsafe_allow_html=True
)

st.markdown('<h1 class="animated-heading">Welcome to CareGenie Chatbot 🤖</h1>', unsafe_allow_html=True)

st.markdown(
    """
    <style>
    .blinking-heading {
        font-size: 2.5rem;
        font-weight: bold;
        text-align: center;
        color: #7CFC00;
        animation: blink 1.5s steps(2, start) infinite;
    }

    @keyframes blink {
        0%, 100% { visibility: visible; }
        50% { visibility: hidden; }
    }
    </style>
    """,
    unsafe_allow_html=True
)

# Add the animated heading
st.markdown('<h1 class="blinking-heading">CareGenie-The Hospital Management ChatBot🏥</h1>', unsafe_allow_html=True)


def chatbot(input_text):
    input_text = vectorizer.transform([input_text])
    tag = clf.predict(input_text)[0]
    for intent in intents:
        if intent['tag'] == tag:
            response = random.choice(intent['responses'])
            return response
        
counter = 0

def main():
    global counter
    #menu
    menu = ["Home", "History", "About"]
    choice = st.sidebar.selectbox("Menu", menu)
    # Home Menu
    if choice == "Home":
        st.markdown(
        """
        <style>
        .marquee {
            text-align: center;
            font-size: 1.2rem;
            font-weight: bold;
            color: #ff0000;
            padding: 10px;
            border-radius: 5px;
            animation: scroll 10s linear infinite;
            # animation: glow 1.5s infinite;
        }

        @keyframes scroll {
            0% { transform: translateX(100%); }
            100% { transform: translateX(-100%); }
        }
        </style>
        <div class="marquee">
            Please type a message and press Enter to start the conversation.
        </div>
        """,
        unsafe_allow_html=True
        )

        if not os.path.exists('chat_log.csv'):
            with open('chat_log.csv', 'w', newline='', encoding='utf-8') as csvfile:
                csv_writer = csv.writer(csvfile)
                csv_writer.writerow(['User Input', 'Chatbot Response', 'Timestamp'])

        counter += 1
        user_input = st.text_input("User:", key=f"user_input_{counter}")

        if user_input:

            # Convert the user input to a string
            user_input_str = str(user_input)

            response = chatbot(user_input)
            st.text_area("Chatbot:", value=response, height=120, max_chars=None, key=f"chatbot_response_{counter}")

            # Get the current timestamp
            timestamp = datetime.datetime.now().strftime(f"%Y-%m-%d %H:%M:%S")

            # Save the user input and chatbot response to the chat_log.csv file
            with open('chat_log.csv', 'a', newline='', encoding='utf-8') as csvfile:
                csv_writer = csv.writer(csvfile)
                csv_writer.writerow([user_input_str, response, timestamp])

            if response.lower() in ['goodbye', 'bye']:
                st.write("Thank you for chatting with me. Have a great day!")
                st.stop()

    elif choice == "History":
        st.markdown('<div class="yellow-subheader">Conversation History</div>', unsafe_allow_html=True)
        with open('chat_log.csv', 'r', encoding='utf-8') as csvfile:
            csv_reader = csv.reader(csvfile)
            next(csv_reader) 
            for row in csv_reader:
                st.text(f"User: {row[0]}")
                st.text(f"Chatbot: {row[1]}")
                st.text(f"Timestamp: {row[2]}")
                st.markdown("---")

    elif choice == "About":
        st.write("CareGenie is a sophisticated chatbot designed to enhance hospital management systems by providing an intuitive, automated interface to streamline communication between patients, healthcare providers, and hospital administrators. By utilizing Natural Language Processing (NLP) and machine learning techniques, CareGenie understands and responds to user queries, providing personalized and efficient services such as appointment scheduling, medical inquiries, and general hospital information.")

        st.markdown('<div class="yellow-subheader">Project Features</div>', unsafe_allow_html=True)


        st.write("""
        Core Features:
        1. Patient Interaction: CareGenie interacts with patients to answer questions related to hospital services, doctor availability, appointment booking, medical record queries, and more.
        2. Appointment Scheduling: The chatbot assists patients in scheduling or rescheduling appointments with doctors based on their availability.
        3. Medical Information: Patients can ask CareGenie about medical services, treatment options, and doctor specialties.
        4. Query Resolution: CareGenie answers general queries such as operating hours, hospital directions, and provides health tips.
        5. Conversation History: All user interactions with the chatbot are logged for reference and can be reviewed later.
        6. Data-Driven Responses: CareGenie leverages a machine learning model trained on labeled intents and entities, ensuring accurate and context-aware responses.
        """)

        st.write("""
        Technology Stack:
        1. Natural Language Processing (NLP): The chatbot uses NLP techniques such as tokenization and TF-IDF for text vectorization to understand and classify user queries.
        2. Machine Learning: A Logistic Regression classifier is employed to predict the appropriate response based on the user input, which is matched to predefined intents.
        3. Streamlit: A web-based interface is developed using Streamlit, making it easy for users to interact with the chatbot and for hospital administrators to view conversation histories.
        4. Python Libraries: Key libraries such as nltk, scikit-learn, and streamlit are used to build, train, and deploy the chatbot.
        """)
    
        st.markdown('<div class="yellow-subheader">DataSets</div>', unsafe_allow_html=True)


        st.write("""
        The dataset used in this project is a collection of labelled intents and entities. The data is stored in a list.
        - Intents: The intent of the user input (e.g. "Doctor_Query", "booking", "about_medical_services")
        - Entities: The entities extracted from user input (e.g. "Hi", "What is timimg of the doctor?", "Booking_slots")
        - Text: The user input text.
        """)
        st.markdown('<div class="yellow-subheader">Project Breakdown</div>', unsafe_allow_html=True)


        st.write("""
        - Data Collection: The chatbot’s functionality is based on a dataset of labeled intents and their corresponding patterns and responses. These intents include medical queries, appointment bookings, and general hospital information.
        - Training Model: The model is trained using the labeled data to classify user input into relevant intents, which are then matched with predefined responses.
        - User Interface: The chatbot interface is designed to be user-friendly, featuring text inputs and responses, along with a sidebar that provides easy navigation to features such as "Home," "History," and "About." 
        - Continuous Improvement: The system logs conversations, which allows for future improvements and fine-tuning of the chatbot by analyzing interactions and refining the response model.
        """)

        st.markdown('<div class="yellow-subheader">Potential Extensions/Applications</div>', unsafe_allow_html=True)

        st.write("""
        1. Integration with Hospital Databases: The chatbot could be enhanced to interact with hospital management software to check real-time doctor availability and patient medical records.
        2. Voice Support: Adding voice-based interactions could make the chatbot more accessible to a broader audience, including elderly patients.
        3. Advanced NLP Models: Moving beyond Logistic Regression to more sophisticated deep learning models for improved accuracy and flexibility in understanding complex queries.
        """)



        st.markdown('<div class="yellow-subheader">Conclusion</div>', unsafe_allow_html=True)
        st.write("CareGenie offers a smart, efficient, and user-friendly solution for hospital management. By incorporating AI-powered chatbots, healthcare institutions can improve patient experiences, streamline administrative tasks, and create a more responsive environment for both patients and healthcare providers. This project demonstrates the power of AI and machine learning in healthcare technology, with potential for further innovation and scalability.")

        st.write("Created By-Vivek Lokolakar")

if __name__ == '__main__':
    main()
