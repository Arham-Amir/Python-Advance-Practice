arr1 = [7, 1, 5, 2, 3, 6]
arr2 = [3, 8, 6, 20, 7]

def addOrCheckFrequency(frequencyDict, arr):
    for num in arr:
        if num not in frequencyDict:
            frequencyDict[num] = 1
            
def removeOrCheckFrequency(frequencyDict, arr):
    for num in arr:
        if num in frequencyDict:
            frequencyDict[num] += 1
                 
def unionOfArray(arr1, arr2):
    frequencyDict = {}
    addOrCheckFrequency(frequencyDict, arr1)
    addOrCheckFrequency(frequencyDict, arr2)
    return list(frequencyDict.keys())

def intersectionOfArray(arr1, arr2):
    frequencyDict = {}
    addOrCheckFrequency(frequencyDict, arr1)
    removeOrCheckFrequency(frequencyDict, arr2)
    return list(filter(lambda key: frequencyDict[key] > 1, frequencyDict.keys()))
    

print("Union of Array: ", unionOfArray(arr1, arr2))
print("Intersection of Array: ", intersectionOfArray(arr1, arr2))
    
    
    