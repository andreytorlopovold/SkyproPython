from flask import Flask, request, render_template
from src.helpers import *

app = Flask(__name__)
candidates = []

@app.route("/")
def show_all_candidates():
    items = list(map(lambda x: {"id": x.id, "name": x.name}, candidates))
    return render_template('list.html', items=items)

@app.route("/candidate/<int:id>")
def show_candidate(id):
    c: Candidate = get_candidate(candidates, id)
    if c == None:
        return "Данные не найдены"
    card = {"name": c.name, "position": c.position, "img": c.picture_url, "skills": ", ".join(c.skills)}
    return render_template('card.html', card=card)

@app.route("/search/")
def show_search__name_error():
    return "Строка поиска по имени пустая!"

@app.route("/search/<name>")
def search_by_name(name):
    print(f">>> {name}")
    search_result = get_candidates_by_name(candidates, name)
    if len(search_result) == 0:
        return "Данные не найдены"
    items = list(map(lambda x: {"id": x.id, "name": x.name}, search_result))
    return render_template('list.html', items=items)


@app.route("/skill/")
def show_search_skill_error():
    return "Строка поиска по скиллам пустая!"

@app.route("/skill/<skill>")
def filter_by_skill(skill):
    search_result = get_candidates_by_skill(candidates, skill)
    if len(search_result) == 0:
        return "Данные не найдены"
    items = list(map(lambda x: {"id": x.id, "name": x.name}, search_result))
    return render_template('list.html', items=items)


if __name__ == "__main__":
    candidates = load_candidates_from_json('src/data/candidates.json')
    app.run()
