from flask import Flask, render_template
from flask_bootstrap import Bootstrap
from basketball_reference_scraper import players as p
from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField
from wtforms.validators import DataRequired

app = Flask(__name__)
app.config['SECRET_KEY'] = 'hard to guess string'
bootstrap = Bootstrap(app)


class player_search_form(FlaskForm):
    name = StringField('Player Name:', validators=[DataRequired()])
    submit = SubmitField('Submit')


@app.route("/")
@app.route("/index")
def home():
    return render_template('index.html')


@app.route("/players", methods=['GET', 'POST'])
def players():
    form = player_search_form()
    if form.is_submitted():
        name = form.name.data
        data = [
            p.get_player_headshot(name, False),
            p.get_stats(name, 'PER_GAME', False, False, False),
            p.get_stats(name, 'PER_GAME', True, False, False)
            ]
        return render_template('players.html', form=form, data=data)
    return render_template('players.html', form=form)


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
