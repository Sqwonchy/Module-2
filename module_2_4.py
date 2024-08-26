numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15]
primes = []
not_primes = []
for i in range(len(numbers)):
    n = numbers[i]
    if n < 2:
        continue
    else:
        is_prime = True
        for k in range(2, n):
            if n % k == 0:
                is_prime = False
                break
            else:
                continue
        if is_prime == True:
            primes.append(n)
        elif is_prime == False:
            not_primes.append(n)
print(primes)
print(not_primes)
