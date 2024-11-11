from main import Solution
from time import time 

for f_num in [0, 1, 2, 3, 4, 5, 9]:
  print(f_num)
  with open(f"./sample_test_cases/input0{f_num}.txt") as file:
    _, K, L = file.readline().strip("\n").split(" ")
    K, L = int(K), int(L)

    X = []
    for line in file:
      x, y = line.strip("\n").split(" ")
      X.append([float(x), float(y)])

  sol = Solution()
  s = time()
  if L == 0:
    output = sol.hclus_single_link(X, K)
  elif L == 1:
    output = sol.hclus_complete_link(X, K)
  else:
    output = sol.hclus_average_link(X, K)
  e = time()

  with open(f"./sample_test_cases/output0{f_num}.txt") as file:
    realSol = []
    for line in file:
      realSol.append(int(line.strip("\n")))

  all = True
  d = {}
  for o, r in zip(output, realSol):
    if r in d:
      r = d[r]
    else:
      d[r] = o
      r = d[r]
    # print(o, "->", r)
    all = all and o == r

  print(all)
  print(e - s)