# If char 'C' is found then check if D is next to 'C'. If yes, remove 'C' and 'D'.
# If char 'CA' is found then check if B is previous to 'A'. If yes, remove 'B' and 'A'.

def transform(s): # stack O(N)
    stack = []
    for c in s:
        if stack and stack[-1] + c in ("AB", "BA", "CD", "DC"):
            stack.pop()
        else:
            stack += c
    return "".join(stack)
                        



s = 'CBACD' # 'C'
s = 'CABABD' # ''
S = 'ACBDACBD' # ''
print(transform(s))
