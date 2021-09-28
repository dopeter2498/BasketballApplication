from flask import Flask, render_template
from basketball_reference_scraper.teams import get_roster, get_team_stats, get_opp_stats, get_roster_stats, get_team_misc


app = Flask(__name__)

@app.route("/home")
def home():
    return render_template('home.html')

@app.route("/drafts")
def drafts():
    return print(get_roster('LAL',2019))

if __name__ == "__main__":
    app.run(debug=True)