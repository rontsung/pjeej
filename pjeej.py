import csv
import pandas as pd

with open("timein.csv","a",newline="") as csvfile:
	writer = csv.writer(csvfile)
	# writer.writerow(["Date","Day of Week","Time", "Temp (F)"])
	# writer.writerow(["1/09/2018", "Tuesday","9:07", "23"]) #[1]
	# writer.writerow(["1/10/2018","Wednesday","8:58", "21"])
	# writer.writerow(["1/11/2018","Thursday","9:00", "39"])
	# writer.writerow(["1/12/2018","Friday","9:18", "62"])
	# writer.writerow(["1/15/2018","Monday","8:09", "22"]) #[2][3]
	# writer.writerow(["1/16/2018","Tuesday","8:49", "29"])
	# writer.writerow(["1/17/2018","Wednesday","8:56", "33"]) #[4]
	# writer.writerow(["1/18/2018","Thursday","9:16", "20"])
	# writer.writerow(["1/19/2018","Friday","9:01", "21"])
	# writer.writerow(["1/22/2018","Monday","8:29", "43"])
	# writer.writerow(["1/23/2018","Tuesday","8:25", "56"]) #[5]
	# writer.writerow(["1/24/2018","Wednesday","8:42", ""]) #[6]
	# writer.writerow(["1/26/2018","Friday","8:20", "19"])
	# writer.writerow(["1/29/2018","Monday","8:53", "39"])
	# writer.writerow(["1/30/2018","Tuesday","8:41", "32"])
	# writer.writerow(["1/31/2018","Wednesday","9:14", "20"]) #[7]
	# writer.writerow(["2/01/2018","Thursday","9:15", "31"]) #[8]
	# writer.writerow(["2/02/2018","Friday","8:47", "29"])
	# writer.writerow(["2/05/2018","Monday","8:21", "34"])
	# writer.writerow(["2/06/2018","Tuesday","9:02", "30"])
	# writer.writerow(["2/07/2018","Wednesday","8:58", "33"])
	# writer.writerow(["2/08/2018","Thursday","9:10", "27"])
	# writer.writerow(["2/13/2018","Tuesday","8:13", "27"]) #[9]
	# writer.writerow(["2/14/2018","Wednesday","8:41", "37"])
	# writer.writerow(["2/15/2018","Thursday","8:29", "47"])
	# writer.writerow(["2/16/2018","Friday","8:27", "54"]) #[10]	
	# writer.writerow(["2/20/2018","Tuesday","8:45", "53"])
	# writer.writerow(["2/22/2018","Thursday","8:53", "47"]) 
	# writer.writerow(["2/23/2018","Friday","9:10", "37"])
	# writer.writerow(["2/26/2018","Monday","8:19", "45"]) #[11]
	# writer.writerow(["2/27/2018","Tuesday","8:31", "35"])
	# writer.writerow(["2/28/2018","Wednesday","8:53", "45"])
	# writer.writerow(["3/01/2018","Thursday","8:37", "45"])
	# writer.writerow(["3/02/2018","Friday","8:47", "38"])
	# writer.writerow(["3/05/2018","Monday","8:38", "35"])
	# writer.writerow(["3/06/2018","Tuesday","8:50", "35"])
	# writer.writerow(["3/07/2018","Wednesday","8:47", "35"])
	# writer.writerow(["3/08/2018","Thursday","8:47", "35"])
	# writer.writerow(["3/09/2018","Friday","8:30", ""])
# [1] according to him, left at 8:30 night before 1/12/2018
# [2] came in before I did 1/15
# [3] did not check temperature until 9:50 1/15
# [4] winter storm 1/17
# [5] came in before I did 1/23
# [6] did not check temperature 1/24
# [7] according to Elias, stayed late for BMH-171 9:30
# [8] stayed late for BMH-171 (after 7:00 PM)
# [9] came in before I did after two day absence plus encounter on Thursday
# [10] was out of the room from about 8:24 to 8:37 and he came in during that interval; elias estimated (no help)
# [11] came in before I did 2/26