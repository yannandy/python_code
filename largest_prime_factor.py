#The objective of this algorithm is to perform the decomposition into the product of prime factors and give the largest factor in this decomposition.
#the decomposition into the product of prime factors is done on the basis of prime numbers.
#the decomposition stops when the prime number to be tested is greater than the square root of the number provided

import math

#This function gives the list of all prime numbers less than the square root of the given number.
def list_of_prime_numbers(number):
    number=math.ceil(math.sqrt(number))
    prime_numbers = []
    number_of_divisors = 0
    for i in range(2,number+1):
        for j in range(1,i+1):
            if i % j == 0:
                number_of_divisors += 1

                #A number is said to be prime if it is divisible only twice; by 1 and by itself
        if number_of_divisors <= 2:
            prime_numbers.append(i)

        number_of_divisors = 0

    return prime_numbers

#this function returns the prime numbers constituting the decomposition into prime factors
def decomposition_prime_factor(prime_numbers, number_to_be_decomposed):
    prime_factor = []
    result = number_to_be_decomposed
    for prime_number in prime_numbers:
        if result == 1: 
                break
        else:
            while result % prime_number == 0:
                if result == 1: 
                    break
                else: 
                    result /=  prime_number
                    prime_factor.append(prime_number)
    if result != 1:
        prime_factor.append(result)
    return prime_factor

def main():
    given_number = 10
    x = list_of_prime_numbers(given_number)
    print(f'The list of the prime numbers less than square root of {given_number} is: {x}')
    y = decomposition_prime_factor(x, given_number)
    print("The decomposition in prime factor is", y)
    print("The largest prime factor is: ", max(y))

if __name__ == '__main__':
    main()