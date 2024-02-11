#The purpose is tof ind the difference between the sum of the squares of the first n natural numbers and the square of the sum.
#For example, the sum of the squares of the first ten natural numbers is 385.
#The square of the sum of the first ten natural numbers is 3025.
#The difference between the sum of the squares of the first ten natural numbers and the square of the sum is 3025 − 385 = 2640.
def sumSquareDiff(n):
    list = [*range(1,n+1)]
    sum_of_square_of_numbers = sum(map(lambda number_in_list: number_in_list ** 2, list))
    square_of_sum_of_numbers = sum(list)**2
    difference = square_of_sum_of_numbers -  sum_of_square_of_numbers
    return (sum_of_square_of_numbers, square_of_sum_of_numbers, difference)

def main():
    n = 100
    tuple = sumSquareDiff(n)
    print(f'The sum of square of the first {n} numbers is {tuple[0]}.\nThe square of the sum of the first {n} numbers is {tuple[1]}.\nThe difference is {tuple[2]}')

if __name__ == '__main__':
    main()
