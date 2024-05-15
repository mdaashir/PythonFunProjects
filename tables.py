from os import system
import time
# Time Clock(start)
start = time.time()

for i in range(int(input('Enter a table number: ')),0,-1):
    for j in range(int(input('Enter a multiple number: '))+1):
        print(i,'X',j,'=',i*j)
    break

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
