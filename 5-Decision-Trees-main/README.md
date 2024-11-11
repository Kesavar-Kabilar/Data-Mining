## Decision Tree Implementation

### Problem Description

This project focuses on building a decision tree classifier with a maximum depth of 2. The decision tree will be trained on a provided dataset and used to predict labels for unseen data points. 

### Core Functionalities

Three key functions are essential for this implementation:

1. **fit(train_data, train_labels):** This function takes the training data and its corresponding labels as input. It builds the decision tree by recursively splitting the data based on the attribute with the highest information gain. 
2. **split_info(data, labels, split_dim, split_point):** This function calculates the information gain achieved by splitting the data at a specific dimension (attribute) and split point. 
3. **classify(train_data, train_labels, test_data):** This function takes the training data, labels, and unseen test data as input. It utilizes the constructed decision tree to predict the labels for each data point in the test set.

**Important Note:**

* Only standard Python libraries are allowed. No external libraries like NumPy or Scikit-learn can be used.

### Decision Tree Algorithm

**Basic Structure:**

A decision tree is a tree-like structure where each internal node represents a decision based on an attribute, and each leaf node represents a predicted class label. During training, the algorithm iteratively splits the data based on the attribute that maximizes information gain.

**Information Gain:**

Information gain measures the decrease in uncertainty about the class labels after splitting the data on a particular attribute. It's calculated by comparing the entropy of the data before the split (H(D)) with the weighted average of the entropy of the resulting child nodes (H(C1) and H(C2)).

**Formula:**

```
Information Gain(D, A) = H(D) - ( |C1|/|D| * H(C1) + |C2|/|D| * H(C2) )
```

- **D:** Dataset
- **A:** Attribute
- **C1, C2:** Subsets of D after splitting on A
- **H(D):** Entropy of D
- **H(C1), H(C2):** Entropy of child nodes C1 and C2

**Splitting and Prediction:**

During training, the algorithm iteratively finds the attribute with the highest information gain and splits the data accordingly. This process continues until a maximum depth is reached or a pure leaf node (containing only data points from a single class) is formed.

For prediction, a new data point traverses the decision tree starting from the root node. At each node, the data point's value for the corresponding attribute is compared to the split point. Based on the comparison, the data point is directed to the left or right child node until it reaches a leaf node. The label associated with that leaf node is predicted as the class label for the data point.

### Implementation Details

**`fit` Function:**

1. Initialize the root node of the decision tree.
2. Recursively build the tree:
    * If the maximum depth is reached or all data points belong to the same class (pure node), create a leaf node with the majority class label.
    * Otherwise, calculate information gain for each attribute using the `split_info` function.
    * Choose the attribute with the highest information gain.
    * Find the optimal split point for the chosen attribute (using pre-determined calculation methods).
    * Split the data into two subsets based on the chosen split point.
    * Recursively call `fit` on the left and right subsets, creating the left and right child nodes of the current node.
3. Set the root node as the attribute of the `Solution` object.

**`split_info` Function:**

1. Calculate the entropy of the entire dataset (H(D)).
2. Split the data into two subsets based on the given split dimension and split point.
3. Calculate the entropy of each child node (H(C1) and H(C2)).
4. Use the information gain formula to calculate the information gain achieved by splitting on this attribute and split point.

**`classify` Function:**

1. Traverse the decision tree starting from the root node for each data point in the test set.
2. At each internal node, compare the data point's value for the corresponding attribute with the split point.
3. Based on the comparison, move to the left or right child node.
4. Once a leaf node is reached, the label associated with that node is predicted as the class label for the data point.
5. Return a list of predicted labels for all data points