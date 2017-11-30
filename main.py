import sys

import webbrowser
import random

import time

if __name__ == '__main__':

	with open('regulars.txt', 'r') as f:
		regular_list = f.read().split('\n')
	with open('irregulars.txt', 'r') as f:
		irregular_list = f.read().split('\n')
	with open('data.txt', 'r') as f:
		data_list = f.read().split('\n')
	
	if(len(sys.argv) == 1):
		n_regulars = 1
		n_irregulars = 3
		n_data = 2
	if((len(sys.argv) == 2) | (len(sys.argv) == 3) | (len(sys.argv) > 4)):
		"Please include number of regular sources and number of irregular sources you would like to see."
		"For example, python main.py 2 4 will retrieve 2 regular and 4 irregular sources"
		"Passing no arguments will use 1 regular and 3 irregular sources"
	if(len(sys.argv) ==4):
		n_regulars = sys.argv[1]
		n_irregulars = sys.argv[2]
		n_data = sys.argv[3]

	regular_open_list = random.sample(regular_list, n_regulars)
	irregular_open_list = random.sample(irregular_list, n_irregulars)
	data_open_list = random.sample(data_list, n_data)

	for regular in regular_open_list:
		webbrowser.open_new(regular)
	time.sleep(0.1)
	for irregular in irregular_open_list:
		webbrowser.open_new_tab(irregular)
	time.sleep(0.1)
	for data in data_open_list:
		webbrowser.open_new_tab(data)