from flask import Blueprint
from controller.toxicityController import toxicity_form, toxicity_sentence_check

# Blueprint definition
toxicity_bp = Blueprint('toxicity_bp', __name__)

# Routes definition
toxicity_bp.route('/', methods=['GET'])(toxicity_form)
toxicity_bp.route('/form', methods=['GET'])(toxicity_form)
toxicity_bp.route('/result', methods=['GET'])(toxicity_sentence_check)
