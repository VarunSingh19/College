# ChatBot

import datetime

# Define a dictionary with predefined responses
responses = {
    "hello": "Hello! How can I assist you?",
    "how are you": "I'm just a computer program, but thanks for asking!",
    "bye": "Goodbye! Have a great day.",
    "what's your name": "I'm a chatbot.",
    "who created you": "I was created by a developer.",
    "tell me a joke": "Why did the computer catch a cold? Because it had too many windows open!",
    "what's the weather like today": "I'm sorry, I don't have access to real-time data.",
    "favorite color": "I don't have preferences, but I like all colors!",
    "tell me a fun fact": "A group of flamingos is called a 'flamboyance.'",
    "how old are you": "I'm ageless, just like the internet.",
}

while True:
    user_input = input("You: ")
    if user_input == 'quit':
        break
    response = responses.get(user_input, responses[user_input])
    current_time = datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    print("Chatbot:", response)
    print("Timestamp:", current_time)
