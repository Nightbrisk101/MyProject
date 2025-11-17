# modules of: main.py; modules required for the program to run and to interact with OpenAI's API, in order to run, user needs to have openai and python-dotenv installed, as well as having a .env file with their OpenAI API key specifically with, "OPENAI_API_KEY="your_openai_api_key_here""
import os
import time
import sys
from dotenv import load_dotenv
from openai import OpenAI

# Load environment variables from .env, specifically the OPENAI_API_KEY
load_dotenv()

# Initializes OpenAI client
client = OpenAI(api_key=os.getenv("OPENAI_API_KEY"))

def type_FX(text, speed=0.01):
    """Print text with a typing effect."""
    for char in text:
        print(char, end="", flush=True)
        time.sleep(speed)
    print()  # Just a newline at the end why not, and to ensure the cursor goes to the next line, and cleaner too, why not

# Main chatbot function, where the interaction happens, how the whole program works, without this function the program wouldn't run
def chatbot():
    # Asks the user to begin
    name = input("Enter Your Name: ")
    print(f"\nStory Teller: Hello {name}! Ready to begin?\n")

# Main loop for user interaction
    while True:
        user_input = input(f"\n{name}: ")
        if user_input.lower() in ["leave", "goodbye", "bye", "exit"]:
            print(f"Story Teller: Goodbye, {name}!")
            break

        # Show message that story generation is in progress, just a cool detail because why not
        print("\nStory Teller: Story Generation in Progress...", end="", flush=True)

        # Utilize OpenAI's chat completion endpoint, as well as the gpt-4o-mini model
        response = client.chat.completions.create(
            model="gpt-4o-mini",
            messages=[
                {"role": "system", "content": f"You are a story teller that tells a story with 10 endings, that takes place in a haunted manor with 5 friends, and in the haunted house there are spooky things and horror stories throughout the story, and throughout the story the user makes choices which leads to their fate on what ending they get, the user play alongs with the story, it is an interactive story, and always refer to the user as {name}."}, # This gives the AI a persona to act as, in this case, a story teller
                {"role": "user", "content": user_input} # The user's input that the AI will respond to
            ]
        )

        # Clear the Show message that story generation is in progress line
        sys.stdout.write("\r" + " " * 50 + "\r")  # overwrite line with spaces

        # Get the response from Openai so the ai can reply to the user
        reply = response.choices[0].message.content

        # Print the response of the ai
        print("\nStory Teller: ", end="", flush=True)
        type_FX(reply, speed=0.01) # Typing effect for the response, cool feature because why not

# Run the chatbot function if this script is executed directly
if __name__ == "__main__":
    chatbot()
