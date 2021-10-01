def calculator(s):
    result = 0
    sign = 1
    stack = []
    operationStack = []

    for i in range(len(s)):
        curr = s[i]
        if curr == " ":
            continue
        elif curr == "+":
            sign = 1
        elif curr == "-":
            sign = -1
        elif curr >= "0" and curr <= "9":
            num = curr
            while i + 1 < len(s) and s[i + 1] >= "0" and s[i + 1] <= "9":
                num += s.charAt(i + 1)
                i += 1

            result += sign * int(num)
        elif curr == "(":
            stack.append(result)
            result = 0
            operationStack.append(sign)
            sign = 1
            print('stack', stack,'operationStack',operationStack)
        elif curr == ")":
            result = operationStack.pop() * result + stack.pop()
            sign = 1

    return result

#print(calculator('2 + 2'))
print(calculator('(2+2) - 3'))
