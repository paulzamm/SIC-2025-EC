# Resolución de ejercicios del quiz

# Q 37-01
def bubblesort(S):
    n = len(S)
    cont = 0
    for i in range(n):
        print("Pasada:", i+1)
        for j in range(0, n-1):
            cont += 1
            print(f"  Comparando S[{j}]={S[j]} y S[{j+1}]={S[j+1]}")
            if S[j] > S[j+1]:
                print(f"    Intercambiando S[{j}] y S[{j+1}]")
                S[j], S[j+1] = S[j+1], S[j]
        print("  Estado de la lista:", S)
    print("Total de comparaciones:", cont)
    return S

S = [50, 30, 40, 10, 20]
print("-----BUBBLE SORT-----")
print("Lista original:", S)
result = bubblesort(S)
print("Lista ordenada:", result)

# Q 27-02

def insertionSort2(S):
    n = len(S)
    cont = 0
    for i in range(1, n):
        print(f"Pasada {i}:")
        x = S[i]
        j = i - 1
        while j >= 0 and S[j] > x:
            cont += 1
            print(f"  Comparando S[{j}]={S[j]} con x={x}")
            S[j + 1] = S[j]
            j -= 1
        S[j + 1] = x
        print("  Estado de la lista:", S)
    print("Total de comparaciones:", cont)
    return S

S = [50, 30, 40, 10, 20]
print("\n-----INSERTION SORT-----")
print("Lista original:", S)
result = insertionSort2(S)
print("Lista ordenada:", result) 

# Q 28-01
cont = 0
def merge2(S, low, mid, high):
    global cont
    cont += 1
    print(f"  Merge llamada {cont}: low={low}, mid={mid}, high={high}")
    
    R = []
    i, j = low, mid + 1
    while i <= mid and j <= high:
        if S[i] < S[j]:
            R.append(S[i])
            i += 1
        else:
            R.append(S[j])
            j += 1
    if i > mid:
        for k in range(j, high + 1):
            R.append(S[j])
    else:
        for k in range(i, mid + 1):
            R.append(S[i])
    for k in range(len(R)):
        S[low + k] = R[k]

def mergeSort2(S, low, high):
    if low < high:
        mid = (low + high) // 2
        mergeSort2(S, low, mid)
        mergeSort2(S, mid + 1, high)
        merge2(S, low, mid, high)

S = [6,2,11,7,5,4,8,16,10,3]
print("\n-----MERGE SORT-----")
print("Lista original:", S)
mergeSort2(S, 0, len(S)-1)
print("Lista ordenada:", S)
print(f"Total de llamadas a merge2(): {cont}")


# Q 29-01
def partition1(S, low, high):
    pivot = S[low]
    left, right = low + 1, high
    while left < right:
        print(S)
        while left <= right and S[left] <= pivot:
            left += 1
        while left <= right and S[right] >= pivot:
            right -= 1
        if left < right:
            S[left], S[right] = S[right], S[left]
        else:
            break
    pivotpoint = right
    S[low], S[pivotpoint] = S[pivotpoint], S[low]
    return pivotpoint

S = [15,10,12,20,25,13,22]
print("\n-----PARTITION-----")
print("Lista original:", S)
result = partition1(S, 0, len(S)-1)
print("Lista después de particionar:", S)
print(f"El pivote {S[result]} quedó en el índice {result}.")