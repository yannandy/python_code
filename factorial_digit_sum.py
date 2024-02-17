#n! means n × (n − 1) × ... × 3 × 2 × 1.
#For example, 10! = 10 × 9 × ... × 3 × 2 × 1 = 3628800, and the sum of the digits is 3 + 6 + 2 + 8 + 8 + 0 + 0 = 27.
#The aim of this algorithm is to find the sum of the digits of n!.

def get_factorial(n):
    facto = n
    for i in range (n-1,1,-1):
        facto *= i 
    return str(facto)

def factorial_digits_sum(result_factoriel):
    list_number = [int(char) for char in result_factoriel]
    digit_sum = sum(list_number)
    return digit_sum

def main():
    n = 100
    results = factorial_digits_sum(get_factorial(n))
    print(results)

if __name__ == '__main__':
    main()