from flask import Flask, jsonify, render_template, request, redirect
import pandas as pd
import csv

# Flask setup
app = Flask(__name__)

df = pd.read_csv("timein.csv")
rdr= csv.reader(open("timein.csv", "r" ) )
csv_data = [ row for row in rdr ]
sec = 0
for row in csv_data:
    if row[2]=="Time":
        continue
    time = row[2]
    sec = sec + int(time[0])*3600+int(time[2:])*60

new = sec/(len(csv_data)-1)
hr = str(new/3600)[0]
minu = str((new-int(hr)*3600)/60)
minu = minu[:minu.find(".")]
avg = hr+":"+minu
# print(sec, new, hr, min, avg)
# df1 = df.to_html("df1.html", index = False)
# print(df1)

# # Home route
@app.route("/")
def home():
    return render_template("index.html", dfd=csv_data, avg = "Current Average: "+avg)

if __name__ == '__main__':
    app.run(debug=False)
