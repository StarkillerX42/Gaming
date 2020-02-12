#!/usr/bin/env python3
"""This function grabs my overwatch rank and saves it to a file"""
import requests
import datetime
from pathlib import Path
import starcoder42 as s

now = datetime.datetime.now()
print("Get OW Rank started at {}".format(now))

pc = {'tank': 0, 'damage': 0, 'support': 0}
try:
    data = requests.get("https://ow-api.com/v1/stats/pc/us/Starkiller42-11691/"
                        "profile")
    # print(data.json())
    # try:
    ranks = data.json()["ratings"]
    for rank in ranks:
        pc[rank['role']] = rank['level']
except Exception as e:
    s.iprint(e, 1)

xbox = {'tank': 0, 'damage': 0, 'support': 0}

try:
    data = requests.get("https://ow-api.com/v1/stats/xbl/Starkiller625/profile")
    # print(data.json())
    # try:
    xranks = data.json()["ratings"]
    ranks = data.json()["ratings"]
    for rank in xranks:
        xbox[rank['role']] = rank['level']
except Exception as e:
    s.iprint(e, 1)

rank_path = (Path(__file__).parent / "ow_rolelock_ranks.txt").absolute()
# print(rank_path)

if not rank_path.exists():
    rank_path.touch()

with open(rank_path, "r") as fil:
    lines = fil.readlines()
    if str(now.date()) not in lines[-1]:
        need_rank = True
    else:
        need_rank = False

if need_rank:
    with open(rank_path, "a") as fil:
        print("    Writing new SR")
        fil.write("{}: {}: {}: {}: {}: {}: {}\n".format(now.date(), pc['tank'],
                                                        pc['damage'],
                                                        pc['support'],
                                                        xbox['tank'],
                                                        xbox['damage'],
                                                        xbox['support']))
else:
    print("    SR already written today")
