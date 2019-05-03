from check_prime import check_prime

def prime_range(num):
    '''This function imports the check_prime function from the module of the same name.
It takes an integer as a parameter and returns a list of prime numbers that exist between 1 and that integer'''
    is_prime = []
    
    for n in range(1,num):
        if check_prime(n):
            is_prime.append(n)
    return is_prime
