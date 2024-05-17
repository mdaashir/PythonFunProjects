# Import modules
from os import system
import time
# Time Clock(start)
start = time.time()


# main program starts here


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
