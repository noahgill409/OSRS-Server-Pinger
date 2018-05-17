# -*- coding: utf-8 -*-
"""
Created on Wed May 16 22:45:21 2018

@author: Noah
"""
import subprocess
import operator

prefix, suffix = "oldschool", ".runescape.com"
ignore_worlds = [1,2,3,4,8,9,10,11,12,16,17,18,24,25,26,27,28,30,33,34,35,36,41,42,43,44,45,49,50,51,52,58,59,60,63,64,65,66,67,68,71,72,73,75,76,81,82,83,84,85,87,88,89,90,91,92,93,94]
ping = {}

for i in range(1,95):
    
    if i in ignore_worlds:
        continue
    
    site = prefix+str(i)+suffix
    ret = subprocess.Popen(["ping.exe",site], stdout = subprocess.PIPE)
    rawdata = ret.communicate()[0] # byte fiasco, honestly not sure what's going on here
    data_delim = rawdata.splitlines() # bytes with \n \r etc, removed
    target = data_delim[len(data_delim)-1] # last bit has the goods, min, max, avg
    target_str = target.decode("utf-8") # turn into string
    indices = target_str.split(" = ") # delimit the = sign
    delay = indices[-1] # grab the last index, has the average ping reading "123ms"
    
    maxIndex = 0
    
    for j in range(len(delay)): # turn it into an int for comparison
        
        try:
            int(delay[j]) # see if the index is an int
            maxIndex = j # if so, increase max index it will read to
            
        except ValueError:
            continue
        
    delay = int(delay[0:maxIndex+1]) # exclusive, so + 1
    ping[i] = delay # store pair (world:delay)
    
    if delay < 100: # formatting
        delay = " "+str(delay)
    
    if i < 10:
        print("World ",i,"response:",delay)
    else:
        print("World",i,"response:",delay)


ping_sorted = sorted(ping.items(), key=operator.itemgetter(1))
best_worlds = 5 # top n worlds you want to see
if best_worlds > len(ping_sorted): # catch just in case the best_worlds is too many
    best_worlds = len(ping_sorted)
    
print("\nThe best",best_worlds,"worlds are:\n")
for i in range(best_worlds):
    world = ping_sorted[i][0]
    delay = ping_sorted[i][1]
    
    if delay < 100: # formatting
        delay = " "+str(delay)
    
    if world < 10:
        print("World ",world,"response:",delay)
    else:
        print("World",world,"response:",delay)
