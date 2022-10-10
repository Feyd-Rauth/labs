from datetime import datetime
from flask import Flask, render_template
import requests
from pytz import timezone

app = Flask(__name__)


@app.route("/", methods=("GET",))
def get_msc_time():
    """
    Shows current Moscow time
    :return: html page
    """
    date = datetime.now(timezone('Europe/Moscow')).strftime('%H:%M:%S')

    return render_template("index.html", date=date)
