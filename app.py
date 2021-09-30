from flask import Flask, render_template
from basketball_reference_scraper.teams import get_roster, get_team_stats, get_opp_stats, get_roster_stats, get_team_misc
from flask_bootstrap import Bootstrap



app = Flask(__name__)
bootstrap = Bootstrap(app)

@app.route("/")
@app.route("/home")
def home():
    return render_template('home.html')

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

@app.route("/drafts")
def drafts():
    return render_template('drafts.html')

if __name__ == "__main__":
    app.run(debug=True)