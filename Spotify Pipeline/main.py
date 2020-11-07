import sqlalchemy
import pandas as pd
from sqlalchemy.orm import sessionmaker
import requests
import json
from datetime import datetime
import datetime
import sqlite3

from config import user, token

DATABASE_LOCATION = "sqlite:///my_played_tracks.sqlite"
USER_ID = user
TOKEN = token

if __name__ == '__main__':
    headers = {
        "Accept": "application/json",
        "Content-Type": "application/json",
        "Authorization": f"Bearer {TOKEN}"
    }

    today = datetime.datetime.now()
    yesterday = today - datetime.timedelta(days=1)
    yesterday_unix_timestamp = int(yesterday.timestamp()) * 1000

    r = requests.get(f"https://api.spotify.com/v1/me/player/recently-played?limit=10&after={yesterday_unix_timestamp}",
                     headers=headers)

    data = r.json()
