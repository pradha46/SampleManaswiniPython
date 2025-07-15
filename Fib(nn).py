def fib(nn):
    if nn == 0:
        return 0
    elif nn == 1:
        return 1
    else:
        a, b = 0, 1
        for _ in range(2, nn + 1):  # Iterate from the 2nd term up to nn
            next_fib = a + b
            a = b
            b = next_fib
        return b
