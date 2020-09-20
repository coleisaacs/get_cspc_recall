#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""

__description__  = "Pulls recall information from the Consumer Product
                    Safety Commision (CSPC) and outputs to a formatted (.docx)."
__author__ = "Cole Isaacs"
__credits__ = "Cole Isaacs"
__license__ = "GNU GPLv3 except dependencies where their licenses apply."
__dependencies__ = "CSCPC API, Python packages: python-docx, requests."
__version__ = "1.0.1"
__maintainer__ = "Cole Isaacs"
__email__ = "coleisaacs@gmail.com"
__status__ = "Production"
__notes__  = "CSCPC API: https://cpsc.gov/Recalls/
                         CPSC-Recalls-Application-Program-Interface-API-Information
             "

"""

# Import dependencies. 

import json
import requests
from datetime import date
from docx import Document
from docx.shared import Inches


# Get current date and rewind one year for starting timeframe of recall list.

getCurDate = date.today()
year = getCurDate.year - 1
month = getCurDate.month
day =  getCurDate.day

date = str(year) + "-" + str(month) + "-" + str(day)

# CSCPC API URI parameters.

apiCSCPC = "http://www.saferproducts.gov/RestWebServices/Recall?"
apiParam = "format=json&RecallDateStart=" + str(date)
apiCall = apiCSCPC + apiParam

#  Filename to save to for API output

saveOut = 'recall_' + str(date) + '.docx'

def getDate(date):
    """
    Check date and if not OK, prompt to correct.

    """
    while True:
        print("Use " + date + " as the date?")
        ans = input("Enter Y or y for Yes and N or n for No: ")


        if ('y' == ans) or \
           ('Y' == ans) or \
           ('n' == ans) or \
           ('N' == ans):
               
           # If valid no action.
           
            print("OK. ")
            break
        
   
    if ("n" == ans) or ("N" == ans):
        
    # Validate user entry.
    
            while True:
                year = input("Enter year (4-digit/YYYY): ")
                month = input("Enter month (2-digit/MM): ")
                day =  input ("Enter day (2-digit/DD): ")

                try:
                    year = int(year)
                    month = int(month)
                    day = int(day)
                    

                except:
                    print(
                        "Please enter 4 digits for year, \
                         and 2 digits for month and day. "
                        )
                    continue

                if (0 >= month) or \
                   (13 <= month) or \
                   (0 >= day) or \
                   (32 <= day) or \
                   (getCurDate.year < year):

                    # If out of range restart loop
                    
                    print("Invalid entry.")
                    continue

                else:
                    
                    # Set date to string and format for API call.
                    year = str(year)
                    month = str(month)
                    day = str(day)

                if(2 == len(month)) and (2 == len(day)):
                    date = year + "-" + month + "-" + day

                else:
                    date = year + "-0" + month + "-0" + day
                
                break


    return date
            

# Confirm starting date for recall timeframe.
date = getDate(date)


# TODO: Parse JSON

req =  https://www.saferproducts.gov/RestWebServices/Recall?format=json&RecallDateStart=2020-09-11

request = requests.get(URI).json()
request[0]['RecallID']

# Get timeframe, default to 11/1/(current year - 1) - 10/31/(current year)
# http://www.saferproducts.gov/RestWebServices/Recall?format=json&RecallDateStart=2019-11-01

"""
Keys:
json[#]["Products"][#]["Name"]
json[#]["Hazards"][#]["Name"]

json[#]["Description"]                              #Tables Regex?
json[#]["Retailers"][#]["Name"]

json[#]["Remedies"][#]["Name"]
json[#]["ConsumerContact"]

json[#]["Images"][#++]["URL"]



request[0]["Products"][0]["Name"]
request[0]["Hazards"][0]["Name"]
request[0]["Remedies"][0]["Name"]
request[0]["Description"]
request[0]["Retailers"][0]["Name"]
request[0]["ConsumerContact"]
request[0]["Images"][0]["URL"]


"""


# TODO:  .docx formatting

document = Document()

p = document.add_paragraph('Name of Product')
p = document.add_paragraph('Hazard:')
p = document.add_paragraph('Hazard Details')
p = document.add_paragraph('Description'))
document.add_picture('monty-truth.png', width=Inches(1))

document.save(saveOut)


