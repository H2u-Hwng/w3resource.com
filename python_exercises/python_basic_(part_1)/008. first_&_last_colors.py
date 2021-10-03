# The program prompts the user for the number and name of colors.
# It then displays the first and last colors of the colors' list

# Prompt user for number and name of colors
color_num = int(input('Enter the number of colors: '))
color_list = [input(f'Enter the color number {n}: ')
              for n in range(1, color_num + 1)]

# Displays the first and last colors
print(f'''The first color from the list is {color_list[0]}.
The last color from the list is {color_list[-1]}.''')