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
    
"""
Returns an array that is the result of applying hamiltons method to
fairShare
"""
def hamiltonsMethod(fairShare, n):
    output = []
    #use parallel lists instead of a dictionary to maintain sorted order
    total = 0
    decimals = []
    indexes = []
    for i in range(0, len(fairShare)):
        truncatedShare = int(fairShare[i])
        output.append(truncatedShare)
        total += truncatedShare
        indexes.insert(binaryInsert(decimals, fairShare[i] - truncatedShare), i)
    i = len(decimals) - 1
    #add 1 to those that have highest decimal values
    while (total < n and i >= 0):
        output[indexes[i]] += 1
        total += 1
        i -= 1

    if i < 0:
        print("You f-ed up")
    return output
        
    
"""
Returns true if there is an alabama paradox with the given list of states sizes
when increasing the number of seats from n1 to n2
"""
def alabamaParadox(arr, n1, n2):
    #find the total number of people
    totalPopulation = 0;
    for i in arr:
        totalPopulation += i;
    #find the fair but impossible distributions for n1 and n2
    fairShare1 = []
    fairShare2 = []
    for i in arr:
        proportion = (i / totalPopulation)
        fairShare1.append(n1 * proportion)
        fairShare2.append(n2 * proportion)

    #apply hamiltons method on the fair shares
    ham1 = hamiltonsMethod(fairShare1, n1)
    ham2 = hamiltonsMethod(fairShare2, n2)

    for i in range(0, len(ham1)):
        if ham1[i] > ham2[i]:
            #print(ham1)
            #print(ham2)
            #print("-" * 20)
            return True

    return False


def run(reps, stat, toPrint):

    
    #f = open("output.txt", 'w')
    states = []
    random.seed(10)
    for q in range(int(stat)):
        states.append( random.randint(1000, 50000))
    startTime = time.time()
    for i in range(1, int(reps)):
        if alabamaParadox(states, i, i + 1):
            #f.write("(" + str(i) + ", " + str(i+1) + ")\n")
            if toPrint:
                print("(" + str(i) + ", " + str(i+1) + ")")

    #f.close()
    endTime = time.time()
    #print("Execution took: " + str(endTime - startTime) + " seconds")
    return endTime - startTime
    
if __name__ == '__main__':
    delt = run(sys.argv[1], sys.argv[2], True)
    print(delt)
    
    

    
