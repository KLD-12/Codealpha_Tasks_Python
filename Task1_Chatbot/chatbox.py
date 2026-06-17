def get_response(user_input):
    text = user_input.lower().strip()

    if text in ["hello", "hi", "hey"]:
        return "Hello! Welcome! How can I help you today? "
    
    elif text in ["how are you", "how are you?", "how r u", "how do you do"]:
        return "I'm doing great, thank you for asking! How about you?"

    elif text in ["fine", "good", "great", "i'm fine", "i'm good", "doing well"]:
        return "Glad to hear that! 😄 Is there anything I can help you with?"

    elif text in ["what's your name", "what is your name", "who are you", "your name?"]:
        return "I'm ChatBot — your friendly themed digital assistant! "

    elif text in ["what can you do", "help", "what do you do"]:
        return ("Here's what I can talk about:\n"
                "  • hello / hi\n"
                "  • how are you\n"
                "  • tell me a joke\n"
                "  • ipl / cricket\n"
                "  • capital of india\n"
                "  • indian food / tea\n"
                "  • bye")

    elif text in ["tell me a joke", "joke", "say something funny", "funny"]:
        return ("A programmer told his mom:\n"
                "  'Mom, give me a glass of water!'\n"
                "  Mom: 'Finish your homework first!'\n"
                "  Programmer: 'Mom, I am stuck in an infinite loop!' ")

    elif text in ["cricket", "ipl", "india cricket"]:
        return ("Cricket is India's religion! 🏏🇮🇳\n"
                "  • Team India is consistently ranked among the top in ICC rankings.\n"
                "  • IPL is the world's biggest T20 league.\n"
                "  • MS Dhoni ,Sachin Tendulkar , Virat Kohli and Rohit Sharma are legends of the game!")

    elif text in ["capital of india", "what is the capital of india", "india capital"]:
        return "New Delhi is the capital of India! "


    elif text in ["india population", "population of india"]:
        return "India is the most populous country in the world with over 1.4 billion people!"

    elif text in ["india currency", "indian currency", "what is rupee", "rupee"]:
        return "India's currency is the Indian Rupee (₹ / INR)"

    elif text in ["languages in india", "india languages", "how many languages"]:
        return ("India has 22 officially recognized languages!\n"
                "  Hindi and English are used for official government work.\n"
                "  Some popular ones: Tamil, Hindi, Malayalam, Bengali, Telugu, Marathi, Gujarati.️")

    elif text in ["indian food", "food", "favourite food", "best food"]:
        return ("Indian food is the best!️\n"
                "  Some favourites: Biryani, Butter Chicken, Masala Dosa,\n"
                "  Pani Puri, Chat items, and of course — Tea! ")

    elif text in ["chai", "tea", "lemon tea"]:
        return "Nothing beats a hot lemon tea on a rainy day! "

    elif text in ["bye", "goodbye", "exit", "quit", "see you", "see ya"]:
        return "Goodbye! Have a wonderful day! 👋🇮🇳"

    else:
        return ("Sorry, I didn't understand that. \n"
                "Type 'help' to see what I can respond to.")


def main():
    print("=" * 50)
    print("  ChatBot  ")
    print("  Hello! I'm your assistant.")
    print("  (type 'bye' or 'exit' to quit)")
    print("=" * 50)

    while True:
        user_input = input("\nYou: ").strip()

        if not user_input:
            print("Bot: Please type something! I'm listening. ")
            continue

        response = get_response(user_input)
        print(f"Bot: {response}")

        if user_input.lower().strip() in ["bye", "goodbye", "exit", "quit"]:
            break


if __name__ == "__main__":
    main()
