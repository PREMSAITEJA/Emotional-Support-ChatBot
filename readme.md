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

1. Clone the repository:

   ```
   git clone https://github.com/PREMSAITEJA/Emotional-Support-ChatBot.git

   cd Emotional-Support-ChatBot
   ```
2. Create a Virtual Environment and Activate it:

   ```
   python -m venv myenv
`
   Windows:
```
   myenv\Scripts\activate && source myenv/Scripts/activate

```
   Linux /MacOs/ githubCodespaces:
```
   source myenv/bin/activate
```
   


3. Install the required dependencies:

   ```
   pip install -r requirements.txt
   ```

4. Download the spaCy model:

   ```
   python -m spacy download en_core_web_sm
   ```

5. Set up your Google Gemini API key:
   - Sign up for a Google Cloud account and obtain an API key for the Gemini API.
   - You'll be prompted to enter this key when running the application.

## Usage

Run the main application:

```
streamlit run main.py

```
