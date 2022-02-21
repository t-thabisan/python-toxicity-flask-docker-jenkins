from flask import Blueprint
from controller.toxicityController import default, toxicity_sentence_check

# Blueprint definition
toxicity_bp = Blueprint('toxicity_bp', __name__)

# Routes definition
toxicity_bp.route('/default', methods=['GET'])(default)
toxicity_bp.route('/toxicity', methods=['GET'])(toxicity_sentence_check)