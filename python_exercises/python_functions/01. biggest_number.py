# Compare 2 numbers and return bigger number
def max_of_two(num1, num2):
    
    # Compare 2 number
    if num1 > num2:
        bigger_num = num1
    else:
        bigger_num = num2

    return bigger_num


# Compare 3 numbers and return biggest number
def max_of_three(num1, num2, num3):
    
    # Compare 3 numbers
    biggest_num = max_of_two(num1, max_of_two(num2, num3))
    
    return biggest_num

    
# Define main function
def main():
    
    # Prompt user for 3 numbers
    number1 = float(input('Enter the number one: '))
    number2 = float(input('Enter the number two: '))
    number3 = float(input('Enter the number three: '))
    
    # Obtain biggest number
    biggest_number = max_of_three(number1, number2, number3)
    
    # Display biggest number
    print(f'The Max of number {number1}, {number2}, and {number3} \
is {biggest_number}.')
    
# Call main function
main()
