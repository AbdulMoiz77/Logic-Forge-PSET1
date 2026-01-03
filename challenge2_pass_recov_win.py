from collections import Counter

def characterFreqMatching(pattern, string):
    return not (Counter(pattern) - Counter(string))

def passRecoveryWin(log, pattern):
    n = len(log)
    win_start = 0
    win_end = 0

    while win_end < n:
        win_end += 1

        flag = False
        while characterFreqMatching(pattern, log[win_start: win_end+1]):        
            flag = True
            win_start += 1  

        if (flag):
            win_start -= 1

    if(flag):
        return log[win_start: win_end+1] 
    
    return ""

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