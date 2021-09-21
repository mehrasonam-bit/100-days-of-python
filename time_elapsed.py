import json
import time
from os import system,name

def clear(): 
    if name == 'nt': 
        _ = system('cls') 
    else: 
        _ = system('clear') 

current_time = time.time() 

filename = 'time.json'
try:
    with open(filename) as f_obj:
        results = json.load(f_obj)
except FileNotFoundError:
    with open(filename, "w") as f_obj:
        json.dump(current_time, f_obj)
except NameError:
    with open(filename, "w") as f_obj:
        json.dump(current_time, f_obj)                
print("Starting Time")
print("\t",results)
print("\t",time.ctime(results))
print("The time now")
elapsedtime = time.time() 
print("\t",elapsedtime)
print("\t",time.ctime(elapsedtime))
print("\t",elapsedtime - results, "seconds")

money = 1_000_000
year = money * 0.023
month = year / 12
week = month / 4
day = week / 7
hour = day / 24
minute = hour / 60
second = minute / 60

while True:
    elapsedtime = time.time() - results
    print("========================================================")
    print("Elapsed time",round(elapsedtime,2),"seconds",round(elapsedtime/60,2),"minutes")
    print(f"Starting amount ${money:,}")
    print("This year you can expect to earn:")
    print(f"${round(year,2)} per year, ${round(month,2)} per month, ${round(week,2)} per week")
    print(f"${round(day,2)} per day, ${round(hour,2)} per hour, ${round(minute,2)} per minute")
    print(f"${round(second,5)} per second")
    print("========================================================")
    print(f"You have earned ${round(second * elapsedtime,2)}")
    print("========================================================")
    time.sleep(1)
    clear()
