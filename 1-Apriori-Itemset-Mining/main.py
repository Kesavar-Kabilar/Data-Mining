from itertools import combinations
import numpy as np
from collections import Counter
from time import time

start = time()

transactions = []
with open("categories.txt", "r") as file:
    for line in file: 
        line = line.strip('\n').split(";")
        transactions.append(set(line))

minimum_support_count = 771

# transactions = [
#     {"Bread", "Nuts", "Donuts"}, 
#     {"Bread", "Cookies", "Donuts"}, 
#     {"Bread", "Donuts", "Eggs", "Milk"}
# ]

# minimum_support_count = 1


def support(itemset, transactions=transactions):
    return sum(map(set(itemset).issubset, transactions))

def apriori(transactions=transactions, minimum_support_count=minimum_support_count):
    all_frequent_itemsets = {}

    one_itemsets = Counter([char for tran in transactions for char in tran])
    one_itemsets = {(k,) : v for k, v in one_itemsets.items() if v >= minimum_support_count}

    one_itemsets = dict(sorted(one_itemsets.items(), key=lambda item: item[1]))
    # for k, v in one_itemsets.items():
    #     print(f"{v}:{";".join(k)}")

    all_frequent_itemsets.update(one_itemsets)

    cur_itemsets = one_itemsets
    while cur_itemsets != {}:
        next_itemsets = {}

        for k, _ in cur_itemsets.items():
            for k2, _ in one_itemsets.items():
                if k2[0] not in k:
                    new_k = tuple(sorted(list(k) + list(k2)))
                    if new_k not in next_itemsets and support(new_k) >= minimum_support_count:
                        next_itemsets[new_k] = support(new_k)
        
        next_itemsets = dict(sorted(next_itemsets.items(), key=lambda item: item[1]))
        # for k, v in next_itemsets.items():
        #     print(f"{v}:{";".join(k)}")

        all_frequent_itemsets.update(next_itemsets)
        cur_itemsets = next_itemsets
    
    return all_frequent_itemsets

all_frequent_itemsets = apriori()



with open('patterns.txt', 'w+') as file:
    for k, v in all_frequent_itemsets.items():
        file.write(f"{v}:{";".join(k)}\n")


print(time() - start)