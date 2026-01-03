import heapq

def deepInvSearch(inv, k):
    n = len(inv)

    if k > n*n or k == 0:
        return -1

    heap = []
    for i in range(n):
        heap.append((inv[i][0], i, 0))

    heapq.heapify(heap)

    for i in range(k):
        val = heapq.heappop(heap)
        item = val[0]
        rowidx = val[1]
        colidx = val[2]
        
        if (colidx + 1) != n:
            colidx += 1
            temp = (inv[rowidx][colidx], rowidx, colidx)
            heapq.heappush(heap, (temp))

    return item


if __name__ == "__main__":
    matrix = [[1, 5, 9], [10, 11, 13], [12, 13, 15]]
    k = 8
    print(deepInvSearch(matrix, k))
