from os.path import join, dirname
from ibm_watson import TextToSpeechV1
from ibm_cloud_sdk_core.authenticators import IAMAuthenticator
import os
from dotenv import load_dotenv


load_dotenv(dotenv_path='secret.env')


def get_voice(text):
    filename = ""
    if len(text) < 31:
        filename = text
    else:
        filename = text[:30]

    authenticator = IAMAuthenticator(os.environ.get('IBM_KEY'))
    service = TextToSpeechV1(authenticator=authenticator)
    service.set_service_url(os.environ.get('IBM_URL'))


    print(text)
    print(text.replace(" ", ""))
    with open(join(dirname(__file__), f'sounds/{text.replace(" ", "")}.mp3'),
              'wb') as audio_file:
        response = service.synthesize(
            text, accept='audio/mp3',
            voice="en-US_AllisonV3Voice").get_result()
        audio_file.write(response.content)

    return audio_file.name


if __name__ == '__main__':
    print(get_voice("none"))
