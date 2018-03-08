def fact(n):

    # Base case
    if n == 0:
        return 1
    else:
        return n * fact(n - 1)

print(fact(5))


def rec_sum(n):
    # Base case
    if n == 0:
        return 0
    else:
        return n + rec_sum(n - 1)

print(rec_sum(5))


def sum_func(n):

    if len(str(n)) == 1:
        # Base case
        return n
    else:
        # strip another digit
        return n%10 + sum_func(int(n/10))

print(sum_func(54321))


