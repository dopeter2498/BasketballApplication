from flask import Flask, render_template
from flask_bootstrap import Bootstrap
from basketball_reference_scraper import leaders as leader
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


@app.route("/teams")
def teams():
    return render_template('teams.html')


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
