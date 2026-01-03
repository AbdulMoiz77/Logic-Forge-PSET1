def deepInvSearch(inv, k):
    n = len(inv)
    start = inv[0][0]
    end = inv[n-1][n-1]

    while start < end:
        mid = (start + end) // 2

        # starting from top right
        row = 0
        col = n - 1
        count = 0   

        # will move down or left
        while row < n and col >= 0:
            current = inv[row][col]
            if current <= mid:  # all the values in this row would also be smaller than it, so adding the count and moving to larger value i.e. the next row
                count += col + 1
                row += 1 # moving down to the larger value
            else: # cuurent value is too big and all the values below this value would be larger than it so moving to smaller value i.e. the left value
                col -= 1

        if count >= k:
            end = mid
        else:
            start = mid + 1

    return start


if __name__ == "__main__":
    matrix = [[1, 5, 9], [10, 11, 13], [12, 13, 15]]
    k = 8
    print(deepInvSearch(matrix, k))
