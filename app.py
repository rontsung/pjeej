from flask import Flask, jsonify, render_template, request, redirect
import pandas as pd
import csv

# Flask setup
app = Flask(__name__)

# df = pd.read_csv("timein.csv")
rdr= csv.reader(open("timein.csv", "r" ) )
csv_data = [ row for row in rdr ]
pic = "et.jpg"
# df1 = df.to_html("df1.html", index = False)
# print(df1)

# # Home route
@app.route("/")
def home():
    return render_template("index.html", dfd=csv_data, imgg = pic)

if __name__ == '__main__':
    app.run(debug=False)
