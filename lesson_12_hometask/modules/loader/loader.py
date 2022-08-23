from flask import Blueprint, request, render_template
from models.post import Post
from functions import load_list, save_posts

post_blueprint = Blueprint('post_blueprint', __name__, template_folder='templates')

@post_blueprint.route('/post', methods=['GET'])
def loader_page():
    return render_template("post_form.html")


@post_blueprint.route("/upload", methods=["POST"])
def post_upload():
    picture = request.files.get("picture")
    content = request.values.get("content")
    file_path = f"./uploads/{picture.filename}"
    post = Post(f'/uploads/{picture.filename}', content)
    picture.save(file_path)
    posts = load_list()
    posts.append(post)
    save_posts(posts, 'posts.json')

    return render_template("post_uploaded.html", post=post.__dict__)

