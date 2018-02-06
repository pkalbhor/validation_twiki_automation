# 

#######################################################################
# Authors: Pritam Kalbhor
#          Ravindra Kumar Verma
######################################################################

# What does this program do?
# 1) Takes input from another file. Input is list of i/p files.
# 2) Extract some text from those files. Put it into output text file.


import os
import re
import sys

#Read number of lines in a file------------------------------------------
num_lines = 0
inp_files = []
with open('inputs.txt', 'r') as f1:
	for line in f1:
		if line.startswith("#"):
			continue
		elif not line.strip():
			continue
		else:
		        num_lines += 1
			inp_files.append(line)

print("Number of lines:"+str(num_lines))

#--------------------------------------------------------------------------
#Main code where text is extracted and stored in arrays.

arr = []		#Array for workflows
arr2 = []
CampID= []		#Campaign ID
GTags=[]		#Array for GT's
GTags2=[]
dataset=[]		#whole dataset
DTset=[]		#Dataset Name


with open("output.txt",'w') as f_out:
	for i in range(0, num_lines/2):
		f_out.write("\nDetails for the workflows:  \n\n")
	
		for j in range(2*(i+1)-2,2*(i+1)):
			with open(inp_files[j].strip(),'r') as file:
				for line in file:
#					if re.match("dataset: ", line):
#						for k in line.strip("dataset: ").split(","):
#							dataset.append(k.strip())
#							DTset.append(k.strip().split("/")[1])
					if re.match("/afs/cern.ch/work/", line):
                                                Tital=line.strip("/afs/cern.ch/work").split("/")[3]

					if re.match("type: ", line):
						f_out.write("   * "+ line)
					if re.match("dataset: ", line):
						f_out.write("   * Datasets: ")
						for k in line.strip("dataset: ").split(","):
                                                        dataset.append(k.strip())
							DTset.append(k.strip().split("/")[1])
							f_out.write(k.strip()+" ")
						f_out.write("\n")
					if re.match("run: ", line):
						f_out.write("   * "+ line)
					if re.match("Target ", line):
						f_out.write("   * "+ line)
					if re.match("Reference ", line):
						f_out.write("   * "+ line)
					if re.match("Common ", line):
						f_out.write("   * "+ line)
              
		              		if re.match("                 'Campaign': '", line):
                                                CampID.append(line.split("                 'Campaign': '")[1].strip("',\n"))
                                                #print(line.split("                 'Campaign': '")[1].strip("',\n"))

					if re.match("Injected workflow:", line):
						#print(line.split("Injected workflow: ")[1].strip())
						arr.append(line.split("Injected workflow: ")[1])

					if re.match("                 'GlobalTag': '", line):
						GTags.append(line.split("                 'GlobalTag': '")[1].strip("',\n"))
						#print(line.split("                 'GlobalTag': '")[1].strip("',\n"))
		
#	Sort-out according to dataset
		if (len(arr)>1):
			n = int(len(arr)/2)
			for x in range(0, n):
				arr2.append(arr[x])
				arr2.append(arr[n + x])
		else:
			arr2.append(arr[0])

#	Datasets
		n=int(len(GTags)/2)
		for x in range(0, n):
			GTags2.append(GTags[x])
                        GTags2.append(GTags[n+x])

#	Workflows list
		f_out.write("\n---+++++List of workflows: \n")
		ind = 0
		for i in range(0, len(arr2)):
			if(i % 2 == 0):
				if(ind < len(DTset)):
					f_out.write("\n   * "+DTset[ind]+"\n")
					ind=ind+1		
			f_out.write("   * "+ arr2[i].strip()+"\n")
		f_out.write("   * Campaign ID: [[https://dmytro.web.cern.ch/dmytro/cmsprodmon/requests.php?campaign="+CampID[0]+"]["+CampID[0] +"]]\n" )
		f_out.write("\n")

#	Table	
		print(Tital)
		print(str(len(arr))+" WF:"+str(len(arr2))+ " GT:" + str(len(GTags2))+" #Dataset "+str(len(dataset))+" CampID:"+str(len(CampID))+"\n" )
		f_out.write("| *Workflow* | *Description* | *PD* | *GTs* | *DQM Plots* | *Overlay* |\n")
		count=0
		
		for x in range(0, len(arr2)):
			if(x%2 ==0):
				cond="Reference"
				cond2=""
			else:
				cond="New Condition"
				cond2="New vs Prompt Ref"

			f_out.write("| WF "+str(x+1)+ " | !"+cond+" |"+ dataset[count] +"|"+ GTags2[x] +" | | [[ ]["+cond2 +"]] |\n")
                        if(x%2 == 1):
                                count=count+1
		
		del arr[:]
		del arr2[:]
		del CampID[:]
		del GTags[:]
		del GTags2[:]
		del dataset[:]			#Erase everything from it, to start appending freshly
		del DTset[:]


#Write to output file. Please check output file named as "output.txt" 
#--------------------------------------------------------------------------------------------------------------

