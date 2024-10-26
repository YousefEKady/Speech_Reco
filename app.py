import speech_recognition as sr
import getpass

# Authentication function
def user_auth(name, password):
    user_list = [
        {"username": "Lara", "password": "123456"},
        {"username": "Yousef", "password": "123456"}
    ]
    for user in user_list:
        if user["username"] == name and user["password"] == password:
            return True
    return False

# Speech recognition function
def voice_speech_reco():
    reco = sr.Recognizer()

    # Use Microphone
    with sr.Microphone() as source:
        reco.adjust_for_ambient_noise(source)
        
        # Enter Username and Password
        name = input("What is your username? ")
        password = getpass.getpass("What is your password? ")

        # Check if the user is authenticated
        if user_auth(name, password):
            print(f"Hello {name}, my name is Lara and I am here to help you.")
            
            # Ask if Lara can help
            message = input("Can I help you? (Y/N): ").lower()
            if message == "n":
                print(f"Okay, goodbye {name}!")
            elif message == "y":
                print("Listening... Speak now.")
                while True:
                    audio = reco.listen(source)
                    # Recognize speech
                    try:
                        text = reco.recognize_google(audio).lower()
                        if "hello" in text:
                            print(f"Hello {name}, nice to meet you!")
                        elif "what's your name again" in text:
                            print("My name is Lara.")
                        elif "how are you" in text:
                            print(f"I am fine, thank you {name}.")
                        elif "we have completed the task" in text:
                            print(f"Yes, thank you {name} for creating me.")
                        elif "goodbye" in text or "exit" in text:
                            print(f"Goodbye {name}!")
                            break
                    except sr.UnknownValueError:
                        print("Sorry, I could not understand the audio.")
                    except sr.RequestError:
                        print("Could not request results; check your internet connection.")
            else:
                print("Y or N only!")
        else:
            print("Invalid username or password. Access denied.")

# Run the program
voice_speech_reco()
