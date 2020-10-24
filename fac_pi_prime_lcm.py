import math


def factorial(n):
    """Computes factorial of n recursively."""
    if n == 0:
        return 1
    else:
        recurse = factorial(n-1)
        result = n * recurse
        return result


def estimate_pi():
    total = 0
    k = 0
    factor = 2 * math.sqrt(2) / 9801
    while True:
        num = factorial(4*k) * (1103 + 26390*k)
        den = factorial(k)**4 * 396**(4*k)
        term = factor * num / den
        total += term
        
        if abs(term) < 1e-15:
            break
        k += 1

    return 1 / total

print(estimate_pi())


def is_prime(num):
    if num > 1:
        if num == 2:
            return True
        if num%2 == 0:
            return False
        for i in range(3, int(math.sqrt(num))+1, 2):
            if num%i == 0:
                return False
        return True
    return False

def lcm(number):
    prime = []
    lcm_value = 1
    for i in range(2,number+1):
        if is_prime(i):
            prime.append(i)
    final_value = []
    for i in prime:
        x = 1
        while i**x < number:
            x = x + 1
        final_value.append(i**(x-1))
    for j in final_value:
        lcm_value = j * lcm_value
    return lcm_value

if __name__ == '__main__':
    print(lcm(20))
