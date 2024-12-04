import argparse
import re
import os
import math

parser = argparse.ArgumentParser(
                    prog='list_counter',
                    description='add the sum of the differences for a list',
                    epilog='Text at the bottom of help')
parser.add_argument('filename')     

if __name__=='__main__':
    args = parser.parse_args()
    file_name=args.filename
    a_list=[]
    b_list=[]
    
    
    with open(file_name) as file:
        lines = [line.rstrip() for line in file]
        
    for line in lines:
        nums=[]
        for match in re.finditer("\d+",line):
            nums.append(int(match[0]))
        a_list.append(int(nums[0]))
        b_list.append(int(nums[1]))
        
    a_list.sort()
    b_list.sort()
    
    sums=[ abs(a_list[i] - b_list[i]) for i in range(len(a_list))]
    print(sum(sums))
    