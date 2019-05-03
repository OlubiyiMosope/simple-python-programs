def prime_range(num):
    is_prime = []
    test_prime = []

    for n in range(1,num):
        if num % n == 0:
            test_prime.append(n)
            
    if len(test_prime) == 1:
        is_prime.append(num)
    return is_prime


    
    for n in range(1,num):
        if num % n == 0:
            test_prime.append(n)

    if len(test_prime) == 1: