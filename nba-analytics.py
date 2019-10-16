import csv
import sys
import pandas as pd
import numpy as np
from collections import defaultdict
import argparse
from pprint import pprint
import operator




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
    #avg_20_plus_mins(filename)
    points_per_minutes(filename)
  
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


def points_per_minutes(filename):
    #given x minutes, and averaging n points
    #the result is player y scored n/x points per minute
    df = pd.read_csv(filename)

    df['MP'] = df['MP'].astype(int)
    df['Points'] = df['Points'].astype(int)

    dict_player_and_ppm = {}
    sorted_answer = {}
    curr_pts_div_mins = 0
    for index, player in df.iterrows():
        if(player['MP']!=0):
            curr_pts_div_mins = round(player['Points'] / player['MP'],2)
            dict_player_and_ppm[player['Name']] =  curr_pts_div_mins

    sorted_answer = sorted(dict_player_and_ppm.items(),key=operator.itemgetter(1))


    pprint(sorted_answer[::-1])

if __name__=="__main__":
    main()