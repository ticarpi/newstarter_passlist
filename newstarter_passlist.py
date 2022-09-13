#!/usr/bin/env python3

###########################################
# Generate password lists for new starter #
#   accounts in AD environments           #
# Written by Andy Tyler (@ticarpi)        #
###########################################

import re
import sys
import argparse
import datetime

parser = argparse.ArgumentParser(description='Generate password lists for commonly set New Starter account passwords.')
parser.add_argument('-o','--outputfile', help="name of the output list", action="store")
parser.add_argument('-d','--depth', help="how many years to backdate the search", type=int, action="store", default=1)
parser.add_argument('-a','--additionalwords', help="words to add to the existing common base words list. For example: company name, office location. Note: can add multiple", action="append")
args = parser.parse_args()
passwords_building = []
dates_building = []
symbol_building = ['!'] # consider adding other symbols  as appropriate. e.g.: '?','@'

def output_passwords():
    if args.outputfile:
        with open(args.outputfile, "w") as outfile:
            for password in passwords_building:
                outfile.write(password+'\n')
    else:
        for password in passwords_building:
            print(password)

def build_passwords():
    if args.additionalwords:
        for additional in args.additionalwords:
            append_nums(additional.lower())
            append_nums(additional.capitalize())
    with open('basewords.txt','r') as basewords:
        for word in basewords.readlines():
            append_nums(word.lower())
            append_nums(word.capitalize())

def append_nums(word):
    numbers_building = []
    for number in ['1','2','3','123','1234','12345']:
        numbers_building.append(number)
    for date in dates_building:
        numbers_building.append(date)
    for append in numbers_building:
        passwords_building.append(word.rstrip()+str(append))
        for symbol in symbol_building:
            passwords_building.append(word.rstrip()+str(append)+symbol)

def build_dates(depth=1):
    curyear = str(datetime.date.today().year)
    curyear_short = curyear[2:4]
    if depth > 1:
        diffyr = depth - 1
        while diffyr > 0:
            dates_building.append(int(curyear)-diffyr)
            dates_building.append(int(curyear_short)-diffyr)
            diffyr -= 1
    dates_building.append(curyear)
    dates_building.append(curyear_short)
            

def main():
    build_dates(args.depth)
    build_passwords()
    output_passwords()
    
if __name__ == '__main__':
    main()
exit()
