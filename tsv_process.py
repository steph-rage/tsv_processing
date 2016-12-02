#!/usr/bin/python3

#Program written in python 3, intended to be called with a filename containing a TSV

import sys

#Read in the file passed as an arguement, and split it into a matrix by row and column
#If no file is passed in, the user will need to supply a file name

if len(sys.argv) > 1:
	tsv_file = open(sys.argv[1], 'r')
else:
	filename = input("Please enter the filename for the tsv file: ")
	tsv_file = open(filename, 'r')
rows = [line.rstrip('\n') for line in tsv_file]
data = [row.split('\t') for row in rows]

tsv_file.close()

#Finding the max and min both require first sorting the column, so this is written as
#a separate function which returns only the entries of a specific column, in order

def sort_column(column):
 	if column in data[0]:
 		index = data[0].index(column)
 		column_data = []
 		for row in data:
 			column_data.append(row[index])
 		column_data.pop(0)
 		column_data.sort()
 		return column_data
 	else:
 		print("That column doesn't exist!")
 		ask_user_for_command()
 		return False


def find_max(column):
 	entries = sort_column(column)
 	if entries:
 		print("\nThe maximum of {} is {}".format(column, entries[len(entries) - 1]))
 	else:
 		pass


def find_min(column):
	entries = sort_column(column)
	if entries:
		print("\nThe minimum of {} is {}".format(column, entries[0]))
	else:
		pass

#User interface which asks for commands and explains the possibilies if the user is confused

def ask_user_for_command():
	actions = {"max": [find_max, "Find the maximum of a column"], "min": [find_min, "Find the minimum of a column"]}
	to_do = input("\nWhat would you like to do next? ")
	if to_do in actions:
		col = input("\nOf which column? ")
		actions[to_do][0](col)
	else:
		print("\nThe available actions are:")
		for action, description in actions.items():
			print("{}: type {}".format(action, description[1]))
		ask_user_for_command()

#Run the program!
ask_user_for_command()
	
	
