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
fig = plt.figure(figsize=(8, 6), dpi=200)
ax = fig.gca()
ax.plot_date(dates[good_values], ranks[good_values], "k-", tz=None,
             xdate=True, ydate=False, drawstyle="steps-post", zorder=100)
ax.set_title("Overwatch Ranks Over Time")
ax.set_xlabel("Date")
ax.set_ylabel("Rank")
ax.axhline(2000, c="gold", linewidth=2)
ax.axhline(2500, c="silver", linewidth=2)
ax.annotate("Plat", (Time("2018-04-15").plot_date, 2510))
seasons = ["2018-05-01", "2018-07-02", "2018-08-31", "2018-11-01"]
for i, date in enumerate(seasons):
    ax.axvline(Time(date).plot_date, c="b", linewidth=1, linestyle="--",
               alpha=0.8)
    ax.annotate(f"Season {i+10:.0f}", (Time(date).plot_date+5, 2250),
                rotation=90)
patches = np.arange(1.23, 1.33, 0.01)
patch_notes = ["Rialto", "Petra", "Symmetra rework", "Hammond",
               '"Support Update"', "Roadhog nerf",
               "Pharah buff", "Ashe", "Bastion buff", "Bastet"]
patch_dates = ["2018-05-03", "2018-05-22", "2018-06-26", "2018-07-24",
               "2018-08-09", "2018-09-11", "2018-10-09", "2018-11-13",
               "2018-12-11", "2019-01-08"]
for patch, note, date in zip(patches, patch_notes, patch_dates):
    ax.axvline(Time(date).plot_date, c="orange", alpha=0.8, linewidth=1,
               linestyle="--")
    ax.annotate(f"{patch:.2f}\n{note}", (Time(date).plot_date+15, 2775),
                xycoords="data", rotation=90,
                horizontalalignment="right", verticalalignment="top")

ax.set_ylim(2150, 2800)
fig.savefig("ow_ranks.png")
