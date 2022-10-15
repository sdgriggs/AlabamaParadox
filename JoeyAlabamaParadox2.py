import time
import sys
import random
"""
Inserts an element into the given list using binary search and returns the index
of insertion
"""
def binaryInsert(arr, element):
    lower = 0
    upper = len(arr) - 1
    #edge case of empty list
    if (upper == -1):
        arr.append(element)
        return 0
    while (lower < upper):
        mid = (lower + upper) // 2
        if arr[mid] == element:
            arr.insert(mid, element)
            return mid
        elif arr[mid] > element:
            upper = mid - 1
        else:
            lower = mid + 1

    # lower == upper
    if arr[lower] < element:
        arr.insert(lower + 1, element)
        return lower + 1
    else:
        arr.insert(lower, element)
        return lower  

def hamiltonsMethod(arr, n):
    #the final output
    output = []
    #find the total number of people
    totalPopulation = 0;
    for i in arr:
        totalPopulation += i;
    #find the fair but likely impossible distribution
    fairShare = []
    for i in arr:
        proportion = (i / totalPopulation)
        fairShare.append(n * proportion)
    #use parallel lists instead of a dictionary to maintain sorted order
    seats = 0
    decimals = []
    indexes = []
    for i in range(0, len(fairShare)):
        truncatedShare = int(fairShare[i])
        output.append(truncatedShare)
        seats += truncatedShare
        indexes.insert(binaryInsert(decimals, fairShare[i] - truncatedShare), i)
    i = len(decimals) - 1
    #add 1 to those that have highest decimal values
    while (seats < n and i >= 0):
        output[indexes[i]] += 1
        seats += 1
        i -= 1

    return output
    
"""
Returns true if there is an alabama paradox with the given lists of seat
distributions
"""
def alabamaParadox(n1, n2):
    for i in range(0, len(n1)):
        if n1[i] > n2[i]:
            return True
    return False

def run(reps, stat, toPrint):
    states = []
    random.seed(10)
    for q in range(int(stat)):
        states.append( random.randint(1000, 50000))
    startTime = time.time()
    first = hamiltonsMethod(states, 1)
    for i in range(2, int(reps)):
        after = hamiltonsMethod(states, i)
        if alabamaParadox(first, after):
            if toPrint:
                print("(" + str(i) + ", " + str(i+1) + ")")
        first = after

    endTime = time.time()
    return endTime - startTime
    
if __name__ == '__main__':
    delt = run(sys.argv[1], sys.argv[2], True)
    print(delt)

    

    
