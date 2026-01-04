def isValid(expr):
    open_count = 0
    close_count = 0

    for i in expr:
        if i == "(":
            open_count += 1
        elif i == ")" :
            if open_count > 0:
                open_count -= 1
            else:
                close_count += 1

    return open_count == 0 and close_count == 0 # if removal count of both opening and closing braces are zero, the string must be valid

def dfs(expr, st, idx, open_count, close_count, valid_strings):
    if idx == len(expr):
        if isValid(st):
            valid_strings.add(st)
        return
        
    if expr[idx] == "(" and open_count > 0: # removing the bracket
        dfs(expr, st, idx+1, open_count-1, close_count, valid_strings)    
    elif expr[idx] == ")" and close_count > 0: # removing the bracket
        dfs(expr, st, idx+1, open_count, close_count-1, valid_strings)

    # keeping the bracket
    dfs(expr, st+expr[idx], idx+1, open_count, close_count, valid_strings)    
    

def brokenExprFix(expr):
    open_count = 0
    close_count = 0

    for i in expr: # finding the removal count for both the braces opening and closing
        if i == "(":
            open_count += 1
        elif i == ")" :
            if open_count > 0:
                open_count -= 1
            else:
                close_count += 1

    # performing DFS    
    valid = set() # using set in order to avoid duplicates
    dfs(expr, "", 0, open_count, close_count, valid)
   
    return list(valid)


if __name__ == "__main__":
    st = "()())()"
    print(brokenExprFix(st))
    
    st = "(a)())()"
    print(brokenExprFix(st))
    
    st = ")("
    print(brokenExprFix(st))

    st = "()"
    print(brokenExprFix(st))

    st = "abc"
    print(brokenExprFix(st))

    st = "((("
    print(brokenExprFix(st))

    
