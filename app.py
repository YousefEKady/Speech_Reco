import speech_recognition as sr
reco = sr.Recognizer()
# Use Microphone
with sr.Microphone() as source:
    reco.adjust_for_ambient_noise(source)
    # Enter You Name    
    name = input("What Is Your Name? ")
    print(f"Hello {name}, My name is Lara and I am here to help you.")    
    # Ask if Lara can help only once at the start
    message = input("Can I Help You? (Y/N): ").lower()
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
                    print("My Name is Lara")
                elif "how are you" in text:
                    print(f"I am fine thank you {name}")
                elif "we have completed the task" in text:
                    print(f"Yes, Thank you {name} for creating me")
                elif "goodbye" in text or "exit" in text:
                    print(f"Goodbye {name}!")
                    break
            except sr.UnknownValueError:
                print("Sorry, I could not understand the audio.")
            except sr.RequestError:
                print("Could not request results; check your internet connection.")
    else:
        print("Y or N Only")
