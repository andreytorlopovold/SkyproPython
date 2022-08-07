from flask import Flask
import helpers

app = Flask(__name__)
candidates = []

@app.route("/")
def hello_world():
    all_candidates = helpers.get_all(candidates)
    text = "\n\n".join(all_candidates)
    result = f'<pre>{text}</pre>'
    return result

@app.route("/candidates/<int:uid>")
def show_candidate(uid):
    candidates = helpers.load_candidates()
    c = helpers.get_by_pk(candidates, uid)
    if c == None:
        return "Данные не найдены"

    result = f'<img src="{c.picture_url}">'
    result += '<br>'
    result += '<pre>'
    result += c.get_info()
    result += '</pre>'
    
    return result

@app.route("/skills/<skill_name>")
def show_skills(skill_name):
    candidate_list = helpers.get_by_skill(candidates, skill_name)
    if len(candidate_list) == 0:
        return "Данные не найдены"

    result = "<pre>"
    for item in candidate_list:
        result += item.get_info()
        result += "<br><br>"
    result += "</pre>"

    return result


if __name__ == "__main__":
    candidates = helpers.load_candidates()
    app.run()
