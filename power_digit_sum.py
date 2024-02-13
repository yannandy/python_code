#2 ** 15 = 32768 and the sum of its digits is 3 + 2 + 7 + 6 + 8 = 26.
#The purpose is to find the sum of the digits of the number 2 ** exponent.

def powerDigitSum(exponent):
    number_in_string = str(2 ** exponent)
    list_number = [int(char) for char in number_in_string]
    digit_sum = sum(list_number)
    return digit_sum, number_in_string

def main():
    exponent = 15
    results = powerDigitSum(exponent)
    print(f'The result of 2 exponent {exponent} is {results[1]} and the sum of the digits is {results[0]}')

if __name__ == '__main__':
    main()