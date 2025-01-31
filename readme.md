# Emotional Support ChatBot

Emotional Support ChatBot is a mental health support chatbot built with Streamlit and powered by Google's Gemini AI. It provides a compassionate and helpful interface for users seeking emotional support and mental health resources.

## Features

- Personalized greetings
- Mood tracking
- Intent analysis
- Crisis detection
- Contextual responses
- Mental health resources by country
- Conversation saving

## Installation

1. **Download and Install Python:**

   Ensure you have the last Python version installed. If not, download and install it from Python's official website. For detailed instructions, refer to the tutorials:

   - [How to Install Python on Windows](https://www.geeksforgeeks.org/how-to-install-python-on-windows/)
   - [How to Install Python on Linux](https://www.geeksforgeeks.org/how-to-install-python-on-linux/)
   - [How to Download and Install Python on macOS](https://www.geeksforgeeks.org/how-to-download-and-install-python-latest-version-on-macos-mac-os-x/)

1.a) **Download and Install Google Chrome:**

- Download and install the latest version of Google Chrome from its default location on the [official website](https://www.google.com/chrome).

2. Clone the repository:

   ```
   git clone https://github.com/PREMSAITEJA/Emotional-Support-ChatBot.git

   cd Emotional-Support-ChatBot
   ```

3. **Activate virtual environment:**

   For Unix-based machines -

   ```bash
   python3 -m venv virtual
   ```

   ```bash
   source virtual/bin/activate
   ```

   or for Windows-based machines -

   ```bash
   .\virtual\Scripts\activate
   ```

4. **Install the required packages:**

   Before installing the required packages, make sure to install https://visualstudio.microsoft.com/visual-cpp-build-tools/ and select "Desktop development with C++".

   ```bash
   pip install -r requirements.txt
   ```

5. Download the spaCy model:

   ```
   pip install --upgrade pip
   pip install -r requirements.txt
   python -m spacy download en_core_web_sm
   ```

6. Set up your Google Gemini API key:
   - Sign up for a Google Cloud account and obtain an API key for the Gemini API.
   - You'll be prompted to enter this key when running the application.

## Usage

Run the main application:

```
streamlit run main.py

```
