# Submit this file to Gradescope
from typing import List
# you may use other Python standard libraries, but not data
# science libraries, such as numpy, scikit-learn, etc.


class Solution:
    def d(self, p, q):
        """
        Calculates the Euclidean distance between two points p and q.

        Args:
            p: A tuple representing the coordinates of the first point.
            q: A tuple representing the coordinates of the second point.

        Returns:
            The Euclidean distance between p and q. Note the square root 
            is not calculated as the euclidean distance is only used to 
            compare hence it is not necessary.
        """
        return (p[0]-q[0])**2 + (p[1]-q[1])**2

    def D(self, Ci, Cj, func, clus_mem):
        """
        Calculates the distance between two clusters Ci and Cj using the specified distance function.

        Args:
            Ci: A list of points in cluster Ci.
            Cj: A list of points in cluster Cj.
            func: The distance function to use (e.g., min, max, mean).
            clus_mem: A dictionary to memoize distance calculations.

        Returns:
            The distance between Ci and Cj based on the specified function.
        """
        if (tuple(Ci), tuple(Cj)) in clus_mem:
            return clus_mem[(tuple(Ci), tuple(Cj))]
        DCiCj = []
        for vi in Ci:
            for vj in Cj:
                DCiCj.append(self.d(vi, vj))
        clus_mem[(tuple(Ci), tuple(Cj))] = func(DCiCj)
        return clus_mem[(tuple(Ci), tuple(Cj))]

    def createClusters(self, X):
        """
        Creates a list of initial clusters, where each cluster contains a single data point.

        Args:
            X: A list of data points.

        Returns:
            A list of initial clusters, each containing a single data point.
        """
        allClusters = [[tuple(x)] for x in X]
        return allClusters

    def hclus(self, C, K, func):
        """
        Performs hierarchical clustering on the given clusters C until K clusters remain.

        Args:
            C: A list of clusters.
            K: The desired number of final clusters.
            func: The distance function to use for merging clusters.

        Returns:
            A list of the final K clusters.
        """
        clus_mem = {}
        for _ in range(len(C)-K):
            # Find the closest pair of clusters
            minDist = float("inf")
            minI, minJ = None, None
            for i in range(len(C)):
                for j in range(i+1, len(C)):
                    Ci, Cj = C[i], C[j]
                    curDist = self.D(Ci, Cj, func, clus_mem)
                    if curDist < minDist:
                        minDist = curDist
                        minI, minJ = i, j
                        minCi, minCj = Ci, Cj
            # Merge the closest pair
            C = [minClus for i, minClus in enumerate(C) if i not in [
                                                     minI, minJ]]
            Ck = minCi + minCj
            C.append(Ck)
        return C

    def writeKClus(self, X, KClus):
        """
        Assigns each data point to a cluster in KClus and returns the cluster assignments.

        Args:
            X: A list of data points.
            KClus: A list of the final K clusters.

        Returns:
            A list of cluster assignments for each data point.
        """
        setKClus = []
        for c in KClus:
            setKClus.append(set(c))

        output = []
        for pi, pj in X:
            for i, clus in enumerate(setKClus):
                if (pi, pj) in clus:
                    output.append(i)
                    break
        return output



    def hclus_single_link(self, X: List[List[float]], K: int) -> List[int]:
        """
        Single link hierarchical clustering

        Args:
            X: 2D input data
            K: the number of output clusters
        Returns:
            A list of integers (range from 0 to K - 1) that represent class labels.
            The number does not matter as long as the clusters are correct.
            For example: [0, 0, 1] is treated the same as [1, 1, 0]
        """
        # implement this function
        C = self.createClusters(X)
        KClus = self.hclus(C, K, min)
        output = self.writeKClus(X, KClus)
        return output

    def hclus_average_link(self, X: List[List[float]], K: int) -> List[int]:
        """Complete link hierarchical clustering"""
        # implement this function
        C = self.createClusters(X)
        avg = lambda x: sum(x) / len(x)
        KClus = self.hclus(C, K, avg)
        output = self.writeKClus(X, KClus)
        return output

    def hclus_complete_link(self, X: List[List[float]], K: int) -> List[int]:
        """Average link hierarchical clustering"""
        # implement this function
        C = self.createClusters(X)
        KClus = self.hclus(C, K, max)
        output = self.writeKClus(X, KClus)
        return output