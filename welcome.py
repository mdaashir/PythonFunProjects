from os import system
import time
# Time Clock(start)
start = time.time()

a=input('Enter your Name? ')
print('Hello!',a)
print('Hi,glad to meet you fine')
b=int(input('What is your Age? '))
if b<=18:
    print('You can\'t vote')
else:
    print('You can vote')

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
time.sleep(1)
# sys.exit()
