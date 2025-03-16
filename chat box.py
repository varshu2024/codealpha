def chatbot():
    print("Chatbot: Hello! I'm a simple chatbot. How can I help you today?")
    
    while True:
        user_input = input("You: ").lower()

        # Rule 1: Greetings
        if any(word in user_input for word in ["hi", "hello", "hey"]):
            print("Chatbot: Hi there! How can I assist you?")

        # Rule 2: Ask about the chatbot's name
        elif any(word in user_input for word in ["your name", "who are you"]):
            print("Chatbot: I'm just a simple chatbot. You can call me Bot!")

        # Rule 3: Ask how the chatbot is
        elif any(word in user_input for word in ["how are you", "how do you do"]):
            print("Chatbot: I'm just a program, so I don't have feelings, but thanks for asking!")

        # Rule 4: Farewell
        elif any(word in user_input for word in ["bye", "goodbye", "see you"]):
            print("Chatbot: Goodbye! Have a great day!")
            break

        # Rule 5: Default response for unknown inputs
        else:
            print("Chatbot: I'm not sure how to respond to that. Can you try asking something else?")

if __name__ == "__main__":
    chatbot()