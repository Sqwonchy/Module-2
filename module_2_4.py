numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15] # множество чисел
primes = [] # Простые числа
not_primes = [] # Составные числа
for i in range(len(numbers)):
    n = numbers[i]
    if n < 2: # можно сделать  if n == 1 or if n == 0:  но я решил так. если нужно с учетом отрицательных чисел в множестве то можно и это вариант
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
