def passRecoveryWin(log, pattern):
    n = len(log)
    win_start = 0
    win_end = 0

    # building character maps
    patternMap = {}
    for i in pattern:
        patternMap[i] = patternMap.get(i,0) + 1

    patternMapLength = len(patternMap) # to keep track of how character matches are needed to complete the pattern

    found = 0 # for keeping track of character matches in the window
    windowMap = {}   
    windowSize = float('inf')

    for i in range(n):
        win_end = i # sliding the window
        windowMap[log[i]] = windowMap.get(log[i],0) + 1

        if windowMap[log[i]] == patternMap.get(log[i], 0): # if a character's freq in the window matches the pattern's freq we have found a match of character
            found += 1

        while found == patternMapLength:
            if win_end - win_start < windowSize: #storing the best/min window
                windowSize = win_end - win_start
                best_start = win_start
                best_end = win_end

            # removing a char from the window
            remchar = log[win_start]
            windowMap[remchar] = windowMap[remchar] - 1

            if windowMap[remchar] + 1 == patternMap.get(remchar, 0): # if the character just removed from the window was required for the pattern
                found -= 1

            win_start += 1 # shrinking the window            

    # if no valid window is found (while loop is not entered once, as the windowSize was updating inside the while) then return empty string
    if windowSize == float('inf'):
        return ""
    
    # This statement is reached only when the while loop was executed atleat once and so the best_start and best_end would be defined
    return log[best_start : best_end+1]



if __name__ == "__main__":
    log = "ADOBECODEBANC"
    pattern = "ABC"
    print(passRecoveryWin(log, pattern))
    
    log = "a"
    pattern = "a"
    print(passRecoveryWin(log, pattern))

    log = "a"
    pattern = "aa"
    print(passRecoveryWin(log, pattern))