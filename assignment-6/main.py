#1
a = 15
b = 20
res = a + b 
print(res)

#2
text = "asylai"
print(text[::-1])

#3
text = "kanagattyndyrilmagandyktarynyzdan"
print(len(text))

#4
first = "Nfactorial"
second = "School"
print(first + second)

#5
char = "e"
vowel = "aeiou"
print(char in vowel)

#6
text = "hello"
result = text[-1] + text[1:-1] + text[0]
print(result)

#7
string = "asylai"
print(string.upper())

#8
length = 15
width = 3
area = length * width
print(area)

#9
number = 8
if number % 2 == 0:
    print("even")
else:
    print("odd")

#10
string = "asylai"
print(string[:3])

#11
name = "Asylai"
age = 18
print(f"Hello! My name is {name}, I'm {age} y.o")

#12
string = "asylai"
print(string[2:6])

#13
number = "18"
print(int(number))

#14
text = "Asy"
repeated = text * 3
print(repeated)

#15
a = 15
b = 6
quotient = a // b
reminder  = a % b
print(f"quotient = {quotient}, reminder = {reminder}")

#16
a = 15
b = 6
print(a/b)

#17
text = "kanagattyndyrilmagandyktarynyzdan"
print(text.count("k"))

#18
text = "The name of this school \"Nfactorial\""
print(text)

#19
multi_line = '''
kanagattyndyrilmagandyktarynyzdan
The name of this school Nfactorial
asylai
'''
print(multi_line)

#20
base  = 5
exponent = 3
print(base ** exponent)

#21
is_palindrome = "racecar"
if is_palindrome == is_palindrome[::-1]:
    print(True)
else:
    print(False)

#22
str1 = "listen"
str2 = "silent"
if sorted(str1.lower()) == sorted(str2.lower()):
    print(True)
else:
    print(False)