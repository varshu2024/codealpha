import time

def chatbot():
    print("Chatbot: Hello! I am your basic chatbot. Type 'exit' to end the chat.")
    
    while True:
        user_input = input("You: ").lower()
        
        if user_input in ["hello", "hi", "hey"]:
            print("Chatbot: Hi there! How can I help you?")
        elif user_input in ["how are you?", "how are you"]:
            print("Chatbot: I'm just a bot, but I'm doing great! What about you?")
        elif user_input in ["what's your name?", "who are you?"]:
            print("Chatbot: I'm a simple chatbot written in Python!")
        elif user_input in ["bye", "exit", "quit"]:
            print("Chatbot: Goodbye! Have a great day!")
            break
        else:
            print("Chatbot: I'm not sure how to respond to that.")
        
        time.sleep(1)  # Adds a short delay for a better user experience

# Run the chatbot
if __name__ == "__main__":
    chatbot()
