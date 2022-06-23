"""
This module contains translator functions.
"""
import os
import ibm_watson
from ibm_cloud_sdk_core.authenticators import IAMAuthenticator
from dotenv import load_dotenv

load_dotenv()

apikey = os.environ['apikey']
apiurl = os.environ['url']

authenticator = IAMAuthenticator(apikey)
language_translator = ibm_watson.LanguageTranslatorV3(
    version='2018-05-01',
    authenticator=authenticator
)

language_translator.set_service_url(apiurl)


def english_to_french(english_text):
    """
    Function that translate input text from English to French.
    """
    french_text = None
    if english_text is not None:
        result = language_translator.translate(
            english_text,
            model_id='en-fr'
        ).get_result()
        french_text = result['translations'][0]['translation']
    return french_text


def french_to_english(french_text):
    """
    Function that translate input text from French to English.
    """
    english_text = None
    if french_text is not None:
        result = language_translator.translate(
            french_text,
            model_id='fr-en'
        ).get_result()
        english_text = result['translations'][0]['translation']
    return english_text
