â#!/usr/bin/python3
âimport sys

âdef factorial(n):
â    result = 1
â    while n > 1:
â        result *= n
â        n -= 1
â    return result

âf = factorial(int(sys.argv[1]))
âprint(f)
