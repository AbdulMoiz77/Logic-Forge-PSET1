def deepInvSearch(inv, k):
    n = len(inv)

    if k > n*n or k == 0:
        return -1

    heap = []
    for i in range(n):
        heap.append((inv[i][0], i, 0))

    for i in range(k):
        smallest = float('inf')
        rowidx = -1
        colidx = -1
        heapidx = -1
        for j in range(len(heap)):
            if heap[j][0] < smallest:
                smallest = heap[j][0]
                rowidx = heap[j][1]
                colidx = heap[j][2]
                idx = j
        
        item = heap.pop(idx)[0]
        if (colidx + 1) != n:
            colidx += 1
            heap.append((inv[rowidx][colidx], rowidx, colidx))

    return item


if __name__ == "__main__":
    matrix = [[1, 5, 9], [10, 11, 13], [12, 13, 15]]
    k = 8
    print(deepInvSearch(matrix, k))