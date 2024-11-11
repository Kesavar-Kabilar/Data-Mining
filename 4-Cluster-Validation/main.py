# Submit this file to Gradescope
from typing import Dict, List, Tuple
# you may use other Python standard libraries, but not data
# science libraries, such as numpy, scikit-learn, etc.

from math import comb, log, sqrt


class Solution:

    def confusion_matrix(self, true_labels: List[int], pred_labels: List[int]) -> Dict[Tuple[int, int], int]:
        """Calculate the confusion matrix and return it as a sparse matrix in dictionary form.
        Args:
          true_labels: list of true labels
          pred_labels: list of predicted labels
        Returns:
          A dictionary of (true_label, pred_label): count
        """
        c = {}
        for t, y in zip(true_labels, pred_labels):
            if (t, y) in c:
                c[(t, y)] += 1
            else:
                c[(t, y)] = 1
        return c

    def jaccard(self, true_labels: List[int], pred_labels: List[int]) -> float:
        """Calculate the Jaccard index.
        Args:
          true_labels: list of true cluster labels
          pred_labels: list of predicted cluster labels
        Returns:
          The Jaccard index. Do NOT round this value.
        """
        conf = self.confusion_matrix(true_labels, pred_labels)

        TP = 0

        true_clus = {}
        pred_clus = {}

        for (t, y), count in conf.items():
            TP += comb(count, 2)

            if t in true_clus:
                true_clus[t] += count
            else:
                true_clus[t] = count

            if y in pred_clus:
                pred_clus[y] += count
            else:
                pred_clus[y] = count
        FN = sum([comb(count, 2) for count in true_clus.values()]) - TP
        FP = sum([comb(count, 2) for count in pred_clus.values()]) - TP

        if (TP+FN+FP) == 0:
            return 0
        return TP/(TP+FN+FP)

    def nmi(self, true_labels: List[int], pred_labels: List[int]) -> float:
        """Calculate the normalized mutual information.
        Args:
          true_labels: list of true cluster labels
          pred_labels: list of predicted cluster labels
        Returns:
          The normalized mutual information. Do NOT round this value.
        """
        try:
            n = len(true_labels)
            conf = self.confusion_matrix(true_labels, pred_labels)

            true_clus = {}
            pred_clus = {}

            for (t, y), count in conf.items():
                if t in true_clus:
                    true_clus[t] += count
                else:
                    true_clus[t] = count

                if y in pred_clus:
                    pred_clus[y] += count
                else:
                    pred_clus[y] = count

            HC = -sum([(Ci/n)*log(Ci/n) for Ci in pred_clus.values()])
            HG = -sum([(Gi/n)*log(Gi/n) for Gi in true_clus.values()])

            ICG = 0
            for (t, y), count in conf.items():
                pij = count / n
                pCi = pred_clus[y] / n
                pGj = true_clus[t] / n

                ICG += pij * log(pij / (pCi*pGj))

            return ICG / sqrt(HG*HC)
        except:
            return 0
