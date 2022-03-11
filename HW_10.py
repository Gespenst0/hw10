from flask import Flask
import json

app = Flask(__name__)


def get_candidates():
    with open("candidates.json", "r") as file:
        candidates_json = file.read()
        candidates = json.loads(candidates_json)
        return candidates


candidates = get_candidates()


def get_all_candidates():
    screen_info = str()
    for candidate in candidates:
        name = candidate["name"]
        position = candidate["position"]
        skills = candidate["skills"]
        info = "<pre>Имя кандидата - " + str(name) + "\n" + "Позиция - " + str(position) + "\n" + "Навыки - " + str(skills) + "<pre>\n\n"
        screen_info = screen_info + info
    return screen_info


def get_candidate(uid):
    for candidate in candidates:
        if str(candidate["id"]) == str(uid):
            picture = candidate["picture"]
            name = candidate["name"]
            position = candidate["position"]
            skills = candidate["skills"]
            show_picture = '<img src="' + picture + '">\n\n\n'
            show_text = "<pre>Имя кандидата - " + str(name) + "\n" + "Позиция - " + str(position) + "\n" + "Навыки - " + str(skills) + "<pre>"
            screen = show_picture + show_text
    return screen


def get_skills(name_skill):
    screen_info = str()
    for candidate in candidates:
        if name_skill in candidate["skills"]:
            name = candidate["name"]
            position = candidate["position"]
            skills = candidate["skills"]
            info = "<pre>Имя кандидата - " + str(name) + "\n" + "Позиция - " + str(position) + "\n" + "Навыки - " + str(skills) + "<pre>\n\n"
            screen_info = screen_info + info
    return screen_info


@app.route("/")
def page_index():
    return get_all_candidates()


@app.route('/candidate/<int:uid>')
def profile(uid):
    return get_candidate(uid)


@app.route('/candidate/skill/<name_skill>')
def skill(name_skill):
    return get_skills(name_skill)


app.run()
