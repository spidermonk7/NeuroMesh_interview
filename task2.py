import numpy as np
# import stack here






def run():
    origin_str = input("Enter the sentence to be checked: ")
    # use a stack here
    stack = []
    right_marks = []
    left_marks = []
    for id, c in enumerate(origin_str):
        if c == '(':
            stack.append((id, c))
        elif c == ')':
            if len(stack) == 0:
                # print("It's invalid!")
                right_marks.append(id)
            else:
                stack.pop()
    left_marks = [item[0] for item in stack]
    new_str = ""
    print(origin_str)
    for id, c in enumerate(origin_str):
        if id in left_marks:
            print('x', end="")
        elif id in right_marks:
            print('?', end="")
        else:
            print(' ', end="")



if __name__ == "__main__":
    run()
    
    
    