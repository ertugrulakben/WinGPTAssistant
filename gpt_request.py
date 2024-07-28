import openai
import pyperclip
import logging
import os
import pyautogui
import time
import requests
from datetime import datetime
import webbrowser
from googlesearch import search

# Logging configuration
log_file_path = os.path.expanduser('C:/Users/your-username/jarvis/gpt_request.log')
logging.basicConfig(filename=log_file_path, level=logging.DEBUG, format='%(asctime)s - %(levelname)s - %(message)s')

# Place your API keys here
openai.api_key = "your-openai-api-key"
weather_api_key = "your-weather-api-key"

# Function to get real-time information
def get_real_time_info():
    """
    Retrieves weather and date information.
    """
    current_date = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    current_day = datetime.now().strftime("%A")
    city = "YOUR-CITY" # Place your
    weather_url = f"http://api.openweathermap.org/data/2.5/weather?q={city}&appid={weather_api_key}&units=metric"
    weather_response = requests.get(weather_url)
    weather_data = weather_response.json()

    if weather_response.status_code == 200:
        temperature = weather_data['main']['temp']
        weather_description = weather_data['weather'][0]['description']
    else:
        temperature = "unknown"
        weather_description = "unknown"

    return current_day, current_date, temperature, weather_description

# Function to make ChatGPT API call
def chatgpt_prompt(prompt, include_real_time_info=False):
    """
    Makes a request to the ChatGPT API and returns the response.
    """
    logging.info('API request initiated')
    try:
        full_prompt = prompt
        if include_real_time_info:
            current_day, current_date, temperature, weather_description = get_real_time_info()
            full_prompt += f"\n\nToday is {current_day}, the date is {current_date}. The weather in Manavgat is {weather_description}, with a temperature of {temperature}°C."

        response = openai.ChatCompletion.create(
            model="gpt-4",  # Specify the model name here
            messages=[
                {
                    "role": "system",
                    "content": (
                        "You are an assistant named XXXX. You will primarily communicate in English. " # Place your NAME
                        "You have information about the user: "
                        "social media consultancy, and advertising. He has received various awards and certifications "
                        "in the field of advertising and digital marketing. "
                    )
                },
                {"role": "user", "content": full_prompt}
            ]
        )
        logging.info('API request completed successfully')
        return response.choices[0].message['content'].strip()
    except Exception as e:
        logging.error(f'Error occurred: {e}')
        return 'An error occurred. Please check the log file.'

# Function to play a song on YouTube
def play_youtube_song(song_name):
    """
    Plays a song on YouTube Music.
    """
    try:
        search_url = f"https://music.youtube.com/search?q={song_name}"
        webbrowser.open(search_url)
        logging.info(f"Playing song on YouTube Music: {song_name}")
    except Exception as e:
        logging.error(f"Error playing song: {e}")

# Function to perform a Google search
def google_search(query):
    """
    Performs a Google search and returns the results.
    """
    try:
        search_results = []
        for result in search(query, num=5, stop=5, pause=2):
            search_results.append(result)
        logging.info(f'Google search results: {search_results}')
        return search_results
    except Exception as e:
        logging.error(f'Error during Google search: {e}')
        return []

# Function to format Google search results
def format_search_results(results, query):
    """
    Formats Google search results.
    """
    formatted_results = f"Searched for {query} on Google, here are some results:\n\n"
    for i, result in enumerate(results, 1):
        formatted_results += f"{i}. {result}\n"
    formatted_results += f"\nFor more information, you can [search for {query} on Google](https://www.google.com/search?q={query}), Ertuğrul abi."
    return formatted_results

if __name__ == "__main__":
    logging.info('Script started')
    try:
        input_text = pyperclip.paste()  # Get text from clipboard
        logging.info(f'Text from clipboard: {input_text}')

        # Check if real-time weather and date info is requested
        include_real_time_info = 'weather' in input_text.lower() or 'date' in input_text.lower()
        
        # Check for play song command
        if any(keyword in input_text.lower() for keyword in ['play song', 'play music', 'start music']):
            song_name = input_text.lower().replace('play song', '').replace('play music', '').replace('start music', '').strip()
            if song_name:
                play_youtube_song(song_name)
                result = f"{song_name} is now playing on YouTube Music."
            else:
                result = "I'm unable to play music. Ertuğrul abi?"
        # Check for Google search command
        elif 'google search' in input_text.lower():
            query = input_text.lower().replace('google search', '').strip()
            search_results = google_search(query)
            result = format_search_results(search_results, query)
        elif 'search images' in input_text.lower():
            query = input_text.lower().replace('search images', '').strip()
            search_url = f"https://www.google.com/search?tbm=isch&q={query}"
            webbrowser.open(search_url)
            result = f"Image search for {query} has been performed on Google."
        elif input_text.lower().startswith('http'):
            webbrowser.open(input_text.strip())
            result = f"{input_text.strip()} URL has been opened."
        else:
            result = chatgpt_prompt(input_text, include_real_time_info)

        logging.info(f'API result: {result}')
        pyperclip.copy(result)  # Copy the result to clipboard
        logging.info('Result copied to clipboard')
        
        # Paste the result
        time.sleep(1)  # Wait for one second
        pyautogui.hotkey('ctrl', 'v')
        logging.info('Result pasted')
        
    except Exception as e:
        logging.error(f'Error occurred: {e}')
