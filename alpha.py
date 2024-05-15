from os import system # Importing system module for clearing screen
import time           # Importing time module for measuring execution time

# Time Clock(start)
start = time.time()

i=1  # Initialize the outer loop counter
n=65 # Initialize the ASCII value for 'A'

while(i<=5):  # Outer loop
    j=1       # Initialize the outer loop counter

    while(j<=i):                # Inner loop
        print(chr(n),end=' ')   # Print the character corresponding to the ASCII value
        j+=1                    # Increment the inner loop counter
        n+=1                    # Increment the ASCII value for the next character
    print()
    i+=1

# Time Clock(end)
end = time.time()

# Time elapsed(start-end)
seconds = end - start

# clear screen
#system('cls')
system('clear')

# Print time executed
print('Execution time: {0:.03f} s'.format(seconds))
