"""This function grabs my overwatch rank and saves it to a file"""
import requests
import datetime
import os
now = datetime.datetime.now()
print("Get OW Rank started at {}".format(now))

data = requests.get("http://api.steampowered.com/ISteamUserStats/GetUserStatsFo"
                    "rGame/v0002/?appid=730&key=E65AB2D9A4C8C42DCEEBCCD8D56BF02"
                    "9&steamid=76561198199499279")
dumb_stats = data.json()["playerstats"]["stats"]  # Because CSGO's format sucks
stats = {}
for i, elem in enumerate(dumb_stats):
    stats[elem["name"]] = elem["value"]

print("\n".join(stats.keys()))
kdr = stats["total_kills"]/stats["total_deaths"]
kills_per_round = stats["total_kills"]/stats["total_rounds_played"]
