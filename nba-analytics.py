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

    print(player)
  
def funcname(self, parameter_list):
    pass




if __name__=="__main__":
    main()