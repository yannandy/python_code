#This program takes a number and gives the list of numbers multiples of 3 or 5.
#The sum of all these numbers are displayed.
def multiple_of_3_or_5(number):
    list = [i for i in range(number)
            if (i%3 == 0 or i%5 == 0)
           ]
    return list

def main():
    while 1:
        print("\nDepending on your input, this program will list all the numbers multiples of 3 or 5 and display the sum")
        number = int(input('Enter the number : '))
        list_of_multiple = multiple_of_3_or_5(number)
        total = sum(list_of_multiple)
        print(f'\nThe list of numbers multiple of 3 or 5 are :{list_of_multiple}\n and the total is {total}')

if __name__ == '__main__':
    main()
