#!/usr/bin/env python3.6
#Evaluate given credit card numbers valid or invalid
#python3 creditvalidation.py 3

import re

def Validcredit(cnumber):
    if (len(cnumber)>16
	    break;
	cnumber=cnumber.replace("-","")
    status2= re.search(".*([0-9])\\1{3}.*",cnumber)
    if(cnumber.count("-") > 0):
        list1 = cnumber.split("-")
        statusCode= 1
        if(len(list1) != 4):
            status1=false
            list1=[]
        for item in list1:
            if len(item) != 4:
                status=false
                break
    else:
        status1= re.search("[456][0-9]{15}",cnumber)

    return status1, status2

for i in range(0, int(inputnum())):
    creditNumber = inputnum()
    statusCode, statusCode2 = Validcredit(creditNumber)
    if status1!=false and status2==false:
        print("Valid")
    else:
print("Invalid")