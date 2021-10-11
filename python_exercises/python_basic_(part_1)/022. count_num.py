# Define list count 4 function
def list_count_4(num_list):
    
    # Assume count
    count = 0
    
    # Count 4 in list
    for n in num_list:
        if n == 4:
            count += 1
    
    return count

# Define main function
def main():
    
    # Prompt user for numebers of list
    num_list = [int(num) for num in input('Enter the list: ').split(',')]
    
    # Get list count 4
    count = list_count_4(num_list)
    
    # Display list count 4
    print(f'The total number 4 in the list is {count}.')
    
# Call main function
main()
