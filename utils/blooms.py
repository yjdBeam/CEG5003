# -*- coding: utf-8 -*-
# @Author   : jundong.yao
# @Time     : 2023/9/26 11:19
# @File     : csv_utils
# @Project  : Project for Network IDS
# @brief    : logic for bloom filter

from config import *
from utils.csv_utils import *
import csv
import math
import mmh3
from bitarray import bitarray


def create_bloom_filter(rows, fp_rate, num_hashes):
    """
    :param rows: rows of data
    :param fp_rate: false positive rate (误判率)
    :param num_hashes: num of hash functions
    :return:
    """
    # Create a Bloom filter with the given rows, false positive rate, and number of hashes
    num_rows = len(rows)
    num_bits = int(-(num_rows * math.log(fp_rate)) / (math.log(2) ** 2))
    filter = bitarray(num_bits)
    filter.setall(0)  # init with 0
    for row in rows:
        for i in range(num_hashes):
            hash_value = mmh3.hash(str(row).encode('utf-8'), i) % num_bits
            filter[hash_value] = 1
    return filter, num_bits, num_hashes

def check_bloom_filter(filter, row, num_bits, num_hashes):
    # Check if a row is in the Bloom filter
    for i in range(num_hashes):
        hash_value = mmh3.hash(str(row).encode('utf-8'), i) % num_bits
        if not filter[hash_value]:
            return False
    return True

if __name__ == '__main__':
    # Parameters
    fp_rate = 0.01
    num_hashes = 4

    # Read the rows from the CSV files
    association_rules = read_csv_file('association_rules.csv')
    association_rules_rep = read_csv_file('association_rules_rep.csv')

    # Create a Bloom filter for the rows in association_rules_rep.csv
    filter, num_bits, num_hashes = create_bloom_filter(association_rules_rep, fp_rate, num_hashes)

    # Check the rows in association_rules.csv against the Bloom filter
    new_rows = []
    for row in association_rules:
        if not check_bloom_filter(filter, row, num_bits, num_hashes) and row not in association_rules_rep:
            new_rows.append(row)

    # Append the new rows to association_rules_rep.csv
    association_rules_rep += new_rows
    write_csv_file('association_rules_rep.csv', association_rules_rep)

    # Print the number of new rows added
    print('Number of new rows added to association_rules_rep.csv:', len(new_rows))