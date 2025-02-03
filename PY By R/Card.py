def create_greeting_card():
    # Get user input for name and age
    name = input("Enter your name: ")
    age = input("Enter your age: ")

    # Create a personalized greeting message
    greeting_message = f"🎉 Happy Day! 🎉\n"
    greeting_message += f"Dear {name},\n"
    greeting_message += f"Congratulations on reaching {age} years of wisdom!\n"
    greeting_message += "Wishing you all the happiness and success in the year ahead.\n"
    greeting_message += "Enjoy your special day to the fullest!\n"
    greeting_message += "Best wishes, \nYour Virtual Friend 😊"

    # Print the greeting card
    print("\n" + "=" * 40)  # Divider
    print(greeting_message)
    print("=" * 40)


# Run the function
if __name__ == "__main__":
    create_greeting_card()
