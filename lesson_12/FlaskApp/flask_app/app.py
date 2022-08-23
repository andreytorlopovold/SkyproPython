from flask import Flask, request, render_template
from Search.views import search_blueprint

app = Flask(__name__)

app.register_blueprint(search_blueprint, url_prefix='/search')

@app.route("/")
def home():
    return '<h1>Hello!</h1>'


if __name__ == "__main__":
    app.run()