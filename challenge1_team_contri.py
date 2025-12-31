def teamContriMultiplier(contributions):
    n = len(contributions)
    prefix = [1]*n

    for i in range(1,n):
        prefix[i] = prefix[i-1] * contributions[i-1]

    suffix = [1]*n
    for i in range(n-1, 0, -1):
        suffix[i-1] = suffix[i] * contributions[i]

    impact = [1]*n
    for i in range(n):
        impact[i] = suffix[i] * prefix[i]

    return impact



if __name__ == "__main__":
    contributions = [1, 2, 3, 4]
    print(teamContriMultiplier(contributions))

    contributions = [-1, 1, 0, -3, 3]
    print(teamContriMultiplier(contributions))