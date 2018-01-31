
import os
import re
import sys


#Open text files
f = open(sys.argv[1], 'r')
f_out = open(sys.argv[2], 'w')
f_contents = f.readline()  # reads single line


print("List of workflows: ")
arr = []
for line in f:
    if re.match("Injected workflow:", line):
        # print(line.split("Injected workflow: ")[1], end="")
        arr.append(line.split("Injected workflow: ")[1])

#Sort out workflow names
arr2 = []
n = int(len(arr) / 2)
for x in range(0, n):
    arr2.append(arr[x])
    arr2.append(arr[n + x])

#Write to file
for i in range(0, len(arr2)):
    f_out.write(arr2[i])


#close all files
f.close()
f_out.close()
