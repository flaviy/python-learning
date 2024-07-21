def count_primes(num):
    if num < 2:
        return 0

    def is_prime(n):
        if n < 2:
            return False
        for i in range(2, n):
            if n % i == 0:
                return False
        return True

    prime_list = [i for i in range(0, num + 1) if is_prime(i)]
    print(prime_list)
    return len(prime_list)


print(count_primes(99))


# another way to solve this problem
def count_prime_numbers(number):
    prime_numbers = [2]
    iteration = 3

    if number < 2:
        return 0

    while iteration <= number:
        for n in range(3, iteration, 2):
            if iteration % n == 0:
                iteration += 2
                break
        else:
            prime_numbers.append(iteration)
            iteration += 2

    print(prime_numbers)
    return len(prime_numbers)


print(count_prime_numbers(99))
