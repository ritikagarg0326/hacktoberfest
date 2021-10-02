#!/bin/python3

import math
import os
import random
import re
import sys



#
# Complete the 'processLogs' function below.
#
# The function is expected to return a STRING_ARRAY.
# The function accepts following parameters:
#  1. STRING_ARRAY logs
#  2. INTEGER maxSpan
#

def processLogs(logs, maxSpan):
    d={}
    for i in range(len(logs)):
        list1=logs[i].split(' ')
        
    for j in range(len(list1)):
        if (list1[j]) not  in d:
            d[j]=int(list1[j]),int(list1[j+1])
        else:
            d[j]=1
    print(d)           

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    logs_count = int(input().strip())

    logs = []

    for _ in range(logs_count):
        logs_item = input()
        logs.append(logs_item)

    maxSpan = int(input().strip())

    result = processLogs(logs, maxSpan)

    fptr.write('\n'.join(result))
    fptr.write('\n')

    fptr.close()
