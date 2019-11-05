#!/usr/bin/env python3
"""This function grabs my overwatch rank and saves it to a file"""
import requests
import datetime
import os
now = datetime.datetime.now()
print("Get OW Rank started at {}".format(now))

data = requests.get("https://ow-api.com/v1/stats/pc/us/Starkiller42-11691/"
                    "profile")
# print(data.json())
except Exception:
    rank = 0

data = requests.get("https://ow-api.com/v1/stats/xbl/Starkiller625/profile")
# print(data.json())
try:
    xbl_rank = int(data.json()["rating"])
except Exception:
    xbl_rank = 0

rank_path = os.path.join(os.path.dirname(
        os.path.abspath(__file__)), "ow_ranks.txt")
# print(rank_path)
with open(rank_path, "r") as fil:
    lines = fil.readlines()
    if str(now.date()) not in lines[-1]:
        need_rank = True
    else:
        need_rank = False
if need_rank:
    with open(rank_path, "a") as fil:
        print("    Writing new SR")
        fil.write("{}: {}: {}\n".format(now.date(), rank, xbl_rank))
else:
    print("    SR already written today")
