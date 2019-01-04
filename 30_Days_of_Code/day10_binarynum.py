import math
import os
import random
import re
import sys


if __name__ == '__main__':
    n = int(input())
    binary_num = bin(n)[2:]
    print(len(max(binary_num.split('0'))))
