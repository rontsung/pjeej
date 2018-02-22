import csv
import pandas as pd

with open("jeo.csv","a",newline="") as csvfile:
	writer = csv.writer(csvfile)
	#writer.writerow(["Date","Day of Week","Time", "Statement", "Correct"])
	#writer.writerow(["02/21/18","Wednesday","", "Presidents same last names - both took office unexpectedly", "Ron"])
	#writer.writerow(["02/22/18","Thursday","9:15", "Musical Idioms - cheap so can be had for a ___", "Elias"])