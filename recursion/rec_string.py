def reverse(s):

    if len(str(s)) <= 1:
        # Base Case
        return s
    else:
        # abc
        return s[len(str(s)) - 1] + reverse(s[:-1])

print(reverse(123123))