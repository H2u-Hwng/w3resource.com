# The program prompts the user for an integer n.
# It then calculates and displays the value of n + nn + nnn.

# Prompt user for an integer n
num = int(input('Enter an integer: '))

# Calculate and display the value of n + nn + nnn
n = int('%s' % num)
nn = int('%s%s' % (num, num))
nnn = int('%s%s%s' % (num, num, num))

print(f'The value of n + nn + nnn is {n + nn + nnn}.')
