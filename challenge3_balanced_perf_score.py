def balancedPerfScore(scoresA, scoresB):
    n = len(scoresA) 
    m = len(scoresB)
    elements = n + m
    
    median_pos = elements // 2
    a = 0
    b = 0
    seen = 0

    prev = 0
    while seen < median_pos:
        if scoresA[a] <= scoresB[b] and a < n-1:
            prev = scoresA[a]
            a = a + 1
        elif b < m-1:
            prev = scoresB[b]
            b = b + 1

        seen += 1

    if scoresA[a] <= scoresB[b]:
        median = scoresA[a]
    else:
        median = scoresB[b]

    if elements % 2 == 0:
        median += prev
        median = median / 2

    return median


if __name__ == "__main__":
    scoresA = [1, 3]
    scoresB = [2]
    print(balancedPerfScore(scoresA, scoresB))

    scoresA = [1, 2]
    scoresB = [3, 4]
    print(balancedPerfScore(scoresA, scoresB))    