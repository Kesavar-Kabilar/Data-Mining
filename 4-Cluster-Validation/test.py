from main import Solution
from time import time
from random import randint

with open("./sample_test_cases/input00.txt") as file:
  n = int(file.readline().strip("\n"))

  true = []
  pred = []
  for line in file:
    t, y = line.strip("\n").split(" ")
    true.append(int(t))
    pred.append(int(y))

# n = 10000000
# n = 10000

# k1, k2 = 8, 5
# true = [randint(0, k1) for _ in range(n)]
# pred = [randint(0, k2) for _ in range(n)]


sol = Solution()


s = time()

output = sol.jaccard(true, pred)
print("Solution Jaccard: ", output)

output = sol.nmi(true, pred)
print("NMI: ", output)

output = sol.confusion_matrix(true, pred)
print("Confusion Matrix: ")

for k, v in output.items():
    print(k, "->", v)

e = time()
print("Total Time: ", e - s)