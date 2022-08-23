from flask import Blueprint, request, render_template
from models.post import Post
from functions import load_list, filter_by_word

main_blueprint = Blueprint('main_blueprint', __name__, template_folder='templates')

posts: [Post] = []

@main_blueprint.route('/')
def main_page():
    global posts
    posts = load_list()
    return render_template("index.html")


@main_blueprint.route("/search", methods=['GET', "POST"])
def search():
     request_value = request.values.get('s')
     models = list(map(lambda x: x.__dict__, filter_by_word(posts, request_value)))
     return render_template("post_list.html", request_value=request_value, models=models)