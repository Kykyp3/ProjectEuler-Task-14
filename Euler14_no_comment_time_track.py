# The following iterative sequence is defined for the set of positive integers:
# n → n/2 (n is even)
# n → 3n + 1 (n is odd)
# Using the rule above and starting with 13, we generate the following sequence:
# 13 → 40 → 20 → 10 → 5 → 16 → 8 → 4 → 2 → 1
# It can be seen that this sequence (starting at 13 and finishing at 1) contains 10 terms.
# Although it has not been proved yet (Collatz Problem), it is thought that all starting numbers finish at 1.
# Which starting number, under one million, produces the longest chain?

import time

time_start = time.time()

def count_collatz_length(x):
    length = 1
    current_number = x
    while current_number != 1:
        if current_number % 2 == 0:
            current_number = current_number/2
            length += 1
        else:
            current_number = current_number*3 + 1
            length +=1
    else:
        return length

def find_maximum_collatz_length(max):
    max_length=0
    max_number=0
    for i in range(max,9,-1):
        length = count_collatz_length(i)
        if length > max_length:
            max_length = length
            max_number = i
    return max_number


if __name__=="__main__":
    print("Максимальное значение последовательности Коллатца обладает число {}".format(find_maximum_collatz_length(1000000)))
    elapsed_time = time.time() - time_start
    print(elapsed_time)
