import numpy as np

def weight(a):
    a = np.array(a)
    mean = np.mean(a)
    median = np.median(a)
    val = mean - median
    print(f"a:{a}, mean: {mean}, median: {median}, val: {val}")
    
    return val



def sub_seq(a):
    # 生成a的所有子序列
    sub_seq = []
    for i in range(len(a)):
        for j in range(i+1, len(a)+1):
            sub_seq.append(a[i:j])
    print(f"a: {a}")
    print(f"sub_seq: {sub_seq}")
    return sub_seq

def run(a):
    max_weight = 0
    # 遍历a的子序列
    for sub in sub_seq(a):
        w = weight(sub)
        if w > max_weight:
            max_weight = w 
    # 计算子序列的权重
    return max_weight


if __name__ == "__main__":
    a = input("Enter the list: ")
    print(f"a: {a}, type: {type(a)}")
    a = a[1:-1].split(",")
    a = [int(i) for i in a]
    weight = run(a)
    print(f"The maximum weight is: {weight}")