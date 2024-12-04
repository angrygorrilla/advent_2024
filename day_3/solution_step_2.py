import argparse
import re
import os
import math
import copy

def multiplier(text):
    numbers=[]
    for match in re.finditer("\d+",text):
        numbers.append(match[0])
    return(int(numbers[0])*int(numbers[1]))



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
    for match in re.finditer("(do\(\))|(don't\(\))|(mul\(\d+\,\d+\))",all_text):
        muls.append(match[0])
    
 
products=[] 
last_item='do()'
for item in muls:
    print(item)
    if item=="don't()" or item == "do()":
        last_item=item
    else:
        print(item)
        if last_item=='do()':
            products.append(multiplier(item))
            
print(sum(products))
    
    
            

