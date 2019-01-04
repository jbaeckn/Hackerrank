import math
import os
import random
import re
import sys



if __name__ == '__main__':
    arr = []

    for _ in range(6):
        arr.append(list(map(int, input().rstrip().split())))
    
    hourglass = []
    for j in range(4):
        for i in range(4):
            first = arr[j][i:i+3]
            second = arr[j+1][i+1]
            third = arr[j+2][i:i+3]
            hourglass.append((first,second,third))

    sum_list = []
    for k in range(len(hourglass)):
        sum_list.append(sum(hourglass[k][0]) + hourglass[k][1] + sum(hourglass[k][2]))

    print(max(sum_list))
