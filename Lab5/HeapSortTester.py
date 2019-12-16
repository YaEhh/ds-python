# give frequency list
# give text string, get bitstring
# give bitstring, get text string
import random
import string
import re
import math
#Module Imports
import sys
from importlib import import_module

def GenerateArray(size=10):
    if (size <= 1) :
        size = 2
    elif (size > 50):
        size = 50
    data = []
    for i in range(1,size):
        data.append(random.randint(0, size))
    data.append(0)

    return data

def CheckHeapness(heap):
    if len(heap) < 2:
        return True # 1 element heap is trivially correct
    data = heap.getData()
    for i in range(len(data)-1, 1, -1):
        #print(f"Checking {i}")
        if data[i] > data[math.floor(i/2)]:
            return False
    return True

def Test(lib, seed=0, size=10, rounds=10, verbose=False ):
    if not lib:
        print("You need to include a testable library")
        return False
    random.seed(a=seed)

    for i in range(rounds):
        data = GenerateArray(size)
        try:
            heap = lib.MyHeap(size)
        except:
            if verbose:
                print("Error: Heap not creatable.")
            return False
        count = 0
        for elem in data:
            try:
                heap.insert(elem)
            except:
                if verbose:
                    print("Error: Heap element not insertable.")
                return False
            count += 1

            if len(heap) != count:
                if verbose:
                    print("Error: Heap item count incorrect.")
                return False    

            if not CheckHeapness(heap):
                if verbose:
                    print("Error: Insertion does not maintain heap property.")
                return False

        try:
            m = heap.extractMax()
            if not CheckHeapness(heap):
                if verbose:
                    print("Error: Extraction does not maintain heap property.")
                return False
            heap.insert(m+1)
            if (m+1) != heap.extractMax():
                if verbose:
                    print("Error: Insertion does not maintain heap property.")
                return False
        except:
            if verbose:
                print("Error: Heap element not insertable.")
            return False

        data = sorted(data, reverse=True)
        data[0] += 1

        heapsorted = []
        for i in range(count):
            try:
                heapsorted.append(heap.extractMax())
            except:
                if verbose:
                    print("Error: Element not extracted.")
                return False 
            
            if not CheckHeapness(heap):
                if verbose:
                    print("Error: Extraction does not maintain heap property.")
                return False

        for i in range(len(heapsorted)-1):
            if heapsorted[i]<heapsorted[i+1]:
                if verbose:
                    print("Error: Extraction does not return sorted list")
                return False

    return True

if __name__ == "__main__":
    if len(sys.argv) < 2:
        print("Include at least a library name as an argument.")
        exit()
    name = sys.argv[1]
    if name.endswith(".py"):
        name = name[:-3]
    print(f"Testing module {name}")
    module=import_module(name,package=__name__)
    v = Test(module,seed=123456, size=3000, rounds=200, verbose=True)
    print(f"Test result: {v}")