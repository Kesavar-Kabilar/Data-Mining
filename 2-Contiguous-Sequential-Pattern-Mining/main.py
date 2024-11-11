from itertools import combinations
import numpy as np
from collections import Counter
from time import time

start = time()

# transactions = []
# with open("small.txt", "r") as file:
#     for line in file: 
#         line = line.strip('\n').split(" ")
#         transactions.append(list(line))

# minimum_support_count = (2/3)*len(transactions)

transactions = []
with open("reviews_sample.txt", "r") as file:
    for line in file: 
        line = line.strip('\n').split(" ")
        transactions.append(list(line))

minimum_support_count = (0.01)*len(transactions)

def get_one_itemset(transactions=transactions, minimum_support_count=minimum_support_count):
    one_itemsets = Counter([char for tran in transactions for char in list(set(tran))])
    one_itemsets = {k : v for k, v in one_itemsets.items() if v >= minimum_support_count}
    
    one_itemsets = dict(sorted(one_itemsets.items(), key=lambda item: item[1]))
    return one_itemsets, set(one_itemsets.keys())


def k_window(k, one_itemsets_keys, transactions=transactions, minimum_support_count=minimum_support_count):
    new_trans = []
    for line in transactions:
        new_trans_line = set()
        for i in range(0, len(line)-k+1):
            if set(line[i:i+k]).issubset(one_itemsets_keys):
                new_trans_line.add(tuple(line[i:i+k]))
        new_trans.extend(new_trans_line)
    k_itemsets = Counter(new_trans)
    k_itemsets = {k : v for k, v in k_itemsets.items() if v >= minimum_support_count}
    return k_itemsets

def get_cont_sequence(transactions=transactions, minimum_support_count=minimum_support_count):
    all_itemsets = {}

    one_itemsets, one_itemsets_keys = get_one_itemset()
    one_itemsets = dict(sorted(one_itemsets.items(), key=lambda item: (item[1], item[0])))
    all_itemsets.update(one_itemsets)
    k = 2

    cur_itemsets = one_itemsets
    while cur_itemsets != {}:
        cur_itemsets = k_window(k, one_itemsets_keys, transactions, minimum_support_count)
        cur_itemsets = dict(sorted(cur_itemsets.items(), key=lambda item: (item[1], item[0])))
        all_itemsets.update(cur_itemsets)
        k+=1
    
    return all_itemsets

d = get_cont_sequence()
with open('patterns.txt', 'w+') as file:
    for k, v in d.items():
        if type(k) == str:
            file.write(f"{v}:{k}\n")
        else:
            file.write(f"{v}:{";".join(k)}\n")

print(time() - start)