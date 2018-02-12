from flask import Flask, jsonify, render_template, request, redirect
import pandas as pd
import csv
import numpy as np
import matplotlib
matplotlib.use('Agg')
from matplotlib import pyplot as plt

# Flask setup
app = Flask(__name__)

df = pd.read_csv("timein.csv")
dts = {}
rtimes = ["8:00", "8:20", "8:40", "9:00", "9:20"]
ntimes = [int(e[0])*3600+int(e[2:])*60 for e in rtimes]
rdr= csv.reader(open("timein.csv", "r" ) )
csv_data = [ row for row in rdr ]
sec = 0
totsec = 0
for index, row in df.iterrows():
    date = row["Date"]
    time = row["Time"]
    sec = int(time[0])*3600+int(time[2:])*60
    totsec = totsec + sec
    ntimes.append(sec)
    dts[date] = sec
# for row in csv_data:
    # if row[2]=="Time":
    #     continue
    # time = row[2]
    # totsec = totsec + int(time[0])*3600+int(time[2:])*60
xs = np.arange(len(dts))
dates = [e for e in dts.keys()]
len_dates = len(dates)
times = [e for e in dts.values()]
interv = len(dates)/5-.1
k = 0
ndates = []
newmarks = []
while k < len_dates:
    newmarks.append(int(k))
    ndates.append(dates[int(k)])
    k+=interv
plt.plot(xs, [e for e in dts.values()])
plt.xticks(newmarks, ndates, rotation = 25)
plt.yticks(ntimes, rtimes)
plt.savefig("static/graph2.png")

new = totsec/(len(csv_data)-1)
hr = str(new/3600)[0]
minu = str((new-int(hr)*3600)/60)
minu = minu[:minu.find(".")]
avg = hr+":"+minu


# # Home route
@app.route("/")
def home():
    return render_template("index.html", dfd=csv_data, avg = "Current Average: "+avg)

if __name__ == '__main__':
    app.run(debug=False)
