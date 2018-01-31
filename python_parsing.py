
import os
import re
import sys

os.chdir('/home/pk/Desktop/Programming/Python/parsing')

# print(os.getcwd())
# for f in os.listdir():
#     print(f)


#
f = open('wmc_PR.log', 'r')
f_contents = f.readline()  # reads single line
# print(f_contents, end="")
#

#------ Read in a chunk --------

# size_to_read = 10
# while len(f_contents) > 0:
#     print(f_contents, end='')
#     f_contents = f.read(size_to_read)

# look for pattern
i = 1
print("List of workflows: ")

k = ["DoubleEG", "SinglePhoton", "JetHT", "DoubleMuon", "SingleMuon", "HLTPhysics", "MET", "ZeroBias"]

arr = []

for line in f:
    if re.match("Injected workflow:", line):
        # print(line.split("Injected workflow: ")[1], end="")
        tt = (line.split("Injected workflow: ")[1])
        print("ffsd", tt)
        if tt == 'rverma_PR_reference_RelVal_306154_171209_114545_4322':
            print("yes da")
        arr.append(line.split("Injected workflow: ")[1])

# Sort out workflow names
arr2 = []
n = int(len(arr) / 2)
for x in range(0, n):
    arr2.append(arr[x])
    arr2.append(arr[n + x])

ind = 0
print()
print (k[ind])

mycount = 0
# for x in range(0, len(k)):
#     print(k[x])
for i in range(0, len(arr2)):
    print(arr2[i], end="")
    mycount = mycount + 1
    if(mycount % 3 == 2):
        ind = ind + 1
        mycount = mycount + 1
        if(ind < len(k)):
            print()
            print (k[ind])

print(len(arr))


f.close()
