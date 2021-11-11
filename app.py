from flask import Flask, render_template, request
from flask_bootstrap import Bootstrap
from basketball_reference_scraper import seasons as s
from basketball_reference_scraper import teams as t
from basketball_reference_scraper import leaders as leader
from basketball_reference_scraper import constants 
from basketball_reference_scraper.constants import TEAM_TO_TEAM_ABBR
from datetime import date
from flask_wtf import FlaskForm
from wtforms import SelectField, SubmitField
from wtforms.validators import DataRequired


app = Flask(__name__)
app.config['SECRET_KEY'] = 'hard to guess string'
bootstrap = Bootstrap(app)


class leaders_search_form(FlaskForm):
    currYear = date.today().year
    if (date.today().month > 7):
        currYear += 1
    year = SelectField(
                'Season:',
                choices=[year for year in range(currYear, 1949, -1)],
                validators=[DataRequired()]
           )
    submit = SubmitField('Submit')


@app.route("/")
@app.route("/index")
def home():
    return render_template('index.html')


@app.route("/players")
def players():
    return render_template('players.html')

  
@app.route("/teams", methods=['GET', 'POST'])
def teams():                                       
    data = s.get_standings()
    return render_template('teams.html', data=data)

  
@app.route("/teams-result/<string:team>", methods=['GET', 'POST'])
def teams_result(team):
    currYear = date.today().year
    if (date.today().month > 7):
        currYear += 1
    for key in TEAM_TO_TEAM_ABBR:
        if key == team.upper():
            teamAbbr = TEAM_TO_TEAM_ABBR[key]
    roster = t.get_roster_stats(teamAbbr,currYear)
    return render_template('/teams-result.html', roster=roster, team=team)


@app.route("/seasons")
def seasons():
    return render_template('seasons.html')


@app.route("/leaders", methods=['GET', 'POST'])
def leaders():
    form = leaders_search_form()
    if form.validate_on_submit():
        data = leader.get_season_leaders(form.year.data)
        return render_template('leaders.html', data=data, form=form)
    data = leader.get_season_leaders()
    return render_template('leaders.html', data=data, form=form)


@app.route("/scores")
def scores():
    return render_template('scores.html')


@app.route("/draft")
def draft():
    return render_template('draft.html')


if __name__ == "__main__":
    app.run()
