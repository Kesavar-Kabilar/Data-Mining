## Naive Bayes Classifier

### Background

This assignment focuses on building a Naive Bayes classifier to predict the animal class (Mammal, Bird, Reptile, etc.) based on various attributes like hair, feathers, eggs, etc., using the Zoo Animal Classification dataset: https://archive.ics.uci.edu/dataset/111/zoo

### The Naive Bayes Classifier

Naive Bayes is a probabilistic classifier based on Bayes' theorem. It assumes independence between features (attributes) given the class label. This simplifying assumption allows for efficient training and prediction.

**Key Formulae:**

* **Posterior Probability:** The probability of a class label (y) given a data point (X) is calculated as:

```
P(y | X) = P(X, y) / P(X)
```

  - P(y | X): Posterior probability of class y given data point X
  - P(X, y): Joint probability of X and y
  - P(X): Prior probability of data point X (sum of posterior probabilities over all classes)

* **Class Prediction:** The class with the highest posterior probability is predicted for a data point:

```
y' = argmax_y P(y | X) = argmax_y P(y) * P(X | y)
```

  - y': Predicted class label

* **Naive Bayes Assumption:** Independence between features given the class label:

```
P(X | y) = Π_i P(x_i | y)
```

  - P(X | y): Conditional probability of data point X given class y
  - Π_i: Product over all features (i)
  - P(x_i | y): Conditional probability of feature i given class y

**Laplacian Correction:**

To avoid zero probabilities for unseen feature values in a class, Laplacian correction is applied by adding a pseudo-count to the numerator and the number of unique values for that feature to the denominator.

* **Smoothed Conditional Probability:**

```
P(x_i = f | y = c) = ( # of training examples where class = c and xi = f + 0.1 ) / ( # training examples of class c + 0.1 × # unique values for attribute xi )
```

  - P(x_i = f | y = c): Smoothed conditional probability of feature i having value f given class c
  - c: Class label

* **Smoothed Prior Probability:**

```
P(y = c) = ( N_c + 0.1 |C| ) / ( N + 0.1 |C| )
```

  - P(y = c): Smoothed prior probability of class c
  - N_c: Number of training examples of class c
  - N: Total number of training examples
  - |C|: Number of classes

### Implementation Details

1. **compute_class_priors(X_train, Y_train):** This function calculates the prior probability for each class using the smoothed prior probability formula.
2. **predict_classes(X_train, Y_train, X_test):** This function trains the Naive Bayes model using the training data (X_train, Y_train) and then predicts the class labels for the unseen test data (X_test). It utilizes the functions below for calculations:
    * **calculate_posteriors(X_test, class_priors, cond_probs):** This function calculates the posterior probability for each class for each data point in the test set.
    * **get_most_probable_class(posteriors):** This function identifies the class with the highest posterior probability for each data point.