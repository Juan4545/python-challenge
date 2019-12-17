import os
import csv
import re
import operator

csv_file = os.path.join("..","PyPoll","election_data.csv")

votes = 0
kvotes = 0
cvotes = 0
livotes = 0
ovotes = 0
winner = []
with open(csv_file,"r",newline="")  as csvfile:
	readcsv=csv.reader(csvfile, delimiter=",")
	header = next(readcsv,None)

	
	for row in readcsv:
		votes = 1 + votes
		if row[2] == "Khan":
			kvotes = 1 + kvotes
		elif row[2] == "Correy":
			cvotes = 1 + cvotes
		elif row[2] == "Li":
			livotes = 1 + livotes
		elif row[2] == "O'Tooley":
			ovotes = 1 + ovotes
			
	winner={'Khan': kvotes,'Correy':cvotes,'Li':livotes,'OTooley':ovotes}
	max_value = max(winner.values())
	max_keys = [k for k,v in winner.items() if v == max_value]

	print("Election Results")
	print("-----------------------------------")
	print(f"Total Votes: {votes}")	
	print("-----------------------------------")
	print(f"Khan: {round((kvotes/votes)*100,2)}% ({kvotes})")	
	print(f"Correy {round((cvotes/votes)*100,2)}% ({cvotes})")
	print(f"Li: {round((livotes/votes)*100,2)}% ({livotes})")
	print(f"O'Tooley: {round((ovotes/votes)*100,2)}% ({ovotes})")	
	print("-----------------------------------")
	print(f"Winner:{max_keys} with {max_value} votes")


	file1 = open("Pypoll.txt","w") 
	L = [f"Election Results \n------------------------------ \nTotal Votes: {votes} \n -----------------------------------\n Khan: {round((kvotes/votes)*100,2)}% ({kvotes})\n Correy {round((cvotes/votes)*100,2)}% ({cvotes}) \n Li: {round((livotes/votes)*100,2)}% ({livotes}) \nO'Tooley: {round((ovotes/votes)*100,2)}% ({ovotes}) \n -----------------------------------\n Winner:{max_keys} with {max_value} votes"]  
	file1.writelines(L) 
	file1.close()