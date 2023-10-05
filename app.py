from datetime import datetime

import requests,api.bibleAPI as bib
from flask import Flask, render_template

# Directs Flask to find Static files
app = Flask(__name__, static_url_path='/static', static_folder='static')

dt = datetime.now()
currentTime = dt.strftime('%I:%M %p')
currentDayOfWeek,currentMonth,currentDay = dt.strftime('%A'),dt.strftime('%B'),dt.strftime('%d')
APIkey = '3e5358db3b3ab858d99d68405fe62b0b'

apicall = 'http://api.openweathermap.org/data/2.5/forecast?id=524901&appid={APIkey}'
jsondata = requests.get(url=apicall)

@app.route("/")
def index():
    return render_template("index.html", 
                           currentDayOfWeek=currentDayOfWeek,
                           currentDay=currentDay,
                           currentMonth=currentMonth,
                           currentTime=currentTime,
                           verse = bib.getVerse())

if __name__ == '__main__':
    app.run(host='127.0.0.1', debug=True)
