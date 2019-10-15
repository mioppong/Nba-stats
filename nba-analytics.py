import csv
import sys
import pandas as pd
import numpy as np
from collections import defaultdict
import argparse





def main():
    #gets the file we are dealing with, and parses command line
    #arguments
    parser = argparse.ArgumentParser()
    parser.add_argument("filename", help="csv file")
    parser.add_argument("firstname", help="firstname of choice")
    parser.add_argument("lastname",help="lastname of player")

    args = parser.parse_args()
    filename = args.filename
    firstname = args.firstname
    lastname = args.lastname
    player = firstname+" "+lastname

    #uses nbastats2018-2019.csv
    #avg_20_plus(filename)
    avg_20_plus_mins(filename)
  
def avg_20_plus(filename):
    #returns players who avged more than 20 points
    df = pd.read_csv(filename)

    df['Points'] = df['Points'].astype(int)
    list_20_plus = []
    for index,player in df.iterrows():
        if (player["Points"] >= 20):
            list_20_plus.append(player)
            print(player["Name"])
    print(len(list_20_plus),"people averages over 20 pts")

def avg_20_plus_mins(filename):
    df = pd.read_csv(filename)

    list_30_plus_mins = []
    df['MP'] = df['MP'].astype(int)
    
    for index,player in df.iterrows():
        if(player['MP']>=30):
            list_30_plus_mins.append(player)
            print(player.Name)
    print(str(len(list_30_plus_mins))," players play 30 plus mins")


if __name__=="__main__":
    main()