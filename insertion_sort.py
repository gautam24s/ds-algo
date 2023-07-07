def insertionSort(A,  n):
    
    if n < 2:
        return
    
    for i in range(0, n):
        key = A[i]

        j = i - 1
        while j >= 0 and A[j] > key:
            A[j+1] = A[j]
            j -= 1
        
        A[j+1] = key


A = [9,3,5,4,2,1]

insertionSort(A, 6)

print(A)