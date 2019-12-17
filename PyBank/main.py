import os
import csv
import re



# Read csv
csv_file = os.path.join("..","PyBank","budget_data.csv")
#months=["Jan","Feb","Mar","Apr","May","Jun","Jul","Aug","Sep","Oct","Nov","Dic"]
cmonth = 0
summonth = 0
appenddata=[]
totalappend=[]
total = 0
helprule = 0
avgchange = 0
maxvalue = 0
minvalue = 0


print("Financial Analysis")
print("--------------------------------")
with open(csv_file,"r",newline="")  as csvfile:
	readcsv=csv.reader(csvfile, delimiter=",")
	readcsv2=csv.reader(csvfile, delimiter=",")
	lel = next(readcsv,None)
	
	#print(next(readcsv2, 0))

	for row in readcsv:
		summonth=float(row[1]) + summonth
		cmonth = 1 + cmonth
		appenddata.append(row)
	#print(appenddata[3][1])

	for i in range(len(appenddata)-1):
			
			total = float(appenddata[i+1][1]) - float(appenddata[i][1])
			helprule = total + helprule
			if total > maxvalue:
				maxvalue = total
				mesmax = appenddata[i+1][0]
			if total < minvalue:
				minvalue = total
				mesmin = appenddata[i+1][0]
				
										
		
	avgchange = helprule/(cmonth-1)	
	
	
	print(f"Total months: {cmonth}")
	print(f"Total: ${summonth}")
	print(f"Average  Change: ${avgchange}")
	print(f"Greatest Increase in Profits: {mesmax} (${maxvalue})")
	print(f"Greatest Increase in Profits: {mesmin} (${minvalue})")	

	file1 = open("PyBank.txt","w") 
	L = [f"Financial Analysis \n------------------------------ \nTotal months: {cmonth} \nTotal: ${summonth}\nAverage  Change: ${avgchange}\nGreatest Increase in Profits: {mesmax} (${maxvalue})\nGreatest Increase in Profits: {mesmin} (${minvalue})"]  
	file1.writelines(L) 
	file1.close()


