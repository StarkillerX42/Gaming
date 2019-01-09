"""This function grabs my overwatch rank and saves it to a file"""
import requests
import datetime
import os
now = datetime.datetime.now()
print("Get OW Rank started at {}".format(now))

data = requests.get("https://ow-api.com/v1/stats/pc/us/Starkiller42-11691/profile")
# print(data.json())
try:
    rank = int(data.json()["rating"])
except:
    rank = 0

rankpath = os.path.join(os.path.dirname(
        os.path.abspath(__file__)), "ow_ranks.txt")
# print(rankpath)
with open(rankpath, "r") as fil:
    lines = fil.readlines()
    if str(now.date()) not in lines[-1]:
        needrank = True
    else:
        needrank = False
if needrank:
    with open(rankpath, "a") as fil:
        print("    Writing new SR")
        fil.write("{}: {}\n".format(now.date(), rank))
else:
    print("    SR already written today")

