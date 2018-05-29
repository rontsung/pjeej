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
	# writer.writerow(["3/12/2018","Monday","8:26", "28"])
	# writer.writerow(["3/13/2018","Tuesday","9:16", "33"]) #[12]
	# writer.writerow(["3/14/2018","Wednesday","8:52", "31"])
	# writer.writerow(["3/15/2018","Thursday","9:04", "35"])
	# writer.writerow(["3/16/2018","Friday","8:32", "31"])
	# writer.writerow(["3/19/2018","Monday","8:05", "30"]) #[13]
	# writer.writerow(["3/20/2018","Tuesday","8:53", "30"])
	# writer.writerow(["3/21/2018","Wednesday","8:39", "34"])
	# writer.writerow(["3/22/2018","Thursday","8:49", "34"])
	# writer.writerow(["3/27/2018","Tuesday","9:19", "36"]) #[14]
	# writer.writerow(["3/28/2018","Wednesday","9:27", "41"])
	# writer.writerow(["3/29/2018","Thursday","8:56", ""]) #[15]
	# writer.writerow(["3/30/2018","Friday","8:48", "61"])
	# writer.writerow(["4/03/2018","Tuesday","8:56", ""])
	# writer.writerow(["4/04/2018","Wednesday","9:15", "50"])
	# writer.writerow(["4/05/2018","Thursday","8:42", ""])
	# writer.writerow(["4/06/2018","Friday","9:23", "38"])
	# writer.writerow(["4/09/2018","Monday","8:25", "32"]) #[16]
	# writer.writerow(["4/10/2018","Tuesday","8:40", "38"])
	# writer.writerow(["4/12/2018","Thursday","8:55", "46"])
	# writer.writerow(["4/13/2018","Friday","8:41", "63"])
	# writer.writerow(["4/16/2018","Monday","8:45", "53"])
	# writer.writerow(["4/17/2018","Tuesday","8:50", "42"])
	# writer.writerow(["4/18/2018","Wednesday","9:08", "43"])
	# writer.writerow(["4/20/2018","Friday","8:22", "39"]) #[17]
	# writer.writerow(["4/23/2018","Monday","9:19", "54"])
	# writer.writerow(["4/24/2018","Tuesday","8:48", "51"]) #[18]
	# writer.writerow(["4/25/2018","Wednesday","9:06", "55"])
	# writer.writerow(["4/27/2018","Friday","9:03", "52"])
	# writer.writerow(["4/30/2018","Monday","9:00", "48"])
	# writer.writerow(["5/01/2018","Tuesday","8:47", "55"])
	# writer.writerow(["5/02/2018","Wednesday","9:09", "74"])
	# writer.writerow(["5/03/2018","Thursday","8:46", "75"])
	# writer.writerow(["5/07/2018","Monday","9:08", "60"])
	# writer.writerow(["5/08/2018","Tuesday","8:20", "56"])
	# writer.writerow(["5/09/2018","Wednesday","9:05", ""])
	# writer.writerow(["5/10/2018","Thursday","8:52", "54"])
	# writer.writerow(["5/11/2018","Friday","8:31", "67"])
	# writer.writerow(["5/15/2018","Tuesday","8:54", "71"])
	# writer.writerow(["5/16/2018","Wednesday","8:45", "62"])
	# writer.writerow(["5/23/2018","Wednesday","8:56", "65"]) #[20]
	# writer.writerow(["5/25/2018","Friday","9:12", "72"])
	writer.writerow(["5/29/2018","Tuesday","9:05", "68"])
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
# [12] inclement weather; overheard him saying that he had to maintain gas station
# [13] 3/19 in before me
# [14] flew back from his vacation on same day
# [15] came in after this recorded time and before 9:30
# [16] came in before I did 4/09
# [17] went with the dive team early the day before 
# [18] estimate based on when I got back into the room (8:50) and he only had the desktop open
# [19] estimate - he came in between 8:55 and 9:10
# [20] estimate - came in between 8:52 and 9:02