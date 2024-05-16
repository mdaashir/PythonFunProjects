from os import system
import time
# Time Clock(start)
start = time.time()

def lcm_gcd(x,y):
    gcd=x if x>y else y
    lcm=y if x>y else x
    while gcd%x != 0 or gcd%y != 0 or x%lcm != 0 or y%lcm != 0:
        if ((gcd%x != 0) or (gcd%y != 0)):
            gcd+=1
        if ((x%lcm != 0) or (y%lcm != 0)):
            lcm-=1
    return (gcd,lcm)

def values(a):
    if any(num <= 0 for num in a):
        print('Check your inputs for non-zero.')
        exit()
    for _ in range(1,len(a)):
        gcd,lcm=lcm_gcd(a[_],a[_-1])
    print('Gcd = {}\nLcm = {}'.format(gcd,lcm))


try:
    values(eval(input('Enter a list of numbers (e.g., [1, 2, 3]): ')))
except:
    print('Check your inputs for atleast two numbers.')

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
