def balancedPerfScore(scoresA, scoresB):
    n = len(scoresA) 
    m = len(scoresB)
    elements = n + m
    
    median_pos = elements // 2
    a = 0
    b = 0
    current = 0
    prev = 0

    for i in range(median_pos + 1):
        prev = current
        if a < n and (b >= m or scoresA[a] <= scoresB[b]) :
            current = scoresA[a]
            a = a + 1
        else:
            current = scoresB[b]
            b = b + 1

    if elements % 2 == 0:
        median = (prev + current) / 2
    else:
        median = current

    return median


if __name__ == "__main__":
    scoresA = [1, 3]
    scoresB = [2]
    print(balancedPerfScore(scoresA, scoresB))

    scoresA = [1, 2]
    scoresB = [3, 4]
    print(balancedPerfScore(scoresA, scoresB))    