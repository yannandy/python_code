#                   TASK
#By considering the terms in the Fibonacci sequence whose values do not exceed n, 
#find the sum of the even-valued terms.

#This function takes a number and return a sequence whose values do not exceed n.
#This sequence is stored in a list
def get_list_of_fibonacci_number(number): 
    list_fibonacci_number = []

    if number == 1:
        list_fibonacci_number = list_fibonacci_number.append(1)
    
    else:
        list_fibonacci_number = [1, 2]
        while number >= list_fibonacci_number[-1]+list_fibonacci_number[-2]:
            sum_of_last_two_numbers = list_fibonacci_number[-1]+list_fibonacci_number[-2]
            list_fibonacci_number.append(sum_of_last_two_numbers)

    return list_fibonacci_number

#This fuction takes a list and return the sum of the even numbers
def get_sum_of_even_fibonacci_number(list):
    even_fibonacci_sum = 0
        
    for num in list:
        if num % 2 == 0:
            even_fibonacci_sum += num
    
    return even_fibonacci_sum

def main():
    number = 1000
    sequence_of_fibonacci_number = get_list_of_fibonacci_number(number)
    print(f'Fibonacci sequence whose values do not exceed {number} is {sequence_of_fibonacci_number}')
    print(f'The sum of the even number in this sequence is {get_sum_of_even_fibonacci_number(sequence_of_fibonacci_number)}')

if __name__ == '__main__':
    main()        
    
    