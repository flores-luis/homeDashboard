from datetime import datetime 
import re
import requests
from flask import Flask, render_template

app = Flask(__name__)
dt = datetime.now()
currentTime = dt.strftime('%I:%M %p')
currentDayOfWeek,currentMonth,currentDay = dt.strftime('%A'),dt.strftime('%B'),dt.strftime('%d')
APIkey = '3e5358db3b3ab858d99d68405fe62b0b'

apicall = 'http://api.openweathermap.org/data/2.5/forecast?id=524901&appid={APIkey}'
jsondata = requests.get(url=apicall)

@app.route("/")
def index():
    return render_template("index.html", currentDayOfWeek=currentDayOfWeek,currentDay=currentDay,currentMonth=currentMonth,currentTime=currentTime)

if __name__ == '__main__':
    app.run(host='127.0.0.1', port=5000, debug=False)
