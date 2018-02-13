import csv
import pandas as pd

with open("timein.csv","a",newline="") as csvfile:
	writer = csv.writer(csvfile)
	#writer.writerow(["Date","Day of Week","Time", "Temp (F)"])
	#writer.writerow(["1/9/2018", "Tuesday","9:07", "23"]) #[1]
	#writer.writerow(["1/10/2018","Wednesday","8:58", "21"])
	#writer.writerow(["1/11/2018","Thursday","9:00", "39"])
	#writer.writerow(["1/12/2018","Friday","9:18", "62"])
	#writer.writerow(["1/15/2018","Monday","8:09", "22"]) #[2][3]
	#writer.writerow(["1/16/2018","Tuesday","8:49", "29"])
	#writer.writerow(["1/17/2018","Wednesday","8:56", "33"]) #[4]
	#writer.writerow(["1/18/2018","Thursday","9:16", "20"])
	#writer.writerow(["1/19/2018","Friday","9:01", "21"])
	#writer.writerow(["1/22/2018","Monday","8:29", "43"])
	#writer.writerow(["1/23/2018","Tuesday","8:25", "56"]) #[5]
	#writer.writerow(["1/24/2018","Wednesday","8:42", ""]) #[6]
	#writer.writerow(["1/26/2018","Friday","8:20", "19"])
	#writer.writerow(["1/29/2018","Monday","8:53", "39"])
	#writer.writerow(["1/30/2018","Tuesday","8:41", "32"])
	#writer.writerow(["1/31/2018","Wednesday","9:14", "20"]) #[7]
	#writer.writerow(["2/1/2018","Thursday","9:15", "31"]) #[8]
	#writer.writerow(["2/2/2018","Friday","8:47", "29"])
	#writer.writerow(["2/5/2018","Monday","8:21", "34"])
	#writer.writerow(["2/6/2018","Tuesday","9:02", "30"])
	#writer.writerow(["2/7/2018","Wednesday","8:58", "33"])
	#writer.writerow(["2/8/2018","Thursday","9:10", "27"])
	#writer.writerow(["2/9/2018","Friday","N/A", "27"])
	#writer.writerow(["2/13/2018","Tuesday","8:13", "27"]) #[9]

# [1] according to him, left at 8:30 night before 1/12/2018
# [2] came in before I did 1/15
# [3] did not check temperature until 9:50 1/15
# [4] winter storm 1/17
# [5] came in before I did 1/23
# [6] did not check temperature 1/24
# [7] according to Elias, stayed late for BMH-171 9:30
# [8] stayed late for BMH-171 (after 7:00 PM)
# [9] came in before I did after two day absence plus encounter on Thursday
