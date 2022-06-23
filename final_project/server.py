from machinetranslation import translator
from flask import Flask, render_template, request
import json

app = Flask("Web Translator", template_folder='templates')


@app.route("/englishToFrench")
def english_to_french():
    text_to_translate = request.args.get('text_to_translate')
    print('text_to_translate= ', text_to_translate)
    translated_text = ''
    if text_to_translate is not None or text_to_translate == "":
        translated_text = translator.english_to_french(text_to_translate)
    return translated_text


@app.route("/frenchToEnglish")
def french_to_english():
    text_to_translate = request.args.get('text_to_translate')
    translated_text = ''
    if text_to_translate is not None or text_to_translate == "":
        translated_text = translator.french_to_english(text_to_translate)
    return translated_text


@app.route("/")
def render_index_page():
    return render_template(str('index.html'))


if __name__ == "__main__":
    app.run(host="0.0.0.0", port=8080)
