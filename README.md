# NBA Analytics

With this project, I just asnwer basic NBA questions, based on stats from the 2018-2019 season. Like who average most points, how many players avg more than 20pts, and random things like that.

## Getting Started

These instructions will get you a copy of the project up and running on your local machine for development and testing purposes. See deployment for notes on how to deploy the project on a live system.

Basically you will need python installed, hopefully above 3.6, along with these libraries.

```
import csv
import sys
import pandas as pd
import numpy as np
from collections import defaultdict
import argparse
from pprint import pprint
import operator
import matplotlib.pyplot as plt
import math
```


### Running program

In the code, there are lines with
```
#uses nbastats2018-2019.csv
avg_20_plus_mins(filename)
points_per_minutes(filename)
```
or
```
#uses nba-2018-2019-stats.csv
undrafted_15_pts(filename)
more_than_80_games(filename)
```

To run certain functions, we will require either nbastats2018-2019.csv, or nba-2018-2019-stats.csv.

so for example if we want to find the undrafted players who averaged more than 15 pts in the 2018-2019 season, the code above tells us to use nba-2018-2019-stats.csv, so we will first uncomment that function, then

```
python nba-analytics.py nba-2018-2019-stats.csv
```

## Future Work
* In the future, I want to stray away from csv files, and scrape everything from the web, or use a library which does that

* I want to be able to get certain stats from whichever year, just write the function for it, and supply the data/stats/csv file through scraping basketball-reference


## Acknowledgments

* https://www.basketball-reference.com/
* NBA.com

## Author
* Michael Oppong