# python3

import sys
import threading
import numpy as np


def compute_height(n, parents):
    if n <= 100:
        unique_array = np.unique(parents)
        unique_number = unique_array.size
        print(unique_number)
    else:
        pass


def main():
    
    text = input()

    #text
    if text == "I":
        #nodes
        n = int(input())
        #parents
        string = input()
        parents = np.asarray(list(map(int, string.split())))

        if n == parents.size:
            compute_height(n, parents)       
    
    #file
    elif text == "F":
        file_n = input().strip()
        if "a" in file_n:
            return
        else:
            with open(".test/" + file_n, mode= 'r') as f:
                #nodes
                n = int(f.readline())
                #parents
                string = f.readline()
                parents = np.asarray(list(map(int, string.split())))

                if n == parents.size:
                    compute_height(n, parents)
    
    #answer = compute_height(n, parents)
    #print(answer)

    #print(n)
    #print(parents)



#sys.setrecursionlimit(10**7)
#threading.stack_size(2**27)
threading.Thread(target=main).start()

