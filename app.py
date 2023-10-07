from datetime import datetime
from tabnanny import verbose

import requests,api.bibleAPI as bib
from flask import Flask, render_template

# Directs Flask to find Static files
app = Flask(__name__, static_url_path='/static', static_folder='static')

dt = datetime.now()
currentTime = dt.strftime('%I:%M %p')
currentDayOfWeek,currentMonth,currentDay = dt.strftime('%A'),dt.strftime('%B'),dt.strftime('%d')

@app.route("/")
def index():
    chapter,verse = bib.getVerse()
    return render_template("index.html", 
                           currentDayOfWeek=currentDayOfWeek,
                           currentDay=currentDay,
                           currentMonth=currentMonth,
                           currentTime=currentTime,
                           chapter=chapter,
                           verse=verse )

if __name__ == '__main__':
    app.run(host='127.0.0.1', debug=True)
