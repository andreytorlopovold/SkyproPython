from flask import Blueprint

search_blueprint = Blueprint('search_blueprint', __name__, template_folder='templates')

@search_blueprint.route('/')
def profile_page():
    return f"<h1>Search page!</h1>"
