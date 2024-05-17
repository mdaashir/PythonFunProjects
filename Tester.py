from os import system
import time
# Time Clock(start)
start = time.time()

# main program starts here

for i in range(5):
    print('aashir')

print('available'.center(25,'*'))

for i in range(len('COMPUTER'),0,-1):
    print('COMPUTER'[:i])

# Time Clock(end)
end = time.time()
# Time elapsed(start-end)
seconds = end - start
# clear screen
# system('cls')
# system('clear')
# Print time executed
print('Execution time: {0:.03f} s'.format(seconds))
# input('Press ENTER to continue......')
