# python3

import sys
import threading
import numpy as np


def compute_height(n, parents):

    parents = np.array(parents)

    tree = np.empty(n, dtype = object)

    tree.fill([])

    
    for i in range(n):

        if parents[i] == -1:

            root = i       
        else:

            tree[parents[i]] = np.append(tree[parents[i]], i)

    def max_height(a):

        if not tree[a]:

            return 1      
        return max(max_height(b) for b in tree[a])      
    
    return max_height(root)
 


def main():
    
    text = input()

    if text == 'F':
        file = input().strip()
        with open(file, 'r') as f:
            n = int(f.readline())
            parents = list(map(int, f.readline().split()))

            print(compute_height(n, parents))

    else:
        n = int(text)
        #n = int(input())
        line = input()
        parents = list(map(int, line.split()))

        print(compute_height(n, parents))


if __name__ == '__main__':

    sys.setrecursionlimit(10**7)
    threading.stack_size(2**27)
    threading.Thread(target=main).start()
    main()
