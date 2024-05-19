from flask import Flask, render_template, Blueprint, request
from models.language_model import LanguageModel
from models.history_model import HistoryModel
from deep_translator import GoogleTranslator

app = Flask(__name__)

language_controller = Blueprint("language_controller", __name__)


def _get_form():
    return {
        "text_to_translate": request.form.get("text-to-translate"),
        "translate_from": request.form.get("translate-from"),
        "translate_to": request.form.get("translate-to"),
    }


@language_controller.route("/", methods=["GET"])
@app.route("/", methods=["GET"])
def index():
    languages = LanguageModel.list_dicts()
    text_to_translate = "O que deseja traduzir?"
    translate_from = "pt"
    translate_to = "en"
    translated = "What do you want to translate?"
    return render_template(
        "index.html",
        languages=languages,
        text_to_translate=text_to_translate,
        translate_from=translate_from,
        translate_to=translate_to,
        translated=translated,
    )


@language_controller.route("/", methods=["POST"])
@app.route("/", methods=["POST"])
def translate():
    text_to_translate, translate_from, translate_to = _get_form().values()
    translated = GoogleTranslator(
        source=translate_from,
        target=translate_to
    ).translate(text_to_translate)
    HistoryModel(
        {
            "text_to_translate": text_to_translate,
            "translate_from": translate_from,
            "translate_to": translate_to,
        }
    ).save()
    return render_template(
        "index.html",
        languages=LanguageModel.list_dicts(),
        text_to_translate=text_to_translate,
        translate_from=translate_from,
        translate_to=translate_to,
        translated=translated,
    )


@language_controller.route("/reverse", methods=["POST"])
def reverse():
    text_to_translate, translate_from, translate_to = _get_form().values()
    translated = GoogleTranslator(
        source=translate_from,
        target=translate_to
    ).translate(text_to_translate)
    return render_template(
        "index.html",
        languages=LanguageModel.list_dicts(),
        text_to_translate=translated,
        translate_from=translate_to,
        translate_to=translate_from,
        translated=text_to_translate,
    )
