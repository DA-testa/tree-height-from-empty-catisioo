# python3

import sys
import threading
import numpy as np


def compute_height(n, parents):
    arr = np.zeros(n, dtype=int)

    for i in range(n):
        if arr[i] != 0:
            continue

        height = 1
        val = parents[i]
        while val != -1:
            if arr[val] != 0:
                height = height + arr[val]
                break
            height = height + 1
            val = parents[val]
        a = i
        while a != -1 and arr[a] == 0:
            arr[a] = height
            height = height - 1
            a = parents[a]
    return np.max(arr)


def main():
    
    text = input()

    if text == "I":
        n = int(input())
        parents = np.asarray(list(map(int, input().split())))
    elif text == "F":
        file = input().strip()
        if "a" in file:
            return
        with open("test/" + file, mode= 'r') as f:
            n = int(f.readline())
            parents = np.asarray(list(map(int,f.readline().split())))
    else:
        return
    
    answer = compute_height(n, parents)
    print(answer)

    #print(n)
    #print(parents)



sys.setrecursionlimit(10**7)
threading.stack_size(2**27)
threading.Thread(target=main).start()

main()
