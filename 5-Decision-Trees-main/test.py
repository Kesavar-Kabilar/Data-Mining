from main import Solution

def split_info_test(n):
    print(f"------------- TEST {n} -------------")

    with open(f"./sample_test_cases/split_info/input0{n}.txt", "r") as file:
        split_dim = int(file.readline().strip("\n"))
        split_point = float(file.readline().strip("\n"))

        data, label = [], []

        for line in file:
            line = line.strip("\n").split(" ")
            label.append(int(line[0]))
            row = []
            for attr in line[1:]:
                attr = attr.split(":")
                row.append(float(attr[1]))
            data.append(row)
    
    with open(f"./sample_test_cases/split_info/output0{n}.txt", "r") as file:
        correct_output = float(file.readline().strip("\n"))

    sol = Solution()
    o = round(sol.split_info(data, label, split_dim, split_point), 4)
    print(o == correct_output, o, correct_output)

split_info_test(0)
split_info_test(1)

def tree_structure_test(n):
    print(f"------------- TEST {n} -------------")
    with open(f"./sample_test_cases/tree_structure/input0{n}.txt", "r") as file:
        data, label = [], []

        for line in file:
            line = line.strip("\n").split(" ")
            label.append(int(line[0]))
            row = []
            for attr in line[1:]:
                attr = attr.split(":")
                row.append(float(attr[1]))
            data.append(row)
    
    with open(f"./sample_test_cases/tree_structure/output0{n}.txt", "r") as file:
        output = file.readline().strip("\n").replace("{", "").split("}")[:-1]
        preorder_output = []
        for k in output:
            k = tuple(k.replace("split_dim: ", "").replace(", split_point:", "").replace(", label:", "").split(" "))
            preorder_output.append(k)
            print(k)
            

    sol = Solution()
    sol.fit(data, label)

    def preorder(root):
        if root is None:
            return
        else:
            print((root.split_dim, root.split_point, root.label))
            preorder(root.left)
            preorder(root.right)
    preorder(sol.root)

tree_structure_test(0)
tree_structure_test(1)
tree_structure_test(2)

def classify_test(n):
    print(f"------------- TEST {n} -------------")

    with open(f"./sample_test_cases/classification/input0{n}.txt", "r") as file:
        data, label = [], []
        test_data = []

        for line in file:
            line = line.strip("\n").split(" ")
            if int(line[0]) != -1:
                label.append(int(line[0]))
                row = []
                for attr in line[1:]:
                    attr = attr.split(":")
                    row.append(float(attr[1]))
                data.append(row)
            else:
                row = []
                for attr in line[1:]:
                    attr = attr.split(":")
                    row.append(float(attr[1]))
                test_data.append(row)
    
    with open(f"./sample_test_cases/classification/output0{n}.txt", "r") as file:
        test_label = []
        for line in file:
            test_label.append(int(line.strip("\n")))

    sol = Solution()
    output = sol.classify(data, label, test_data)

    for o, t in zip(output, test_label):
        if o != t:
            print("Error: ", o, t)
    print("Complete")

classify_test(0)
classify_test(1)