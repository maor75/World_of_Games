from flask import Flask

app = Flask(__name__)


def read_score():
    try:
        with open("Scores.txt", "r") as file:
            score = int(file.read())
        return score
    except FileNotFoundError:
        return "Score file not found"
    except Exception as e:
        return str(e)


@app.route('/')
def score_server():
    score = read_score()
    if isinstance(score, int):
        return f'''
        <html>
        <head>
        <title>Scores Game</title>
        </head>
        <body>
        <h1>The score is <div id="score">{score}</div></h1>
        </body>
        </html>
        '''
    else:
        return f'''
        <html>
        <head>
        <title>Scores Game</title>
        </head>
        <body>
        <h1><div id="score" style="color:red">{score}</div></h1>
        </body>
        </html>
        '''


app.run(host="0.0.0.0", port=5000, debug=False)
