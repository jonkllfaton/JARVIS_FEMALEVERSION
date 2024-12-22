# Project

Project Description: Voice-Activated Assistant (Jarvis)
This project aims to build a basic voice assistant, modeled after the AI system "Jarvis" from popular culture, which responds to user voice commands and performs various tasks such as checking the time, date, weather, telling jokes, searching the web, opening applications, and interacting with Wikipedia. The assistant is built using Python and integrates various libraries for speech recognition, text-to-speech, and internet access to gather data.

Key Features:
Voice Commands and Responses: The assistant listens to commands through the microphone and provides spoken responses.
Speech-to-Text (STT): Converts user speech into text, allowing the assistant to understand commands.
Text-to-Speech (TTS): Speaks the responses back to the user.
Time and Date Information: Retrieves the current time and date.
Wikipedia Search: Searches Wikipedia and returns brief summaries of requested topics.
Web Search: Opens Google search results for user queries.
Opening Applications: Opens commonly used applications (like Notepad or Calculator) via voice commands.
Weather Information: Fetches the current weather of a specified city using the OpenWeatherMap API.
Jokes: Provides a random joke from the pyjokes library.
Implementation Details:
1. Libraries Used:
speech_recognition: Used for capturing voice input and converting it into text.
pyttsx3: A text-to-speech library that converts the text into speech, which the assistant uses to speak responses.
datetime: Used to get the current time and date.
wikipedia: Allows the assistant to fetch summaries of Wikipedia articles.
webbrowser: Opens a web browser to perform Google searches based on user queries.
os: Used for opening applications like Notepad or Calculator on the system.
requests: Used to fetch weather data from the OpenWeatherMap API.
pyjokes: Fetches a random joke and speaks it aloud.
2. Functions:
speak(text): This function uses pyttsx3 to speak the text passed to it. It’s used throughout the program to give voice feedback to the user.

listen(): Uses the speech_recognition library to capture and recognize user voice commands. It listens to ambient noise, processes the audio, and converts it to text. If the recognition fails, it prompts the user again.

get_time(): Uses datetime to fetch the current system time and speaks it aloud.

get_date(): Uses datetime to fetch the current date and speaks it aloud.

search_wikipedia(query): Takes a user query, searches Wikipedia using the wikipedia library, and returns a brief summary of the topic.

search_web(query): Opens a web browser and searches for the query on Google using the webbrowser library.

open_application(app_name): Opens common applications like Notepad or Calculator based on the voice command received. It can be expanded to open other applications.

tell_joke(): Fetches a random joke from the pyjokes library and speaks it aloud.

get_weather(city): Uses the OpenWeatherMap API to get the weather information for a specified city. The API key is required for this function to work (replace "YOUR_API_KEY" with a valid API key).

execute_command(command): The core function that processes the user command and determines which action to perform based on the recognized speech. It checks if the command contains keywords like "hello", "time", "weather", "wikipedia", etc., and calls the corresponding function.

3. Main Loop:
The main() function is the entry point. It initiates the assistant by greeting the user and entering an infinite loop to continuously listen for commands. As long as valid commands are received, the assistant executes them. If the user says "bye", the program exits.

Code Walkthrough:
Speech Initialization:

The pyttsx3.init() method initializes the text-to-speech engine.
The voice is set to a female or male voice, and the rate of speech is set to 150 words per minute (this can be adjusted).
Listening for Commands:

The listen() function listens to the user's voice using the microphone, converts the audio to text using Google’s speech recognition service, and returns the recognized command.
If recognition fails (e.g., due to background noise), it handles the error gracefully by prompting the user again.
Handling Commands:

In the execute_command(command) function, the program checks the command string for certain keywords like "time", "weather", "open", etc., and calls the appropriate function.
If the command requires a follow-up query (like searching Wikipedia or asking for weather details), the assistant listens again and processes the new query.
Weather Feature:

The assistant uses the requests library to get real-time weather data from the OpenWeatherMap API. The user provides a city name, and the assistant fetches the temperature and weather description.
You need to replace "YOUR_API_KEY" with your actual OpenWeatherMap API key.
Search Features:

The assistant can search the web by opening a Google search in the browser and also fetch articles from Wikipedia using the wikipedia library.
Joke Feature:

The assistant can tell jokes fetched from the pyjokes library, which are returned as text and spoken aloud.
Application Opening:

If the user asks to open applications like Notepad or Calculator, the assistant uses the os.system() function to open these apps.
You Use For Free! Enjoy!
