import pyttsx3
import webbrowser
import random
import os
import datetime
import wikipedia
import csv
from tracemalloc import stop
import requests

# Initialize once
engine = pyttsx3.init("sapi5")

# Set Microsoft Zira voice
voices = engine.getProperty("voices")

zira_found = False

for voice in voices:
    if "zira" in voice.name.lower():
        engine.setProperty("voice", voice.id)
        zira_found = True
        print(f"Using voice: {voice.name}")
        break

if not zira_found:
    print("Microsoft Zira not found. Using default voice.")

# Optional settings
engine.setProperty("rate", 180)      # Speech speed
engine.setProperty("volume", 1.0)    # Volume (0.0 - 1.0)

def speak(text):
    engine.say(text)
    engine.runAndWait()






def respond_to_command(command):

    command = command.lower()

    if "open google" in command:

        response = "Opening Google..."
        webbrowser.open("https://www.google.com")

    elif "open chatgpt" in command:

        response = "Opening ChatGPT..."
        webbrowser.open("https://chatgpt.com/")


    elif "open youtube" in command:

        response = "Opening YouTube..."
        webbrowser.open("https://www.youtube.com")

    elif "open spotify" in command:

        response = "Opening Spotify..."
        webbrowser.open("https://www.spotify.com")

    elif "open discord" in command:

        response = "Opening Discord..."
        webbrowser.open("https://www.discord.com")  

    elif "open github" in command:

        response = "Opening GitHub..."
        webbrowser.open("https://www.github.com")

    elif "search" in command:

        topic = command.replace("search", "").strip()

        try:
            summary = wikipedia.summary(topic, sentences=2)
            response = f"Wikipedia summary for {topic}: {summary}"
        except Exception as e:
            response = f"Could not fetch Wikipedia summary: {e}"

    elif "open gemini" in command:

        response = "Opening Gemini..."
        webbrowser.open("https://gemini.google.com/")

    elif "open perplexity" in command:

        response = "Opening Perplexity..."
        webbrowser.open("https://www.perplexity.ai/")

    elif "open amazonprime" in command:

        response = "Opening Amazon Prime Video..."
        webbrowser.open("https://net52.cc/home")

    elif "open fl studio" in command:

        fl_path = r"F:\MALAYALAM MOVIE\Flstudio\FL64.exe"

        try:

            os.startfile(fl_path)
            response = "Opening FL Studio..."

        except Exception as e:
            
            response = f"Could not open FL Studio: {e}"


    elif "open roblox" in command:

        response = "Opening Roblox..."
        webbrowser.open("https://www.roblox.com/home")

    elif "play rock paper scissors" in command:

        list1=["rock","paper","scissors"]
        while True:
            user_input=input("Enter rock, paper, or scissors (or 'exit' to quit): ").lower()
            if user_input == "exit":
                print("Thanks for playing! Goodbye!")
                break
            elif user_input not in list1:
                print("Invalid input.")
                continue

            computer_choice = random.choice(list1)
            print(f"Computer chose: {computer_choice}")

            if user_input == computer_choice:
                print("It's a tie!")
            elif (user_input == "rock" and computer_choice == "scissors") or (user_input == "paper" and computer_choice == "rock") or (user_input == "scissors" and computer_choice == "paper"):
                print("You win!")


    elif "play music" in command:

        music_folder = r"F:\fl songs"

        try:
            songs = [
                song for song in os.listdir(music_folder)
                if song.endswith((".mp3", ".wav", ".flac"))
            ]

            if songs:

                song = random.choice(songs)

                song_path = os.path.join(music_folder, song)

                os.startfile(song_path)

                response = f"Playing {song}"

            else:
                response = "No music files found."

        except Exception as e:
            response = str(e)
    
    elif "open netmirror" in command:

        response = "Opening NetMirror..."
        webbrowser.open("https://net22.cc/home")

    elif "open hostinger horizon" in command:

        response = "Opening Hostinger Horizon..."
        webbrowser.open("https://horizon.hostinger.com/")

    elif "open vs code" in command:

        vs_code_path = r"C:\Users\user\AppData\Roaming\Microsoft\Windows\Start Menu\Programs\Visual Studio Code\Visual Studio Code.lnk"

        try:

            os.startfile(vs_code_path)
            response = "Opening Visual Studio Code..."

        except Exception as e:
            
            response = f"Could not open Visual Studio Code: {e}"

    elif "open python" in command:

        python_path = r"C:\Users\user\AppData\Roaming\Microsoft\Windows\Start Menu\Programs\Python 3.13\IDLE (Python 3.13 64-bit).lnk"

        try:

            os.startfile(python_path)
            response = "Opening Python..."

        except Exception as e:
            
            response = f"Could not open Python: {e}"

    elif "open splice" in command:

        splice_path = r"C:\ProgramData\Microsoft\Windows\Start Menu\Programs\Splice\Splice INSTRUMENT.lnk"

        try:

            os.startfile(splice_path)
            response = "Opening Splice..."

        except Exception as e:
            
            response = f"Could not open Splice: {e}"

    elif "open f1 12" in command:

        f1_path = r"F:\F1 2012\F1 2012\F1 2012\f1_2012.exe"

        try:

            os.startfile(f1_path)
            response = "Opening F1 12..."

        except Exception as e:
            
            response = f"Could not open F1 12: {e}"

    elif "open busuu" in command:

        response = "Opening Busuu..."
        webbrowser.open("https://www.busuu.com/")

    elif "open f1 12" in command:

        f1_path = r"F:\F1 2012\F1 2012\F1 2012\f1_2012.exe"

        try:

            os.startfile(f1_path)
            response = "Opening F1 12..."

        except Exception as e:
            
            response = f"Could not open F1 12: {e}"

    elif "exit" in command or "quit" in command:

        response = "Goodbye!"
        exit()

    elif "time" in command:
        now = datetime.datetime.now().strftime("%H:%M")
        response = f"The time is {now}."

    elif "open file" in command or "open folder" in command:
        target = command.replace("open file", "").replace("open folder", "").strip()

        found = False

        drives = ["D:\\", "E:\\", "F:\\"]

        for drive in drives:  

            for root, dirs, files in os.walk(drive):

                for folder in dirs:

                    if target.lower() in folder.lower():

                        folder_path = os.path.join(root, folder)

                        os.startfile(folder_path)

                        response = f"Opening folder {folder}"

                        found = True
                        break
                
                for file in files:

                    if target.lower() in file.lower():

                        file_path = os.path.join(root, file)

                        os.startfile(file_path)

                        response = f"Opening file {file}"

                        found = True
                        break
                if found:
                    break
            if found:
                break
        if not found:
            response = f"Could not find a file or folder matching '{target}'."

    else:
        API_KEY = "aa5e04bcedaee6da14564732d4fc0eb0b69f8d05"  # Replace with your Serper API key

        url = "https://google.serper.dev/search"

        payload = {
            "q": command
        }

        headers = {
            "X-API-KEY": API_KEY,
            "Content-Type": "application/json"
        }

        try:
            response_api = requests.post(
                url,
                json=payload,
                headers=headers,
                timeout=10
            )

            data = response_api.json()

            # Answer Box (if Google provides one)
            if "answerBox" in data:

                answer_box = data["answerBox"]

                title = answer_box.get("title", "")
                answer = (
                    answer_box.get("answer")
                    or answer_box.get("snippet")
                    or ""
                )

                link = answer_box.get("link", "")

                response = f"""{title}

{answer}

Source:
{link}"""

            # Normal Google Search Result
            elif "organic" in data and data["organic"]:

                top_result = data["organic"][0]

                title = top_result.get("title", "")
                snippet = top_result.get("snippet", "")
                link = top_result.get("link", "")

                response = f"""{title}

{snippet}

Source:
{link}"""

            else:
                response = "I couldn't find any search results."

        except Exception as e:
            response = f"Sorry, I couldn't search Google.\n\n{e}"


    speak(response)

    return response






