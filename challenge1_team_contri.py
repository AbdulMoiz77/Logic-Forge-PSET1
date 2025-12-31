def teamContriMultiplier(contributions):
    n = len(contributions)
    impact = [1]*n

    for i in range(1,n):
        impact[i] = impact[i-1] * contributions[i-1]

    temp = 1
    for i in range(n-2, -1, -1):
        temp *= contributions[i+1]
        impact[i] *= temp

    return impact



if __name__ == "__main__":
    contributions = [1, 2, 3, 4]
    print(teamContriMultiplier(contributions))

    contributions = [-1, 1, 0, -3, 3]
    print(teamContriMultiplier(contributions))