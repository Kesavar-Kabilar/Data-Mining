## Apriori Algorithm for Frequent Itemset Mining - README.md

### Description

This program implements the Apriori algorithm to discover frequently occurring category combinations from a real-world dataset. This information can be used for market basket analysis, recommendation systems, and understanding user behavior patterns.

### Algorithm

The Apriori algorithm is an iterative approach for discovering frequent itemsets. It utilizes the following principles:

* **Anti-Monotonicity:** If a set of items is infrequent, then all its supersets (sets containing all the items and potentially more) must also be infrequent.
* **Candidate Generation:** The algorithm starts by identifying frequent single items (length-1 sets) and iteratively generates candidate sets of increasing lengths by joining frequent sets of the previous iteration.
* **Support Counting:** Each candidate set's support is calculated by counting the number of transactions (locations in this case) containing all the items in the set. 

### Implementation Details

* **Minimum Support:** The program uses a minimum support threshold of 0.01 for identifying frequent itemsets. This means a set is considered frequent only if it appears in at least 0.01 * total transactions (locations). 
* **Data Structures:** The program may utilize efficient data structures like hash tables or tries to store itemsets and calculate their support counts.
* **Optimization Techniques:** Techniques like pruning infrequent candidate sets early can be implemented to improve efficiency. 

### Running the Program

1. Ensure you have the "categories.txt" file in the same directory as the program.
2. Execute the program (implementation details will depend on the chosen programming language).
3. The program will generate two output files: "patterns.txt" (Part 1 & Part 2).

### Input

The program expects a text file named "categories.txt" containing category lists for locations. Each line represents a single location and contains a list of categories separated by semicolons (`;`). For example:

```
Local Services;IT Services & Computer Repair
```

### Output

The program generates two output files:

* **patterns.txt (Part 1):** This file lists all frequent categories of length 1 (single categories) along with their absolute support counts. Each line is formatted as:

```
support:category
```

* **patterns.txt (Part 2):** This file lists all frequent category sets (combinations of categories) along with their absolute support counts. Each line is formatted as:

```
support:category_1;category_2;category_3;...
```

The order of categories within a set doesn't matter (e.g., "Restaurant;Fast Food" is equivalent to "Fast Food;Restaurant").