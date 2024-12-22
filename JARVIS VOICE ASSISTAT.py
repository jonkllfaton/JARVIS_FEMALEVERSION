import speech_recognition as sr
import pyttsx3
import datetime
import wikipedia
import webbrowser
import os
import requests
import pyjokes

# Initialize the speech engine
engine = pyttsx3.init()

# Set up the voice properties (optional, you can change voice and speed)
voices = engine.getProperty('voices')
engine.setProperty('voice', voices[1].id)  # Set to male or female voice
engine.setProperty('rate', 150)  # Set speech rate

# Function for text-to-speech (speaking)
def speak(text):
    engine.say(text)
    engine.runAndWait()

# Function for listening to commands via speech recognition
def listen():
    recognizer = sr.Recognizer()
    with sr.Microphone() as source:
        print("Listening...")
        recognizer.adjust_for_ambient_noise(source)  # Adjusting for background noise
        audio = recognizer.listen(source)

    try:
        print("Recognizing...")
        command = recognizer.recognize_google(audio, language="en-US").lower()
        print(f"User said: {command}")
        return command
    except sr.UnknownValueError:
        print("Sorry, I didn't catch that.")
        speak("Sorry, I didn't catch that.")
        return None
    except sr.RequestError:
        print("Sorry, the speech service is down.")
        speak("Sorry, the speech service is down.")
        return None

# Function to check the current time
def get_time():
    time = datetime.datetime.now().strftime("%H:%M:%S")
    speak(f"The current time is {time}")


def get_date():
    date = datetime.datetime.now().strftime("%B %d, %Y")
    speak(f"Today's date is {date}")


def search_wikipedia(query):
    try:
        result = wikipedia.summary(query, sentences=2)
        speak(result)
    except wikipedia.exceptions.DisambiguationError as e:
        speak("There are multiple results, please be more specific.")
    except wikipedia.exceptions.HTTPTimeoutError:
        speak("There was an issue connecting to Wikipedia.")

def search_web(query):
    webbrowser.open(f"https://www.google.com/search?q={query}")
    speak(f"Searching for {query} on the web.")

def open_application(app_name):
    if 'notepad' in app_name:
        speak("Opening Notepad")
        os.system("notepad")
    elif 'calculator' in app_name:
        speak("Opening Calculator")
        os.system("calc")
    else:
        speak(f"Sorry, I don't know how to open {app_name}.")


def tell_joke():
    joke = pyjokes.get_joke()
    speak(joke)

# 
def get_weather(city):
    api_key = "YOUR_API_KEY"  
    url = f"http://api.openweathermap.org/data/2.5/weather?q={city}&appid={api_key}&units=metric"
    response = requests.get(url)
    data = response.json()
    
    if data["cod"] == 200:
        main = data["main"]
        temperature = main["temp"]
        weather = data["weather"][0]["description"]
        speak(f"The weather in {city} is {weather} with a temperature of {temperature}°C.")
    else:
        speak("Sorry, I couldn't retrieve the weather information.")


def execute_command(command):
    if 'hello' in command:
        speak("Hello, I am Jarvis. How can I assist you today?")
    
    elif 'time' in command:
        get_time()
    
    elif 'date' in command:
        get_date()
    
    elif 'wikipedia' in command:
        speak("What do you want to search for on Wikipedia?")
        query = listen()
        if query:
            search_wikipedia(query)
    
    elif 'search' in command:
        speak("What do you want to search on the web?")
        query = listen()
        if query:
            search_web(query)
    
    elif 'open' in command:
        speak("What application would you like to open?")
        app = listen()
        if app:
            open_application(app)
    
    elif 'joke' in command:
        tell_joke()
    
    elif 'weather' in command:
        speak("Which city do you want the weather for?")
        city = listen()
        if city:
            get_weather(city)
    
    elif 'bye' in command:
        speak("Goodbye! Have a nice day.")
        exit()


def main():
    speak("Hello, I am Jarvis. How can I assist you today?")
    while True:
        command = listen()
        if command:
            execute_command(command)

if __name__ == "__main__":
    main()
