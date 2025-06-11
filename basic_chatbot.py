def chatbot():
    print("Chatbot: Hello! I'm your simple chatbot. Type 'bye' to exit.")

    while True:
        user_input = input("You: ").lower()

        if user_input in ["hello", "hi"]:
            print("Chatbot: Hi there!")
        elif user_input in ["how are you", "how are you doing"]:
            print("Chatbot: I'm fine, thanks!")
        elif user_input in ["bye", "exit", "quit"]:
            print("Chatbot: Goodbye! Have a great day.")
            break
        else:
            print("Chatbot: Sorry, I didn’t understand that.")

# Run the chatbot
chatbot()
