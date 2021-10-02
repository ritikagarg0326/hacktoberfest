# hacktoberfest
hacktoberfest 2021.Create a pull request in this repository,fix the issue and have a chance to win hacktoberfest tshit 2021.
It's a simple problem based on hashing.
#problem name:=Sign in sign out
#hackerrank problem
#hackathon
#quesion:Sign-in Sign-out Logs
Application logs are used in analysis of interactions
with an application and may be used to detect
specific actions.
A log file is provided as a string array where each
entry is in the form "user_id timestamp action". Each
of the values is separated by a space.
• Both user_id and timestamp consist only of digits,
are at most 9 digits long and start with a non-zero
digit.
timestamp represents the time in seconds since the
application was last launched

• action will be either "sign-in" or "sign-out"

Given a log with entries in no particular order,
return an array of strings that denote user_id's of
users who signed out in maxSpan seconds or less
after signing in.

#Example

n=7

logs = ["30 99 sign-in", "30 105 sign-out", "12 100
sign-in", "20 80 sign-in", "12 120 sign-out", "20 101
sign-out", "21 110 sign-in"]
an=20





-#!/bin/python3

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

