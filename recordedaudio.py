import getpass
import torch
from transformers import pipeline
from pydub import AudioSegment

# Authentication function
def user_auth(name, password):
    user_list = [
        {"username": "Lara", "password": "123456", "role": "admin"},
        {"username": "Yousef", "password": "123456", "role": "user"}
    ]
    for user in user_list:
        if user["username"] == name and user["password"] == password:
            print(f"You are granted access as a {user['role']}.")
            return user["role"]
    return None

# Function to transcribe audio files
def transcribe_audio_file(audio_path):
    # Load the audio file and convert it to the required format
    audio = AudioSegment.from_file(audio_path)
    audio = audio.set_frame_rate(16000).set_channels(1)  # ensure compatibility with the model

    # Initialize the speech recognition pipeline
    recognizer = pipeline("automatic-speech-recognition", model="openai/whisper-small")

    # Convert audio to bytes for the pipeline
    audio_bytes = audio.raw_data
    transcription = recognizer(audio_bytes)["text"]

    return transcription

# Function to interact based on transcription
def interact_with_transcription(transcription, username):
    transcription = transcription.lower()
    
    # Respond to the transcribed text
    if "hello" in transcription:
        print(f"Hello {username}, nice to meet you!")
    elif "what's your name again" in transcription:
        print("My name is Lara.")
    elif "how are you" in transcription:
        print(f"I am fine, thank you {username}.")
    elif "we have completed the task" in transcription:
        print(f"Yes, thank you {username} for creating me.")
    elif "goodbye" in transcription or "exit" in transcription:
        print(f"Goodbye {username}!")
    else:
        print("I'm here to help. Could you clarify what you need?")

# Main function
def main():
    # Enter Username and Password
    name = input("What is your username? ")
    password = getpass.getpass("What is your password? ")

    # Check if the user is authenticated
    role = user_auth(name, password)
    if role:
        print(f"Hello {name}, my name is Lara and I am here to help you.")
        
        # Ask if Lara can help
        message = input("Can I help you? (Y/N): ").lower()
        if message == "n":
            print(f"Okay, goodbye {name}!")
        elif message == "y":
            # Select an audio file for processing
            audio_path = input("Please provide the path to the audio file: ")
            try:
                # Transcribe the audio file and interact
                transcription = transcribe_audio_file(audio_path)
                print(f"Transcription: {transcription}")
                interact_with_transcription(transcription, name)
            except Exception as e:
                print(f"An error occurred while processing the audio file: {e}")
        else:
            print("Y or N only!")
    else:
        print("Invalid username or password. Access denied.")

# Run the program
main()
