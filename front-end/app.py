from flask import Flask, redirect, url_for
from routes.toxicity_bp import toxicity_bp

app = Flask(__name__)
app.register_blueprint(toxicity_bp, url_prefix='/toxicity')


@app.route('/')
def index():
    return redirect(url_for('toxicity_bp.toxicity_form'))


if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5001)
