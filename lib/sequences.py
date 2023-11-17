#!/usr/bin/env python3

def print_fibonacci(length):
    i = 0
    j = 1
    count = 1
    my_list = []


    if length == 0:
        print(my_list)
    elif length == 1:
         my_list.append(i)
         print(my_list)
    else:    
        my_list=[i]
        while count < length:
                # my_list=[i]
                count += 1
                i, j = j, i + j
                my_list.append(i)
        print(my_list)

# print_fibonacci(1)