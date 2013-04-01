def fib(n):
    print 'n = ', n
    if n > 1:
        return n * fib(n - 1)
    else:
        print 'end of the line'
        return 1

for n in range(1, 10):
    print fib(n)
