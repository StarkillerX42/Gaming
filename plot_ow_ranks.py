import matplotlib.pyplot as plt
import numpy as np
from astropy.time import Time
dates = []
ranks = []
with open("ow_ranks.txt", "r") as rank_fil:
    for i, line in enumerate(rank_fil):
        date, rank = line.split(":")
        dates.append(Time(date).plot_date)
        ranks.append(int(rank))
dates = np.array(dates)
ranks = np.array(ranks)
good_values = ranks != 0
fig = plt.figure(figsize=(8, 6))
ax = fig.gca()
ax.plot_date(dates[good_values], ranks[good_values],"-", tz=None,
             xdate=True, ydate=False, drawstyle="steps-post")
ax.set_title("Overwatch Ranks Over Time")
ax.set_xlabel("Date")
ax.set_ylabel("Rank")
ax.axhline(2000, c="gold", linewidth=0.5)
ax.axhline(2500, c="green", linewidth=2)
ax.set_ylim(2200, 2700)
fig.savefig("ow_ranks.png")
