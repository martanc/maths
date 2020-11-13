def commonDivisors(num1, num2):
    """
    Calculates the common divisors from both numbers
    
    :param num1, num2: numbers from which calculate the common divisors
    """

    divisors = list()
    for x in range(1, min(abs(num1), abs(num2))+1):
        if (num1 % x == 0 ) & (num2 % x == 0):
            divisors.append(x)
    return divisors

def divisors(num):
    """
    Calculates the divisors from the input number
    
    :param num1: number from which calculate the divisors
    """
    divisors = list()
    for x in range(1, abs(num)+1):
        if num % x == 0:
            divisors.append(x)
    return divisors

def factorize(num):
    """
    Calculates the factorization of the number in prime numbers
    
    :param num: number from which calculate the factorization
    """
    divisors = list()
    prime = 2
    while(num > 1):
        if num % prime == 0:
            divisors.append(prime)
            num = num / prime
        else:
            prime += 1
    return divisors

if __name__ == "__main__":
    print("Welcome to elementary.")
