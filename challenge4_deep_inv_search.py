def deepInvSearch(inv, k):
    n = len(inv)
    start = inv[0][0]
    end = inv[n-1][n-1]

    while start < end:
        mid = (start + end) // 2

        # starting from bottom left
        row = n-1
        col = 0
        count = 0   

        # will move up or right
        while row >= 0 and col < n:
            current = inv[row][col]
            if current <= mid:  # all the value above this value would be smaller than it, so adding the count of all those values
                count += row + 1
                col += 1 # moving right to the larger value
            else: # all the value to the right of this value would be larger than it so moving to smaller value i.e. the above value
                row -= 1

        if count >= k:
            end = mid
        else:
            start = mid + 1

    return start


if __name__ == "__main__":
    matrix = [[1, 5, 9], [10, 11, 13], [12, 13, 15]]
    k = 8
    print(deepInvSearch(matrix, k))
