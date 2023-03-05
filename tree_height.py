# python3

import sys
import threading
import numpy as np


def compute_height(n, arr):
    # Write this function
    #unique = np.unique(arr, return_counts=False)

    
    #max_height = len(unique)
    # Your code here
    #return max_height
    #print(max_height)


def main():
    
    # implement input form keyboard and from files
    n = int(input())
    number_string = input()
    
    arr = np.fromstring(number_string, dtype = int, sep= ' ')
    
    unique = np.unique(arr, return_counts=False)
    max_height = len(unique)
    print(max_height)

    #print(arr)

    
    # let user input file name to use, don't allow file names with letter a
    # account for github input inprecision
    
    # input number of elements
    # input values in one variable, separate with space, split these values in an array
    # call the function and output it's result

    

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
