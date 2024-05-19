from flask import Flask, render_template, Blueprint, request
from models.language_model import LanguageModel
from googletrans import Translator


app = Flask(__name__)


language_controller = Blueprint("language_controller", __name__)
translator = Translator()


def get_requests(reverse=False):
    text_to_translate = request.form.get(
        "text-to-translate",
        "O que deseja traduzir?"
    )
    translate_from = request.form.get("translate-from", "pt")
    translate_to = request.form.get("translate-to", "en")
    # Translate the text
    translated_text = translator.translate(
        text_to_translate,
        src=translate_from,
        dest=translate_to
    ).text
    if reverse:
        # Invert the languages
        translate_from, translate_to = translate_to, translate_from
        return translated_text, translate_from, translate_to, text_to_translate
    else:
        return text_to_translate, translate_from, translate_to, translated_text


@language_controller.route("/", methods=["GET", "POST"])
@app.route("/", methods=["GET", "POST"])
def index():
    if request.method == "POST":
        text_to_translate, translate_from, translate_to, translated = \
            get_requests()
    else:
        text_to_translate = "O que deseja traduzir?"
        translate_from = "pt"
        translate_to = "en"
        translated = "What do you want to translate?"
    languages = LanguageModel.list_dicts()
    return render_template(
        "index.html",
        languages=languages,
        text_to_translate=text_to_translate,
        translate_from=translate_from,
        translate_to=translate_to,
        translated=translated,
    )


@language_controller.route("/reverse", methods=["POST"])
def reverse():
    text_to_translate, translate_from, translate_to, translated = \
        get_requests(reverse=True)
    languages = LanguageModel.list_dicts()
    return render_template(
        "index.html",
        languages=languages,
        text_to_translate=text_to_translate,
        translate_from=translate_from,
        translate_to=translate_to,
        translated=translated,
    )
