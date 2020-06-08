from Utils import *
import os.path
from flask import Flask

app = Flask(__name__)

@app.route('/')
def home():
    return generte_template()

def score_server():
    user_scores = read_scores()
    html_code = generate_html_code(user_scores)
    # show web page
    app.run(port=50000, debug=True)

# generate template
def generte_template():
    try:
        tmp_file_name = "index.html"
        temp_file = open(tmp_file_name, "r")
        return temp_file.read()
    except FileNotFoundError:
        print("Error in template file ...")
        return ""


# generate HTML code
def generate_html_code(scores):
    html = "<HTML>"
    html += "<HEAD><TITLE>Scores Game</TITLE></HEAD>"
    html += "<BODY>"
    if scores == BAD_RETURN_CODE:
        html += "<h1><div id=\"score\" style=""color:red"">Problem showing the result ... </div></h1>"
    else:
        html += "<h1>The score is <div id=\"score\">" + str(scores) + "</div></h1>"
    html += "</BODY>"
    html += "</HTML>"

    # write template file
    temp_file = open("index.html", "w")
    temp_file.write(html)

    return html


# read scores from file or create a new file
def read_scores():
    try:
        player_scores = 0
        if os.path.isfile(SCORES_FILE_NAME):
            # read file content
            scores_file = open(SCORES_FILE_NAME, "r")
            player_scores = scores_file.readline()
            if not player_scores.isdigit():
                player_scores = 0
            scores_file.close()
        else:
            # create new file
            scores_file = open(SCORES_FILE_NAME, "w")
            scores_file.write(str(player_scores))
            scores_file.close()

        return player_scores

    except IOError:
        print("Error creating scores file ....")
        return BAD_RETURN_CODE
