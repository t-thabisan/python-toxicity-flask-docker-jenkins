from flask import Flask, redirect, url_for
from routes.toxicity_bp import toxicity_bp
from prometheus_client import start_http_server

app = Flask(__name__)
app.register_blueprint(toxicity_bp, url_prefix='/api')

@app.route('/')
def index():
    return redirect(url_for('toxicity_bp.default'))
    
if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0', port=5000)
start_http_server(8010)