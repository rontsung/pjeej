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
# rdr= csv.reader(open("timein.csv", "r" ) )
# csv_data = [ row for row in rdr ]
sec = 0
totsec = 0
eachday = {}
daydiff = {}
weekdiff = {}
upavg = 0
eachday["Monday"],eachday["Tuesday"],eachday["Wednesday"],eachday["Thursday"],eachday["Friday"]= 0,0,0,0,0
for index, row in df.iterrows():
    date = row["Date"]
    time = row["Time"]
    sec = int(time[0])*3600+int(time[2:])*60
    totsec += sec
    daydiff[date] = 0
    upavg = totsec/len(daydiff)
    daydiff[date] = (sec - upavg)/60
    dts[date] = sec
for day in eachday:
    tt = df.loc[df["Day of Week"] == day]
    count = 0
    upavg = 0
    totsec2 = 0
    for index, row in tt.iterrows():
        count += 1
        date = row["Date"]
        time = row["Time"]
        sec = int(time[0])*3600+int(time[2:])*60
        totsec2 += sec
        upavg = totsec2/count
        weekdiff[date] = (sec - upavg)/60
        eachday[day] += sec
    eachday[day] = eachday[day]/len(tt)
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
newweek = {}
for e in dates:
    for f in weekdiff:
        if e == f:
            newweek[f] = weekdiff[f]
overror = 0
werror = 0
for e in daydiff:
    overror += abs(daydiff[e])
overror = overror/len(daydiff)
for e in weekdiff:
    werror += abs(weekdiff[e])
werror = werror/len(daydiff)
while k < len_dates:
    newmarks.append(int(k))
    ndates.append(dates[int(k)])
    k+=interv
new = totsec/(len(df))
hr = str(new/3600)[0]
minu = str((new-int(hr)*3600)/60)
minu = minu[:minu.find(".")]
avg = hr+":"+minu

plt.plot(xs, [e for e in dts.values()], '-o')
plt.title("Overall")
plt.ylabel("Time in")
plt.xlabel("Date")
plt.xticks(newmarks, ndates, rotation = 25)
plt.yticks(ntimes, rtimes)
plt.hlines(y=new, xmin=0, xmax=len(df), color="grey")
plt.tight_layout()
plt.savefig("static/overall.png")

plt.clf()
week = np.arange(5)
plt.plot(week, [e for e in eachday.values()], '-o')
plt.title("Weekly")
plt.ylabel("Time in")
plt.xlabel("Day of Week")
plt.xticks(week, [e for e in eachday.keys()], rotation = 25)
plt.yticks(ntimes, rtimes)
plt.hlines(y=new, xmin=0, xmax=5, color="grey")
plt.tight_layout()
plt.savefig("static/weekly.png")

plt.clf()
plt.plot(xs, [e for e in daydiff.values()], '-o')
plt.title("Average Difference By Passing Day")
plt.ylabel("Difference")
plt.xlabel("Date")
plt.xticks(newmarks, ndates, rotation = 25)
plt.hlines(y=0, xmin=0, xmax=len(df), color="grey")
plt.tight_layout()
plt.savefig("static/avgdiff.png")

plt.clf()
plt.plot(xs, [e for e in newweek.values()], '-o')
plt.title("Average Difference By Weekday")
plt.ylabel("Difference")
plt.xlabel("Date")
plt.xticks(newmarks, ndates, rotation = 25)
plt.hlines(y=0, xmin=0, xmax=len(df), color="grey")
plt.tight_layout()
plt.savefig("stati.png")




# # Home route
@app.route("/")
def home():
    return render_template("index.html", dfd=df, avg = "Current Average: "+avg, overror = "Mean Error: "+str(overror)[:5], werror = "Mean Weekday Error: "+str(werror)[:5])

if __name__ == '__main__':
    app.run(debug=False)
