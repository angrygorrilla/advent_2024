import argparse
import re
import os
import math
import copy


if __name__=='__main__':
    
    parser = argparse.ArgumentParser(
                        prog='advent_day_3',
                        description='find real multiply statements',
                        epilog='Text at the bottom of help')
    parser.add_argument('filename')
    args = parser.parse_args()
    file_name=args.filename
       
    with open(file_name) as file:
        lines = [line.rstrip() for line in file]
        
    all_text='\n'.join(lines)
    print(all_text)
    
    
    muls=[]
    for match in re.finditer("mul\(\d+\,\d+\)",all_text):
        muls.append(match[0])
    
    products=[]
    for equations in muls:
        numbers=[]
        for match in re.finditer("\d+",equations):
            numbers.append(match[0])
        products.append(int(numbers[0])*int(numbers[1]))
    
    #print(all_text)
    print(sum(products))
            

