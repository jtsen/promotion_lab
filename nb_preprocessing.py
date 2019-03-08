import csv, copy
import random as rd


# def discretize_cluster_type(data):
# 	for row in data:
# 		if row[len(data)-3] > 6:
#


def find_unique_col_values(data):
	unique_items = [[]] * len(data[0])
	for i in range(len(data[0])):
		curr_col = []
		for row in data:
			if row[i] not in curr_col:
				curr_col.append(row[i])
		unique_items[i] = copy.deepcopy(curr_col)
	return unique_items


def prob_to_numeric(data):
	for row in data:
		for i in range(5,20):
			row[i] = row[i] * row[2]
	return data


def prob_round(data):
	for row in data:
		row[28] = round(row[28], 1)
		row[32] = round(row[32], 1)
	return data


def calc_cardinality(list):
	cardinality_list = []
	for row in list:
		cardinality_list.append(len(row))
	return cardinality_list


'''PARAMETERS:	data -> 2D List
				col -> col to remove'''
def delete_col(data, col):
	for row in data:
		del row[col-1]
	return data


def get_col(data, col):
	desired_col = []
	for rows in data:
		desired_col.append(rows[col-1])
	return desired_col


'''PARAMETERS: path -> csv file path'''
def open_csv_file(path):
	data = []
	with open(path) as csvfile:
		readCSV = csv.reader(csvfile, delimiter=',')
		for row in readCSV:
			data.append(row)
	data.pop(0)
	return data


'''PARAMETERS: data -> 2D List'''
def str_to_float(data):
	for row in range(len(data)):
		for col in range(len(data[row])):
			data[row][col] = float(data[row][col])
	return data



def bootstrap_sampling(data, rows=None):
	rd.seed(1)
	sample = []
	set = []
	for rows in range(rows):
		sample = copy.deepcopy(data[rd.randint(0,len(data))])
		set.append(sample)
	return set

