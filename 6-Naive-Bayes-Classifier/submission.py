# Submit this file to Gradescope
import math
from typing import Dict, List, Tuple
# You may use any built-in standard Python libraries
# You may NOT use any non-standard Python libraries such as numpy, scikit-learn, etc.

num_C = 7  # Represents the total number of classes


class Solution:

    def prior(self, X_train: List[List[int]], Y_train: List[int]) -> List[float]:
        """Calculate the prior probabilities of each class
        Args:
            X_train: Row i represents the i-th training datapoint
            Y_train: The i-th integer represents the class label for the i-th training datapoint
        Returns:
            A list of length num_C where num_C is the number of classes in the dataset
        """
        num_C_prob, n = [0.1 for _ in range(num_C)], len(Y_train)+0.1*num_C
        for y in Y_train:
            num_C_prob[y-1] += 1
        return [y/n for y in num_C_prob]

    def label(self, X_train: List[List[int]], Y_train: List[int], X_test: List[List[int]]) -> List[int]:
        """Calculate the classification labels for each test datapoint
        Args:
            X_train: Row i represents the i-th training datapoint
            Y_train: The i-th integer represents the class label for the i-th training datapoint
            X_test: Row i represents the i-th testing datapoint
        Returns:
            A list of length M where M is the number of datapoints in the test set
        """
        # implement this function

        prior_prob = self.prior(X_train, Y_train)

        Y_pred_h = [[[[0.1, 0] for _ in range(len(X_train[0]))] for _ in range(num_C)] for _ in range(len(X_test))]
        U_feat = [set() for _ in range(len(X_train[0]))]
        Y_pred = []

        for x_tr, y_tr in zip(X_train, Y_train):
            for t_i, x_te in enumerate(X_test):
                for f_t, (x_tr_f, x_te_f) in enumerate(zip(x_tr, x_te)):
                    Y_pred_h[t_i][y_tr-1][f_t][0] += x_tr_f == x_te_f
                    Y_pred_h[t_i][y_tr-1][f_t][1] += 1
                    U_feat[f_t].add(x_tr_f)

        for matrix in Y_pred_h:
            PXy = []
            for row, prior_t in zip(matrix, prior_prob):
                row_prob = [x/(t + 0.1*len(u)) for (x, t), u in zip(row, U_feat)]
                total = 1
                for num in row_prob:
                    total *= num
                PXy.append(total*prior_t)
            Y_pred.append(PXy.index(max(PXy))+1)

        return Y_pred


