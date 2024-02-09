#The goal is to find the smallest positive number that is evenly divisible by all of the numbers from 1 to n
#2520 is the smallest number that can be divided by each of the numbers from 1 to 10 without any remainder.

def smallest_mult(n):
    #Create a list of number from 1 to n
    range_number_list = [*range(1,n+1)]
    number = 1
    #We perform the modulo operation between the number and each element of the list.
    #If the modulo is equal to 0 for each operation then the number is divided by the whole list and therefore represents the smallest multiple.
    while sum(list(map(lambda list_of_numbers: number % list_of_numbers, range_number_list))) != 0:
        number += 1
    return number

def main():
    n = 13
    print(smallest_mult(n))

if __name__ == '__main__':
    main()
