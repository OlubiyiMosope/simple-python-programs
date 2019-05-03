def divisors(num):
    ''' takes in an integer as a parameter then prints out a list of all the divisors of that integer.'''

    divisors = []
    for n in range(1,num):
        if num % n == 0:
            divisors.append(n)

    print(f'the divisors of {num} are:')
    return divisors