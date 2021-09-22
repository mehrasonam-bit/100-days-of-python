#***************************************************
# Name: Sonam Mehra
# Bus Stop Findings
#
#
#***************************************************
###########
# QUESTION 5
############

#import packages
import urllib.request
import json


#input a store number
stop=input("Enter the stop number for which you need information: ")
url = f'https://dataportal.greatersudbury.ca/api/v2/stops/{stop}?auth_token=e0c2f2c209513b79947d4c149b85dead'

response = urllib.request.urlopen(url)
result = json.loads(response.read())


#next buses from the stop
print("Next buses from the stop are:")
length=len(result["stop"]["calls"])
#to get the information about next buses
for i in range(length):
   bus_no=result["stop"]["calls"][i]["route"]
   what_time=result["stop"]["calls"][i]["passing_time"]
   route=result["stop"]["calls"][i]["destination"]["name"]
   print(f"Bus Number: {bus_no} on route  {route} at {what_time}")








