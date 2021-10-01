from flask import Flask, render_template
from flask_bootstrap import Bootstrap

app = Flask(__name__)
bootstrap = Bootstrap(app)

@app.route("/")
@app.route("/index")
def home():
    return render_template('index.html')

@app.route("/players")
def players():
    return render_template('players.html')

@app.route("/teams")
def teams():
    return render_template('teams.html')

@app.route("/seasons")
def seasons():
    return render_template('seasons.html')

@app.route("/leaders")
def leaders():
    return render_template('leaders.html')

@app.route("/scores")
def scores():
    return render_template('scores.html')

@app.route("/draft")
def draft():
    return render_template('draft.html')

if __name__ == "__main__":
    app.run()
