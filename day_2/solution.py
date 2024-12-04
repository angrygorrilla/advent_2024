import argparse
import re
import os
import math
import copy

def line_safety(line):
    print(line)
    differences_line=[]
    for i in range(len(line)-1):
         differences_line.append(line[i+1]-line[i])
    
    if (all(item>0 for item in differences_line) or all(item<0 for item in differences_line)) and all(abs(item)<4 and abs(item)>0 for item in differences_line):
            print('safe')
            return('safe')
    else:
        for index,element_removal_option in enumerate(line):
            print('removal :' + str(element_removal_option))
            line_copy=copy.deepcopy(line)
            
            
            line_copy.pop(index)
            print(line_copy)
            differences_line=[]
            for i in range(len(line_copy)-1):
                differences_line.append(line_copy[i+1]-line_copy[i])
            
            print(line_copy)
            if (all(item>0 for item in differences_line) or all(item<0 for item in differences_line)) and all(abs(item)<4 and abs(item)>0 for item in differences_line):
                return('safe')
    return('unsafe')


if __name__=='__main__':
    
    parser = argparse.ArgumentParser(
                        prog='list_counter',
                        description='add the sum of the differences for a list',
                        epilog='Text at the bottom of help')
    parser.add_argument('filename')     
    args = parser.parse_args()
    file_name=args.filename
       
    with open(file_name) as file:
        lines = [line.rstrip() for line in file]

    number_lines=[]    
    for line in lines:
        nums=[]
        for match in re.finditer("\d+",line):
            nums.append(int(match[0]))
        number_lines.append(nums)


    safes=[]

    for line in number_lines:
        safes.append(line_safety(line))

    print(safes.count('safe'))
            

