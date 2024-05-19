from flask import Flask, render_template, Blueprint
from models.language_model import LanguageModel


app = Flask(__name__)

language_controller = Blueprint("language_controller", __name__)


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
