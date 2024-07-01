# AI Voice Assistant

This is an AI Voice Assistant using Python. The assistant can perform various tasks such as greeting the user, searching the web, fetching information from Wikipedia, and more.

## Features

- Voice interaction using `speech_recognition` and `pyttsx3`
- Web searching capabilities with `webbrowser`
- Fetching summaries from Wikipedia using `wikipedia`
- Playing media using `pywhatkit`

## Requirements

Ensure you have the following Python packages installed:

```bash
pip install pyttsx3 wikipedia webbrowser pywhatkit SpeechRecognition
```

## Usage
1. Clone the Repository
  ```bash
git clone <repository-url>
```
2. Navigate to the project directory
```bash
cd <repository-directory>
```
3. Run the script
```bash
python <script-name>.py
```

## Code Explaination
The code initializes a text-to-speech engine and sets up a speech recognizer. It defines several functions:

- `speak(audio):` Converts text to speech.
- `wish_me():` Greets the user based on the current time.
- `take_command():` Listens for the user's voice command and recognizes it using Google Speech Recognition.

### The main script starts by greeting the user and then enters a loop to continually listen for commands. Depending on the command, it can:

- Greet the user
- Provide information about itself
- Search Wikipedia
- Open Google
- Perform specific searches on Google or YouTube
- Close the browser
- Example Commands
    "Alexa, who are you?"
    "What is Python programming?"
    "Just open google"
    "Open google and search for AI"
    "Search on YouTube for Python tutorials"
    "Close browser"
  
## Note
Make sure your microphone is properly set up and working before running the script.

