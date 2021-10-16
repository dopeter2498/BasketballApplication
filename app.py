from flask import Flask, render_template
from flask_bootstrap import Bootstrap
from basketball_reference_scraper import box_scores
from datetime import date
from flask_wtf import FlaskForm
from wtforms import SelectField, SubmitField

app = Flask(__name__)
app.config['SECRET_KEY'] = 'hard to guess string'
bootstrap = Bootstrap(app)


class SearchForm(FlaskForm):
    month = SelectField(
                'Month:',
                choices=[
                    'October',
                    'November',
                    'December',
                    'January',
                    'February',
                    'March',
                    'April',
                    'May',
                    'June',
                    'July'
                ]
            )
    currYear = date.today().year
    if (date.today().month > 7):
        currYear += 1
    year = SelectField(
                'Season:',
                choices=[year for year in range(currYear, 1946, -1)]
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


@app.route("/leaders")
def leaders():
    return render_template('leaders.html')


@app.route("/scores", methods=['GET', 'POST'])
def scores():
    form = SearchForm()
    data = None
    month = None
    if form.validate_on_submit():
        month = form.month.data
        data = box_scores.get_schedule(int(form.year.data), form.month.data)
        return render_template('scores.html', form=form, data=[data, month])
    year = date.today().year
    if (date.today().month > 7):
        year += 1
    month = 'October'
    data = box_scores.get_schedule(year, month)
    return render_template('scores.html', form=form, data=[data, month])


@app.route("/draft")
def draft():
    return render_template('draft.html')


if __name__ == "__main__":
    app.run()
