# for i in range(100, 1001, 100):
#     print (i)


# print(56/0)


# def close_far(a, b, c):
#   if abs(a-b) < 1 or abs(a-c) < 1:
#     return False
#   else:
#     return True


# print(close_far(1, 2, 10))


# def make_chocolate(small, big, goal):
#   temp = goal - big*5
#   if goal == big*5:
#     print("test1")
#     return 0
#   elif goal%5 > small:
#     return -1
#     print("test2")
#   elif goal %5 < small:
#     if temp <= small:
#       print("test3")
#       return (goal%5) % small
#     else:
#       return -1

# var = make_chocolate(6, 2, 7)
# print (var)

# print(5%6)
# import pytest

def split(word):
    return [char for char in word]

def double_char(str):
    temp = []
    strlist = split(str)
    strs = ""
    for i in range(len(str)):
        temp.append(strlist[i])
        temp.append(strlist[i])
    return strs.join(temp)

print(split("feeed"))

double_char("the")