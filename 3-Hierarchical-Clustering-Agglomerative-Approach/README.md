## Hierarchical Clustering with Agglomerative Approach - README.md

###  Problem Description

This program implements the agglomerative hierarchical clustering algorithm to group geographical data points based on their similarity. The data consists of 2D vectors representing longitude and latitude coordinates.

###  Agglomerative Hierarchical Clustering

This approach iteratively merges the most similar clusters until a desired number of clusters remain. Here's the breakdown:

1. **Initialization:** Each data point starts as its own individual cluster.
2. **Merging:** In each step, the two most similar clusters are identified and merged into a single new cluster. Similarity is determined by a chosen distance measure between clusters.
3. **Iteration:** Steps 1 & 2 are repeated until the desired number of clusters (K) is reached.

###  Distance Measures

The program utilizes three different distance metrics to measure similarity between clusters:

* **Single Link:** This calculates the minimum distance between any two data points, one from each cluster. The smaller the minimum distance, the more similar the clusters are considered.

```
D(Ci, Cj) = min{d(vp, vq) | vp ∈ Ci, vq ∈ Cj}
```

* **Complete Link:** This calculates the maximum distance between any two data points, one from each cluster. The smaller the maximum distance, the more similar the clusters are considered.

```
D(Ci, Cj) = max{d(vp, vq) | vp ∈ Ci, vq ∈ Cj}
```

* **Average Link:** This calculates the average distance between all possible pairs of data points, one from each cluster. The smaller the average distance, the more similar the clusters are considered.

```
D(Ci, Cj) = mean{d(vp, vq) | vp ∈ Ci, vq ∈ Cj}
```

**Note:** In these equations, `d(⋅, ⋅)` represents the distance function between two data points (often Euclidean distance).

###  Implementation Details

* Reading data points from the provided input format.
* Calculating distance between data points using the Euclidean distance formula.
* Implementing the chosen distance metric (Single Link, Complete Link, or Average Link) to determine similarity between clusters.
* Merging the two most similar clusters based on the chosen distance measure.
* Keeping track of cluster memberships and updating them after merging.
* Returning the final clustering results (cluster assignments for each data point) after reaching K clusters.

###  Additional Notes

* This algorithm was implement with only the standard built-in libraries. There was no use of NumPy or Scikit-learn.