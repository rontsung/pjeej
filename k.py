import csv
import pandas as pd

with open("checkin.csv","a",newline="") as csvfile:
	writer = csv.writer(csvfile)
	#writer.writerow(["Date","Day of Week","Time", "E"])
	#writer.writerow(["1/30/18","Tuesday","8:15", "Y"]) # ***
	#writer.writerow(["1/31/18","Wednesday","<8:15", "N"])
	#writer.writerow(["2/1/18","Thursday","8:10", "N"])
	#writer.writerow(["2/2/18","Friday","<8:09", "N"]) # ^*
	#writer.writerow(["2/5/18","Monday","8:21", "N"])
	#writer.writerow(["2/6/18","Tuesday","~8:20", "Y"])
	#writer.writerow(["2/7/18","Wednesday","8:17", "N"])
	#writer.writerow(["2/8/18","Thursday","8:59", "N"])
	#writer.writerow(["2/9/18","Friday","N/A", "N/A"])
	#writer.writerow(["2/12/18","Monday","N/A", "N"])
	#writer.writerow(["2/13/18","Tuesday","9:38", "N"])
	#writer.writerow(["2/14/18","Wednesday","9:24", "N"])
	writer.writerow(["2/15/18","Thursday","9:31", "N"])