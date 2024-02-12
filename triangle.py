#The sequence of triangle numbers is generated by adding the natural numbers. So the 7th triangle number would be 1 + 2 + 3 + 4 + 5 + 6 + 7 = 28.
#28: 1, 2, 4, 7, 14, 28. We can see that 28 is the first triangle number to have over five divisors.
#The purpose is to find the value of the first triangle number to have over n divisors?

def factors(n):
    list=[*range(1, n+1)]
    another_list = [num for num in list if n % num == 0]
    return another_list

def divisibleTriangleNumber(n):
    natural_number = 2
    triangle_number = 1
    list_of_factors = []

    while True:
        list_of_factors = factors(triangle_number)
        if len(list_of_factors) <= n:
            triangle_number += natural_number
            natural_number += 1
        else: 
            break
    return list_of_factors,triangle_number

def main():
    n = 5
    tuple = divisibleTriangleNumber(n)
    print(f'The first triangle number to have over {n} divisors is {tuple[1]} and the factors are {tuple[0]}')

if __name__ == '__main__':
    main()