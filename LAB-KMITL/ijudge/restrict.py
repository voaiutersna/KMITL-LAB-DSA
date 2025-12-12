    for i in x:
        if i == "(":
            stack.push(i)
        if i == ")":
            stack.pop()
