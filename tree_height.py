# python3

import sys
import threading
import numpy as np


def compute_height(n, parents):
    
    empty = np.zeros(n)
    #print(empty)

    for i in range(n):
        if parents[i] != -1:
            index = parents[i]
            empty[index] = 1
    #print(empty)
    answer = int(np.sum(empty) + 1)
    print(answer)



def main():
    
    text = input()

    #text
    if "I" in text:
        #nodes
        n = int(input())
        #parents
        string = input()
        parents = np.asarray(list(map(int, string.split())))

        if n == parents.size:
            compute_height(n, parents)       
    
    #file
    elif "F" in text:
        file_n = input().strip()
        if "a" in file_n:
            return
        else:
            with open('.test/' + file_n, 'r') as f:
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

