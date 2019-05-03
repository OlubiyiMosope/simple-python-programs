fib_seq = [1, 1]
def fib(n):
    '''
    This function takes in an integer and reurns the integer's length of the fibonacci sequence.'''

    
    if len(fib_seq) != n:
        nxt = fib_seq[-1] + fib_seq[-2]
        fib_seq.append(nxt)
        return fib(n) # recursive case - here, the function  calls itself.
    else:
        return fib_seq # base case - here, the function does not call itself.
    
fib(5)