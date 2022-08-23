from flask import Flask, request, render_template, send_from_directory
from modules.main.main import main_blueprint
from modules.loader.loader import post_blueprint
from flask import send_from_directory

POST_PATH = "posts.json"
UPLOAD_FOLDER = "uploads/images"

app = Flask(__name__)
app.config['MAX_CONTENT_LENGTH'] = 2 * 1024 * 1024

app.register_blueprint(main_blueprint)
app.register_blueprint(post_blueprint)

@app.route("/uploads/<path:path>")
def static_dir(path):
    return send_from_directory("uploads", path)

if __name__ == "__main__":
    app.run()