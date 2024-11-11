## Contiguous Sequential Pattern Mining - README.md

### Description

This program implements an algorithm to discover frequently occurring, consecutive sequences of words (phrases) within a dataset of text reviews. This information can be valuable for tasks like sentiment analysis, product recommendation systems, and understanding user preferences based on their expressed opinions.


### Algorithm

The program implements a variation of a contiguous sequential pattern mining algorithm called PrefixSpan. Here's a breakdown of key concepts:

* **Contiguous Sequence:** A sequence of items appearing consecutively within a review (e.g., "good;food").
* **Minimum Support:**  A user-defined threshold to determine frequent patterns. This program uses a minimum support of 0.01 (at least 100 occurrences) for identifying frequent phrases.
* **Candidate Generation:** The algorithm identifies frequent single words (length-1 sequences) and iteratively generates candidate patterns of increasing lengths by considering frequent sequences from the previous iteration and extending them with words that frequently follow them within reviews.
* **Support Counting:** Each candidate pattern's support is calculated by counting the number of reviews where all words in the sequence appear consecutively in the same order.

### Running the Program

1. Ensure you have the "reviews_sample.txt" file in the same directory as the program.
2. Execute the program with python main.py
3. The program will generate an output file: "patterns.txt".


### Input

The program expects a text file named "reviews_sample.txt" containing pre-processed online reviews. Each line represents a single review where words have been stemmed and most punctuation removed. Individual words within a review are separated by spaces.

**Example Line:**

```
cold cheap beer good bar food good service looking great pittsburgh style fish sandwich place breading light fish plentiful good side home cut fry good grilled chicken salad steak soup day homemade lot special great place lunch bar snack beer
```


### Output

The program generates a single output file named "patterns.txt" listing all frequent contiguous sequential patterns (phrases) along with their absolute support counts. Each line is formatted as:

```
support:item_1;item_2;item_3;...
```

Here,

* `support`: Represents the absolute number of reviews containing the specific contiguous sequence of words.
* `item_n`: Represents a single word in the sequential pattern.

The order of words within a pattern is crucial. For example, "good;food" and "food;good" are considered distinct patterns.