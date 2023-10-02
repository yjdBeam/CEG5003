# -*- coding: utf-8 -*-
# @Author   : jundong.yao
# @Time     : 2023/9/26 11:19
# @File     : csv_utils
# @Project  : Project for Network IDS
# @brief    : utils for csv files

from config import *
import csv

def get_shape(filename):
    file_path = ASSOCIATION_RULES + '/' + filename
    with open(file_path, 'r') as file:
        reader = csv.reader(file)
        rows = sum(1 for row in reader)
        file.seek(0) # Reset the file pointer to the beginning
        cols = len(next(reader))
    print("Shape of {}: {} rows x {} columns".format(filename, rows, cols))
    return (rows, cols)

def read_csv_file(filename):
    # Read a CSV file and return the rows as a list
    file_path = ASSOCIATION_RULES + '/' + filename
    with open(file_path, 'r') as csvfile:
        reader = csv.reader(csvfile)
        rows = list(reader)
    return rows

def write_csv_file(filename, data):
    # Write data to a CSV file
    file_path = ASSOCIATION_RULES + '/' + filename
    with open(file_path, 'w', newline='') as csvfile:
        writer = csv.writer(csvfile)
        writer.writerows(data)

if __name__ == '__main__':
    get_shape("association_rules.csv")
    get_shape("association_rules_live_data.csv")
    get_shape("association_rules_rep.csv")
