from os import system
import time
# Time Clock(start)
start = time.time()

# main program starts here:
def main():
    print("Hello Python!")
if __name__ == "__main__":
    main()

def main():
    print("I am a general syntax Python file")
if __name__ == "__main__":
    main()

def main():
    print("I am a general syntax Python file")
    LetUsDoSomething()
def LetUsDoSomething():
    print("I am doing something")
if __name__ == "__main__":
    main()


def main():
    print('A line inside main function.')
print("A line outside main function.")
if __name__ == main():main()


def main():
    print('A line inside main function.')
    print("A line outside main function.")
if __name__ == main():main()


def main():
    print('A line inside main function.')
    print("A line outside main function.")
    OutsideMainFunction()
def OutsideMainFunction():
    x = 0
    while x < 5:
        print(x)
        x = x + 1
if __name__ == main():main()

# this is main() function
def main():
    OutsideMainFunction()
# this function is outside main() function
def OutsideMainFunction():
    x = 0
    while x < 5:
        print(x)
        x = x + 1
if __name__ == main():main()



a = 1
print(a)
print(type(a))
print(id(a))
a = "One"
print(a)
print(type(a))
print(id(a))


def main():
    x = 1
    print(x)
    print(id(x))
    print(type(x))
    x = 2
    print(x)
    print(id(x))
    print(type(x))
    x = 1
    print(x)
    print(id(x))
    print(type(x))
if __name__ == "__main__":
    main()


# in python everything is object
# a variable is a reference to an object
# each object has an identity or an ID
x = 1
print(type(x))
print(id(x))
##################
# class 'int'
# 139113568
##################
# number, string, tuple -> immutable
# list, dictionary -> mutable
x = 1
y = 1
print(type(x))
print(id(x))
print(type(y))
print(id(y))
if x == y:
    print("True")
else:
    print("False")
if x is y:
    print("True")
else:
    print("False")
##################
# see the last two lines, both are true
# class 'int'
# 139113568
# class 'int'
# 139113568
# True
# True
##################
a = dict(x = 1, y = 1)
print(type(a))
print(id(a))
b = dict(x = 1, y = 1)
print(id(b))
if a == b:
    print("True")
else:
    print("False")
if a is b:
    print("True")
else:
    print("False")
##################
# see the last two lines, one is true but the id is not same so it is false
# class 'dict'
# 3072650252
# 3072692524
# True
# False
##################
for i in range(0, 3):
    print(i, "=", id(i))
##################
# 0 = 139113552
# 1 = 139113568
# 2 = 139113584
##################


def main():
    x = 3
    print(x)
    print(id(x))
    print(type(x))
    print("*********")
    x = 3 /2
    print(x)
    print(id(x))
    print(type(x))
    print("*********")
    x = round(42 / 9)
    print(x)
    print(id(x))
    print(type(x))
    print("*********")
# we want to round it up
    x = 42 // 9
    print(x)
    print(id(x))
    print(type(x))
    print("*********")
# how many digits we want to round to
    x = round(42 / 9, 3)
    print(x)
    print(id(x))
    print(type(x))
    print("*********")
    x = 43 % 7
    print(x)
    print(id(x))
    print(type(x))
    print("*********")
    x = int(34.78)
    print(x)
    print(id(x))
    print(type(x))
    print("*********")
    x = float(23)
    print(x)
    print(id(x))
    print(type(x))
    print("*********")
if __name__ == "__main__":
    main()


def main():
    strings = "I love you."
    print(strings)
    anotherStrings = "I love you but\nI don't know how much you love me."
    print(anotherStrings)
if __name__ == "__main__":
    main()


def main():
    strings = "I love you."
    print(strings)
    anotherStrings = "I love you but\nI don't know how much you love me."
    print(anotherStrings)
    rawStrings = r"I love you but\nI don't know how much you love me."
    print(rawStrings)
if __name__ == "__main__":
    main()

days = 8
lyrics = "%s days a week is not enough to love you." %days
print(lyrics)

days = 8
lyrics = "{} days a week is not enough to love you."
print(lyrics.format(days))

newLines = """\
first line
second line
third line
more to come...
"""
print(newLines)

x = (1, 2, 3, 4)
print(x)
print(type(x))
for i in x:
    print(i)


# tuple
x = (1, 2, 3, 4)
# list
a = [1, 2, 3, 4]
# appending tuple x to list
a.append(x)
print(a)
# inserting tuple x in the first position
a.insert(0, x)
print(a)
# Now iterating the final list a
for i in a:
    print(i)

strings = "This is a string."
for WeWillIterateThroughIt in strings:
    print(WeWillIterateThroughIt)

strings = "string."
print(strings[1:3])

#!usr/bin/python3
EnglishDictionaries = {'bare':'jejune',
'anger':'dudgeon', 'abuse':'vituperate',
'howl':'ululate'}
print(EnglishDictionaries)
# getting in a nmore human readable form
for keys in EnglishDictionaries:
    print(keys, "=", EnglishDictionaries[keys])

EnglishDictionaries = {'bare':'jejune',
'anger':'dudgeon', 'abuse':'vituperate',
'howl':'ululate'}
for keys in sorted(EnglishDictionaries.keys()):
    print(keys, "=", EnglishDictionaries[keys])

synonyms = dict(bare='jejune', anger='dudgeon', abuse= 'vituperate', howl= 'ululate')


class Human:
    def __init__(self, kind = "Good"):
        self.kind = kind
    def whatKind(self):
        return self.kind
def main():
    GoodHuman = Human()
    print(GoodHuman.whatKind())
    BadHuman = Human("Bad")
    print(BadHuman.whatKind())
if __name__ == "__main__":
    main()

class Human:
    def __init__(self, kind = "Good"):
        self.kind = kind
    def whatKind(self):
        return self.kind

def main():
    GoodHuman = Human()
    print(GoodHuman.whatKind())
    BadHuman = Human("Bad")
    print(BadHuman.whatKind())
if __name__ == "__main__":
    main()

def conditionals_exec():
    a, b = 1, 3
    if a < b:
        print("a is less than b")
    elif a > b:
        print("a is greater than b")
    else:
        print("a is equal to b")
conditionals_exec()


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
