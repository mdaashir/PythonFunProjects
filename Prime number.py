from os import system
import time
# Time Clock(start)
start = time.time()

class prime():
    def inputdata(self):
        self.__data=[]
        self.__end=int(input('Enter the End Value => '))
        for self.__i in range(1,(self.__end)+1):
            self.__j=2
            self.__f=0
            while self.__j < self.__i:
                if self.__i % self.__j == 0:
                    self.__f=1
                self.__j+=1
            if self.__f == 0:
                self.__data.append(self.__i)
        return print(self.__data)

    def __init__(self):
        print('....List of Prime Numbers....\n')
        self.inputdata()
        while True:
            if input('Enter 00 to Stop [OR] Press Enter ') == '00':
                break
            self.inputdata()
        return print('Owned By AASHIR IT Solutions Pvt.Ltd.')

prime()

# Time Clock(end)
end = time.time()
# Time elapsed(start-end)
seconds = end - start
# clear screen
# system('cls')
system('clear')
# Print time executed
print('Execution time: {0:.03f} s'.format(seconds))
# input('Press ENTER to continue......')
time.sleep(1)
# sys.exit()
