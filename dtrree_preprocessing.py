import csv, copy
import random as rd


'''PARAMETERS:	data -> 2D List
				col -> col to remove'''
def delete_col(data, col):
	for row in data:
		del row[col-1]
	return data


def get_col(data, col):
	desired_col = []
	for rows in data:
		desired_col.append(data[rows][col-1])
	return desired_col


'''PARAMETERS: path -> csv file path'''
def open_csv_file(path):
	data = []
	with open(path) as csvfile:
		readCSV = csv.reader(csvfile, delimiter=',')
		for row in readCSV:
			data.append(list(row))
	return data


'''PARAMETERS: data -> 2D List'''
def str_to_float(data):
	for row in range(len(data)):
		for col in range(len(data[row])):
			data[row][col] = float(data[row][col])
	return data


def sort_entropy(dataset):
	for row in range(len(dataset)):
		if row == 0:
			continue
		dataset[row][4] = round(int(dataset[row][4]))
		if((dataset[row][4] % 10) >= 5):
			dataset[row][4] = dataset[row][4]+(10 - dataset[row][4]%10)
		else:
			dataset[row][4] = dataset[row][4]- (dataset[row][4]%10)

		dataset[row][5] = round(int(dataset[row][4]))
		if((dataset[row][5] % 10) >= 5):
			dataset[row][5] = dataset[row][5]+(10 - dataset[row][5]%10)
		else:
			dataset[row][5] = dataset[row][5]- (dataset[row][5]%10)

		dataset[row][7] = round(float(dataset[row][7]))
		dataset[row][8] = round(float(dataset[row][8]))

		dataset[row][4] = str(dataset[row][4])
		dataset[row][5] = str(dataset[row][4])
		dataset[row][7] = str(dataset[row][7])
		dataset[row][8] = str(dataset[row][8])

		dataset[row][9] = float(dataset[row][9])
		if dataset[row][9] > 3.5:
			dataset[row][9] = "good"
		else:
			dataset[row][9] = "bad"

	dataset.pop(0)

	return dataset


def sort_variance(data, cols):
	for row in range(len(data)):
		for col in cols:
			# data[row][col-1] = round_this(data[row][col-1])
			if col == 3:
				data[row][col-1] = round(data[row][col-1])
				continue
			elif col == 4:
				data[row][col - 1] = round_this(data[row][col - 1])
				continue
			elif col > 5 and not col > 20:
				data[row][col-1] = round(data[row][col-1], 1)
				continue
			elif col > 20 and not col > 28:
				data[row][col - 1] = round_this(data[row][col - 1])
				continue
			elif col == 29:
				data[row][col-1] = round(data[row][col-1], 1)
				continue
			elif col == 30:
				data[row][col-1] = round(data[row][col-1])
				continue
			elif col == 31 and col == 32 :
				data[row][col - 1] = round_this(data[row][col - 1])
				continue
			elif col == 33:
				data[row][col-1] = round(data[row][col-1])
				continue
			elif col > 33 and not col > 36:
				data[row][col-1] = round(data[row][col-1])
				continue
			elif col == 37:
				data[row][col-1] = round(data[row][col-1])
				continue
			elif col == 42:
				data[row][col-1] = round(data[row][col-1])
				continue
			elif col == 43:
				data[row][col - 1] = round_this(data[row][col - 1])
				continue
			elif col == 44:
				data[row][col-1] = round(data[row][col-1])
				continue
			elif col == 45:
				data[row][col-1] = round(data[row][col-1], 1)
				continue
	return data


def round_this(value):
	if value % 100 >= 50:
		value = value + (100 - (value % 100))
	else:
		value = value - (value % 100)
	return value


def bootstrap_sampling(data, rows=None):
	rd.seed(1)
	sample = []
	set = []
	for rows in range(rows):
		sample = copy.deepcopy(data[rd.randint(0,len(data))])
		set.append(sample)
	return set

