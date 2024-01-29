#The goal of this code is to take a camelCase or PascalCase and convert it in snake_case.
#A PascalCase is a string starting with an uppercase letter and which contains lowercase or uppercase letters.
#A camelCase is a string starting with an lowercase letter and which contains lowercase or uppercase letters.
#A snake_case starting with a lowercase letter and each uppercase letter inside is converted to lowercase preceded by an underscore.


#Here is a first way of solving the problem by using a classic for loop.
def convert_to_snake_case1(pascal_or_camel_cased_string):
    snake_cased_char_list = []
    for char in pascal_or_camel_cased_string:
        if char.isupper():
            converted_character = '_' + char.lower()
            snake_cased_char_list.append(converted_character)
        else:
            snake_cased_char_list.append(char)
    snake_cased_string = ''.join(snake_cased_char_list)
    clean_snake_cased_string = snake_cased_string.strip('_')

    return clean_snake_cased_string

#Here is a second way of solving this problem by using a comprehensive list.
def convert_to_snake_case2(pascal_or_camel_cased_string):
    snake_cased_char_list = [
        '_' + char.lower() if char.isupper()
        else char
        for char in pascal_or_camel_cased_string
    ]
    return ''.join(snake_cased_char_list).strip('_')

def main():
    #call of the first function
    print(convert_to_snake_case1('isTHEREAnyone'))
    #call of the second function
    print(convert_to_snake_case2('MyNameIsYANNICK'))
if __name__ == '__main__':
    main()
