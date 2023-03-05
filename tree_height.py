# python3

import sys
import threading
import numpy as np


def compute_height(n, arr):
    
    
    unique = np.unique(arr, return_counts=False)
    max_height = len(unique)
    
    return max_height


def main():
    
    # implement input form keyboard and from files
    n = int(input())
    number_string = input()
    arr = np.fromstring(number_string, dtype = int, sep= ' ')

    answer = compute_height(n, arr)
    
    print(answer)

    

# In Python, the default limit on recursion depth is rather low,
# so raise it here for this problem. Note that to take advantage
# of bigger stack, we have to launch the computation in a new thread.
sys.setrecursionlimit(10**7)  # max depth of recursion
threading.stack_size(2**27)   # new thread will get stack of such size
threading.Thread(target=main).start()

#main()
# print(numpy.array([1,2,3]))

if __name__ == '__main__':
    main()
