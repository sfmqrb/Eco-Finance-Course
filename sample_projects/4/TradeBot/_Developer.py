import pytse_client as tse
import csv
from persiantools.jdatetime import JalaliDate
from datetime import datetime as clock
import json

def writeToCsv(filePath, data):
    with open(filePath, 'a') as file:
        writter = csv.writer(file) 
        writter.writerow(data)

def writeToJson(q, s):
    date = JalaliDate.today()
    _time = clock.now()
    time = _time.strftime("%H:%M")

    dict = {
        "نماد": s,
        "تاریخ": date,
        "ساعت": time,
        "تعداد پس از معامله": q
    }
    json_obj = json.dumps(dict, indent=4)
    with open("./output/Stocks.json", "w") as file:
        file.write(json_obj)
def today():
    return JalaliDate.today()

def now():
    _time = clock.now()
    time = _time.strftime("%H:%M")
    return time
 