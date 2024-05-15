from os import system
import time
# Time Clock(start)
start = time.time()

class Days_of_week():
    __weekday=['Sunday','Monday','Tuesday','Wednesday','Thursday','Friday','Saturday']
    __months=['January','Febuary','March','April','May','June','July','August','September','October','November','December']
    def inputdata(self):
        while True:
            self.values=input('Enter DD:MM:YYYY =>')
            self.__idate=int(self.values[:2])
            self.__imonth=int(self.values[3:5])
            self.__iyear=int(self.values[6:])
            self.__pyear=self.__iyear
            if self.__idate > 0 and self.__idate < 32:
                if self.__imonth > 0 and self.__imonth < 13:
                    if self.__iyear > 0:
                        break
                    else:
                        print('Incorrect Year')
                else:
                    print('Incorrect Month')
            else:
                print('Incorrect Day')
            print('Try Again....')
        return

    def convert(self):
        self.__iyear-=1900
        self.__days=(30.42*(self.__imonth-1))+self.__idate
        if self.__imonth==2:
            self.__days+=1
        if self.__imonth > 2 and self.__imonth < 8:
            self.__days-=1
        if self.__iyear%4==0 and self.__imonth > 2:
            self.__days+=1
        self.__cycle=self.__iyear/4
        self.__days+=int(self.__cycle)*1461
        self.__year=self.__iyear%4
        if self.__year > 0:
            self.__days+=(365*self.__year)+1
        if self.__days > 59:
            self.__days-=1
        self.__day=self.__days%7
        return int(self.__day)

    def __init__(self):
        print('....Days of Week Convertor....\n')
        self.inputdata()
        while True:
            ans=self.convert()
            print(self.__weekday[ans],self.__idate,self.__months[self.__imonth-1],self.__pyear)
            if input('Enter 00:00:00 to Stop [OR] Press Enter ') == '00 00 00':
                break
            self.inputdata()
        print('Owned By AASHIR IT Solutions Pvt.Ltd.')
        return


Days_of_week()

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
