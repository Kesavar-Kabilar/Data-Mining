from submission import Solution

def test(n):
    with open(f"./input{n}.txt") as file:
        X_train = []
        Y_train = []
        X_test = []
        for line in file:
            if int(line.strip("\n").split(",")[-1]) != -1:
                X_train.append(list(map(int, line.strip("\n").split(",")[1:-1])))
                Y_train.append(int(line.strip("\n").split(",")[-1]))
            else:
                X_test.append(list(map(int, line.strip("\n").split(",")[1:-1])))

        
    sol = Solution()
    p = sol.prior(X_train, Y_train)
    print(p)

    p = sol.label(X_train, Y_train, X_test)
    print(p)

test(0) # 4, 4
test(1) # 3
test(2) # 1