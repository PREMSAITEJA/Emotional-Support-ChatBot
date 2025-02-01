mkdir -p ~/.streamlit/

echo "\
[server]\n\
headless = true\n\
port = $PORT\n\
enableCORS = false\n\
\n\
" > ~/.streamlit/config.toml

# Install build tools
sudo apt-get update
sudo apt-get install -y build-essential

# Install dependencies
pip install -r requirements.txt
