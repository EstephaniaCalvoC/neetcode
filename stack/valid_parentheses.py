def isValid(s: str) -> bool:
    open_close = {"]":"[",
                  "}": "{",
                  ")": "("}

    tmp_stack = []

    for e in s:
        if e not in open_close:
            tmp_stack.append(e)
        else:
            if not tmp_stack or open_close[e] != tmp_stack.pop():
                return False
    
    return False if tmp_stack else True


if __name__ == "__main__":
    print(isValid("[]")) # true
    print(isValid("([{}])")) # true
    print(isValid("[(])")) # false
    print(isValid("[")) # false

