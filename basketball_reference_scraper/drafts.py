import pandas as pd
from requests import get
from bs4 import BeautifulSoup


def get_draft_class(year):
    r = get(f"https://www.basketball-reference.com/draft/NBA_{year}.html")
    df = None

    if r.status_code == 200:
        soup = BeautifulSoup(r.content, "html.parser")
        table = soup.find("table")
        df = pd.read_html(str(table))[0]
        # get rid of duplicate pick col
        df.drop(["Unnamed: 0_level_0"], inplace=True, axis=1, level=0)
        df.columns = [
            "PICK",
            "TEAM",
            "PLAYER",
            "COLLEGE",
            "YEARS",
            "G",
            "MP",
            "PTS",
            "TRB",
            "AST",
            "FG%",
            "3P%",
            "FT%",
            "MPG",
            "PPG",
            "TRPG",
            "APG",
            "WS",
            "WS/48",
            "BPM",
            "VORP",
        ]
        # remove mid-table header rows
        df = df[df["PLAYER"].notna()]
        df = df[~df["PLAYER"].str.contains("Round|Player")]
        df.reset_index(inplace=True, drop=True)
        return df
