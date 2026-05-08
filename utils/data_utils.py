import streamlit as st
import pandas as pd
import os
from datetime import datetime
from typing import List, Dict

def load_country_resources() -> pd.DataFrame:
    return pd.DataFrame({
        'Country': ['India', 'United States', 'United Kingdom', 'Australia', 'Canada'],
        'Helpline': ['91-9820466726', '1-800-273-8255', '116 123', '13 11 14', '1-833-456-4566'],
        'Website': ['http://www.aasra.info/', 'https://suicidepreventionlifeline.org', 'https://www.samaritans.org', 'https://www.lifeline.org.au', 'https://www.crisisservicescanada.ca']
    })

def save_conversation(conversation: List[Dict[str, str]]) -> str:
    timestamp = datetime.now().strftime("%Y%m%d_%H%M%S")
    filename = f"conversation_{timestamp}.txt"
    with open(filename, 'w') as f:
        for entry in conversation:
            f.write(f"{entry['role']}: {entry['content']}\n")
    return filename

def get_gemini_api_key() -> str:
    api_key = os.getenv("GEMINI_API_KEY") or st.secrets.get("GEMINI_API_KEY", "")
    if not api_key:
        st.error("GEMINI_API_KEY is not set. Please add it as an environment variable.")
    return api_key

def get_user_age() -> int:
    return st.number_input("What is your age?", min_value=1, max_value=120, value=18, step=1)
