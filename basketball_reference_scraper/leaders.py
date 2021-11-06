import pandas as pd
from datetime import datetime
from requests import get
from bs4 import BeautifulSoup


def get_season_leaders(season=None):
    if season is None:
        date = datetime.now()
        if date.month > 7:
            season = date.year + 1
        else:
            season = date.year
    df = pd.DataFrame()
    r = get(f'https://widgets.sports-reference.com/wg.fcgi?css=1&site=bbr&url=%2Fleagues%2FNBA_{season}_totals.html&div=div_totals_stats')
    soup = BeautifulSoup(r.content, 'html.parser')
    table = soup.find('table')
    df = pd.read_html(str(table))[0]
    df.rename(columns={'Player': 'PLAYER', 'Pos': 'POS', 'Age': 'AGE',
              'Tm': 'TEAM'}, inplace=True)
    df = df[(df['PLAYER'] != 'Player')]
    df = df.reset_index(drop=True)
    return [df, season]
