def mergeSort(A, p, r):
    if p >= r:
        return
    
    q = (p+r)//2

    mergeSort(A, p, q)
    mergeSort(A, q+1, r)
    merge(A, p, q, r)



def merge(A, p, q, r):
    # length of left and right subarray
    nL = q - p + 1
    nR = r - q

    # define arrays to constitute left and right subarray
    L = []
    R = []

    # copy elements from left subarray to L
    for i in range(0, nL):
        L.append(A[p + i])
    
    # copy elements from right subarray to R
    for j in range(0, nR):
        R.append(A[q+j+1])
    
    i = 0
    j = 0
    k = p

    # compare and merge
    while i < nL and j < nR:
        if L[i] <= R[j]:
            A[k] = L[i]
            i += 1
        else:
            A[k] = R[j]
            j += 1
        k += 1
    
    # merge remaining elements from the left subarray L
    while i < nL:
        A[k] = L[i]
        i += 1
        k += 1
    
    # merge remaining elements from the right subarray R
    while j < nR:
        A[k] = R[j]
        j += 1
        k += 1


A = [9, 8, 7, 6, 5, 4, 3, 2, 1, 0]

mergeSort(A, 3, 8)

print(A)