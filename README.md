# Grok-Streamlit
_Get Started with Grok_

*tl:dr* This is a simple implementation of Streamlit for Grok. This is not a production app but rather it provides an opportunity to explore Grok capabilities with a local app that calls the Grok API.  There are currently two SDKs to implement Grok API access, OpenAI SDK or Anthropic SDK. This app was built leveraging OpenAI SDK.

*New Feature:* You can now use `grok-vision-beta` which supports both text and image input ([main-vision.py](https://github.com/rumarlon/Grok-Streamlit/blob/master/main-vision.py)).

The following instructions will help you deploy a Streamlit app in a python environment on your Mac, feel free to checkout their docs and other examples [here](https://streamlit.io).

### Setup requirements as tested:

* MacOS Sequoia 
* Python 3.12.4
* Grok API Key - Do not commit this in your code or share with others unintetionally. (sign up and get one at [Grok Console](https://console.x.ai/) as of 11/24 you get a free $25 credit monthly until 1/25)

### Step by step:

1) Clone this repo to the directory of your choice
```
git clone https://github.com/rumarlon/Grok-Streamlit.git
```
2) Create python environment (preferably not in the directory you cloned)
```
python3 -m venv venv
```
3) Activate python environment
```
source venv/bin/activate
```
4) Install requirements
```
pip install -r requirements.txt
```
5) Paste your Grok API key in `.streamlit/secrets.toml` 
```
XAI_API_KEY="xai-restofyourkey"
```
6) Run your app
   
Text only:
```
streamlit run main.py
```
Multimoddal (Text & Image):
```
streamlit run main-vision.py
```

7) Your browser should open with a working streamlit app
8) Try a user prompt example, "What is the meaning of life, the universe, and everything?"
9) Get creative and test some other user prompts keeping in mind the system prompt currently is "You are Grok, a chatbot inspired by the Hitchhikers Guide to the Galaxy."

## What to do next?

Go ahead and change the system prompt and see what you can do with Grok. The prompt is in the [main.py](https://github.com/rumarlon/Grok-Streamlit/blob/master/main.py) or [main-vision.py](https://github.com/rumarlon/Grok-Streamlit/blob/master/main-vision.py). You must restart the python app after updating the system prompt. Sky is the limit!

From:
```
{"role": "system", "content": "You are Grok, a chatbot inspired by the Hitchhikers Guide to the Galaxy."}
```
To:
```
{"role": "system", "content": "Your new awesome prompt goes here"}
```

## Troubleshooting

If you get an API access error make sure you have a valid Grok API key and that the key is properly pasted in `.streamlit/secrets.toml`.

