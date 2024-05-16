from os import system
import time,sys
# Time Clock(start)
start = time.time()

try:
    print('Press Ctrl-C to quit...\nMaximize the screen')
    time.sleep(2)
    while 1:
        for i in range(168):
            print('\aSystem Error!!!'*i,end='\t')
            print('a'.center(i,'~'))
            print('\aSystem Error!!!'*i,end='\t')
except KeyboardInterrupt:
    sys.exit()

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
