import numpy as np



def find_max_id(c, str_b):
    
    # find the indices of c in str_b
    max_id = 0
    len_b = len(str_b)
    if c not in str_b:
        return -1
    else:
        max_id = str_b.index(c)
        str_b = str_b[max_id+1:]
        while c in str_b:
            c_id = str_b.index(c)
            max_id += c_id + 1
            str_b = str_b[c_id + 1:]
        return max_id


def is_substr(a, b):
    # check if a is a substring of b
    len_a = len(a)
    if len_a>len(b):
        return False
    for i in range(len_a):
        if a[i] not in b:
            return False
    
    
    for i in range(len_a - 1):
        for j in range(i+1, len_a):
            if b.index(a[i]) > find_max_id(a[j], b):
                return False
    
    return True

def run():
    source_str = input("Enter the source string: ")
    target_str = input("Enter the target string: ")
    
    start_id = 0
    end_id = 1
    cnt = 0
    str_a = target_str[start_id:end_id]
    while end_id <= len(target_str):
        add = False
        while end_id <= len(target_str):
            # print(f"str_a: {str_a}, source_str: {source_str}, is_substr: {is_substr(str_a, source_str)}")     
            if not is_substr(str_a, source_str):
                if not add:
                    print("It's impossible!")
                    return  
                break
            add = True
            end_id += 1
            str_a = target_str[start_id:end_id]
            
        start_id = end_id-1
        str_a = target_str[start_id:end_id]
        if add:
            cnt += 1
            add = False
    if cnt == 0:
        print("It's impossible!")
    else:
        print("The number of substrings is: ", cnt)

if __name__ == '__main__':
    run()
