# Install the SpeechRecognition library if you haven't already
# Run: pip install SpeechRecognition

import speech_recognition as sr

def main():
    # Initialize the recognizer
    recognizer = sr.Recognizer()

    # Capture audio from the microphone
    with sr.Microphone() as source:
        print("Speak now...")
        try:
            audio = recognizer.listen(source, timeout=5)  # Record for 5 seconds
            print("Recording complete. Recognizing...")

            # Recognize the speech
            recognized_text = recognizer.recognize_google(audio)
            print(f"Recognized text: {recognized_text}")

            # You can now use 'recognized_text' in your Hanuman Chalisa project
            # Display it or perform any other action as needed.
        except sr.WaitTimeoutError:
            print("No speech detected. Please try again.")

if __name__ == "__main__":
    main()
