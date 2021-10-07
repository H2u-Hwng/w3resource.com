# Define test num function
def test_num(num1, num2):
    
    # Test number
    if num1 == num2 or num1 + num2 == 5 or abs(num1 - num2) == 5:
        return True
    else:
        return False
    
# Define main function
def main():
    
    # Prompt user for two numbers
    num1 = int(input('Enter the number 1: '))
    num2 = int(input('Enter the number 2: '))
    
    # Call test num function
    result = test_num(num1, num2)
    
    # Display result
    print(result)
    
# Call main function
main()