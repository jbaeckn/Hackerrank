import math
import os
import random
import re
import sys



if __name__ == '__main__':
    n = int(input())

    arr = list(map(int, input().rstrip().split()))
    arr.reverse()
    result_list = ""

    for i in range(n):
        result_list += str(arr[i]) + " "
    
    print(result_list.strip())
