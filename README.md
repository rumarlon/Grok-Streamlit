# Grok-Streamlit
_Get Started with Grok_

*tl:dr* This is a simple implementation of Streamlit for Grok. This is not a production app but rather it provides an opportunity to explore Grok capabilities.  There are currently two paths to implement Grok API access, OpenAI SDK or Anthropic SDK. This app was built leveraging OpenAI SDK.

This app leverages Streamlit, feel free to checkout their docs and other examples [here](https://streamlit.io).

## Setup requirements as tested:

1) MacOS Sequoia 
2) Python 3.12.4
3) Grok API Key (sign up and get one at [Grok Console](https://console.x.ai/) as of 11/24 you get a free $25 credit monthly until 1/25)

### Step by step

1) Clone this repo
2) Create python environment
```
python -m venv venv
```
3) Activate python environment
```
source venv/bin/activate
```
4) Install requirements
```
pip install -r requiremnts.txt
```
5) Paste your key in `.streamlit/secrets.toml` 
```
XAI_API_KEY="xai-restofyourkey"
```
6) Run your app
```
streamlit run main.py
```
7) Your browser should open with a working streamlit app.
8) Try a user prompt example, "What is the meaning of life, the universe, and everything?"

## What to do next?

Go ahead and change the system prompt and see what you can do with Grok. The prompt is in the [main.py](https://github.com/rumarlon/Grok-Streamlit/blob/master/main.py). Sky is the limit!

From:
```
{"role": "system", "content": "You are Grok, a chatbot inspired by the Hitchhikers Guide to the Galaxy."}
```
To:
```
{"role": "system", "content": "Your new prompt goes here"}
```

## Troubleshooting

If you get an API access error make sure you have a valid Grok API key and that the key is properly pasted in `.streamlit/secrets.toml`.

