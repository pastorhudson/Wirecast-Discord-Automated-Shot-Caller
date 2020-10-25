# Wirecast Discord Automated Shot Caller
This project enables wirecast to automatically call shots on a Discord Audio Channel.


We run this on the same computer that runs wirecast. Our wirecast comptuer happens to be Windows.
This version isn't tested on mac.

## Install
- Clone The directory to your c: drive
- rename the main directory "bot"
- Install Python 3.8 or higher
- Install dependencies `python -m pip install -r requirements_win.txt`

## Setup Login Info
- Create a file named secret.env in the c:\bot directory.
- Copy the template below and add your own discord bot keys and IBM Txt to speech keys.
```
BOT_TOKEN='asdasdasdasdasdasdasdasdasd'
VOICE_CHANNEL='media-team'
IBM_KEY="asdasdasdasdasdasdasdasdasdasdas"
IBM_URL="https://api.us-south.text-to-speech.watson.cloud.ibm.com/instances/asdasdasdasdasdasdasdasd"
```
- This bot uses the IBM Watson Txt to speech to make the audio files for the shot names.
- You can get a free account and the KEY and URL here https://cloud.ibm.com/docs/text-to-speech?topic=text-to-speech-gettingStarted


