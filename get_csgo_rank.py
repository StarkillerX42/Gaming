#!/home/pi/berryconda3/bin/python
"""This function grabs my CS:GO rank and saves it to a file"""
import requests
import datetime
import os
now = datetime.datetime.now()
print("Get CS:GO Rank started at {}".format(now))

data = requests.get("http://api.steampowered.com/ISteamUserStats/GetUserStatsFo"
                    "rGame/v0002/?appid=730&key=E65AB2D9A4C8C42DCEEBCCD8D56BF02"
                    "9&steamid=76561198199499279")
# Because CSGO's format sucks, I reformat it into my own dictionary
dumb_stats = data.json()["playerstats"]["stats"]
stats = {}
for i, elem in enumerate(dumb_stats):
    stats[elem["name"]] = elem["value"]

# print("\n".join(stats.keys()))
try:
    kdr = stats["total_kills"]/stats["total_deaths"]
except Exception:
    kdr = None
try:
    kills_per_round = stats["total_kills"]/stats["total_rounds_played"]
except Exception:
    kills_per_round = None
try:
    rank = stats["skill_group"]
except Exception:
    rank = None

archive_path = os.path.join(os.path.dirname(os.path.abspath(__file__)),
                            "csgo_data.txt")
with open(archive_path, "r") as fil:
    lines = fil.readlines()
    if str(now.date()) not in lines[-1]:
        need_rank = True
    else:
        need_rank = False

if need_rank:
    with open(archive_path, "a") as fil:
        print("    Writing new SG")
        fil.write(f"{now.date()}, {kdr:.3f}, {kills_per_round:.0f}, {rank}\n")
else:
    print("    SG already written today")
