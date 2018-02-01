# 

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
	        num_lines += 1
		inp_files.append(line)
print("Number of lines:")
print(num_lines)
print(inp_files[1].strip())

#--------------------------------------------------------------------------
#Main code where text is extracted and stored in arrays.

arr = []		#Array for workflows
my_lines=[]		#Array for GT's

for k in range(0, 2):
	with open(inp_files[k].strip(),'r') as file:
		for line in file:
			if re.match("Injected workflow:", line):
				print(line.split("Injected workflow: ")[1].strip())
				arr.append(line.split("Injected workflow: ")[1])
			if re.match("                 'GlobalTag': '", line):
				my_lines.append(line.split("                 'GlobalTag': '")[1].strip("',\n"))
				print(line.split("                 'GlobalTag': '")[1].strip("',\n"))

#------------------------------------------------------------------------------------------------------------------
#Sort out workflow names

arr2 = []
n = int(len(arr) / 2)
for x in range(0, n):
    arr2.append(arr[x])
    arr2.append(arr[n + x])


#Write to output file. Please check output file named as "output.txt"
with open("output.txt",'w') as f_out:
	f_out.write("List of workflows: \n\n")
	for i in range(0, len(arr)):
		f_out.write(arr[i])

	f_out.write("\nList of Global Tags: \n\n")
	for i in range(0, len(my_lines)):
		f_out.write(my_lines[i]+"\n")


#--------------------------------------------------------------------------------------------------------------

