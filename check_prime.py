def check_prime(num):
    '''This function takes in a number as a parameter and determines whether the number is prime or not.'''
    test_prime = []
    
    for n in range(1,num):
        if num % n == 0:
            test_prime.append(n)

    if len(test_prime) == 1:
        return True

    return False