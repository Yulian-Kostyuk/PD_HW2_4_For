numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15]
primes = []
not_primes = []
is_prime = True
for i in range(len(numbers)):
    if numbers[i] == 1:
        continue
    elif numbers[i] == 2:
        primes.append(numbers[i])
    else:
        for j in range(len(primes)):
            if numbers[i] % primes[j] == 0:
                is_prime = False
                break
            else:
                is_prime = True
        if not is_prime:
            not_primes.append(numbers[i])
        else:
            primes.append(numbers[i])
print(primes)
print(not_primes)
