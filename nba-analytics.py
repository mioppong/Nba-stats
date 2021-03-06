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




def main():
    #gets the file we are dealing with, and parses command line
    #arguments
    parser = argparse.ArgumentParser()
    parser.add_argument("filename", help="csv file")
    #parser.add_argument("firstname", help="firstname of choice")
    #parser.add_argument("lastname",help="lastname of player")

    args = parser.parse_args()
    filename = args.filename
    #firstname = args.firstname
    #lastname = args.lastname
    #player = firstname+" "+lastname

    #uses nbastats2018-2019.csv
    #avg_20_plus(filename)
    #avg_20_plus_mins(filename)
    #points_per_minutes(filename)
    #under_20_avg_20_plus(filename)
    #graph_weight_vs_blocks(filename)
    #plot_3_pct_vs_points(filename)
    #plot_usage_vs_points(filename)
    plot_mp_vs_points(filename)
    
    #uses nba-2018-2019-stats.csv
    #undrafted_15_pts(filename)
    #more_than_80_games(filename)


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

    for x in sorted_answer[::-1]:
        print(x, "points divided by time played")



def under_20_avg_20_plus(filename):
    df = pd.read_csv(filename)

    df.Age = df.Age.astype(int)
    df['Points'] = df['Points'].astype(int)

    for index, player in df.iterrows():
        if((player.Age <= 20) and (player.Points >= 20)):
            print(player.Name, "is age 20 or less, and averaged more than 20 Points")

def graph_weight_vs_blocks(filename):
    #compares weight to blocks
    df  = pd.read_csv(filename)

    plt.bar(df['Weight'],df['Blocks'],width=0.5)
    plt.title('Weight vs Blocks')
    plt.xlabel('Weight')
    plt.ylabel('Blocks')
    plt.show() 

def plot_3_pct_vs_points(filename):
    #prints out the average 3pt % in nba

    df = pd.read_csv(filename)

    plt.bar(df['FG%'], df['Points'], width=0.001)
    plt.xlabel('FG %')
    plt.ylabel('Points')
    plt.title("Points vs FG %")
    plt.show()

def plot_usage_vs_points(filename):
    df  = pd.read_csv(filename)

    plt.title("Usage vs Points")
    plt.bar(df['USG'], df['Points'], width=0.1)
    plt.xlabel('USAGE%')
    plt.ylabel('Points Avg')

    plt.show()


def plot_mp_vs_points(filename):
    df = pd.read_csv(filename)

    plt.bar(df['MP'],df['Points'],alpha=0.8,label='MP vs Points')
    plt.bar(df['USG'], df['Points'], alpha=0.4, label='USG vs Points')
    plt.legend()
    plt.show()

def undrafted_15_pts(filename):
    df = pd.read_csv(filename)
    df['PTS'] = df['PTS'].astype(int)

    for index,player in df.iterrows():
        if(player['DRAFT YEAR']=='Undrafted' and player['PTS'] > 15):
            print(player['PLAYER'])


def more_than_80_games(filename):
    df  = pd.read_csv(filename)
    list_more_than_80_games = []
    for index,player in df.iterrows():
        if (player['GP']>80):
            list_more_than_80_games.append(player['PLAYER'])

    print(list_more_than_80_games)
    print(str(len(list_more_than_80_games)) + " people played more than 80 games" )
if __name__=="__main__":
    main()