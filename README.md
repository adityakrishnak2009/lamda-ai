# Lamda AI

Lamda AI is a Windows desktop assistant with a CustomTkinter chat interface.
It responds to built-in commands for opening websites and local applications,
checking the current time, and searching Wikipedia. It can also speak responses
using Windows text-to-speech.

Despite its name, this project does not connect to a large language model.

## Requirements

- Windows
- Python 3
- The Python packages listed below

Install the dependencies:

```bash
python -m pip install customtkinter pyttsx3 wikipedia requests
```

## Run

From this directory, start the application with:

```bash
python app.py
```

Type a command in the chat box, such as `open google`, `open chatgpt`,
`search Saturn`, or `time`.

## Project files

- `app.py` — desktop chat interface.
- `brain.py` — command handling, website/app launching, Wikipedia lookup, and
  speech output.
- `icon.ico` — application icon.

Some commands in `brain.py` use local Windows paths and may need to be updated
for your computer. The `build`, `dist`, and `__pycache__` folders are generated
artifacts and are not needed to run from source.
