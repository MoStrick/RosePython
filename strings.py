a1='Hello!'
a2="Wild"
a3='''
Cats!!!
    tiger king!'''


# finding length and printing length
print(f'{a1}{a2}{a3}')
print()

print(len(a1))
length=0
for i in a1:
    length=length+1
print(length)

print(f'a1 length:{len(a1)}, a2 length:{len(a2)}, a3 length:{len(a3)}')
for i in a1:
    print(i)

# print elements in each string
print(a1[0],a1[1],a1[2],a1[3],a1[4],'\n')

print(a1[0],'\n', a1[1], '\n', a1[2], '\n', a1[3], '\n', a1[4], '\n')


# Determine if elements/minor strings are present or not in the string
print('ello' in(a1 or a2 or a3))
if 'ola' not in (a1 or a2 or a3):
    print('Nope, not found!')

# String Slicing
print(len(a1))
print(a1[0:len(a1)])
print(a2[0:len(a2)])
print(a3[0:len(a3)])

## Last index in slicing is not included: skips element 0, includes elements 1,2,3,4, does not include element 5
print(a1[1:5])

##Slice to the end from index 3
print(a1[3:7])
print(a1[3:len(a1)])

print(a1[0:len(a1)-3])
print(a1[:-3])

# capitalize/lowercase
print(a1.upper(), a1.lower())

#Capitalize the first letter of every word
print(a3.title())

#remove all spaces before and after
print(a3.strip())

a4=a2.replace('Wild','Python')
print(a4)

a5= 'Hello World'

print(a5.split("!"))

print('@'.join(['stricklandm','cleverbluejays.org']))

print(a5+a3.title() .strip()+'<3')


# Formatiing strings


# String Comparison
#== are they exactly the same?
#using is or isnot is boolean and will determine a true false value for if they are located in the same place/have the same memory location


#search within a string (find a substring): Output will be the first index number where the string occurs
a6="Hello, Class! Today we are learning Python."
###Does the data contain the string lo inside of it anywhere
print(a6.find('lo'))
### Does the string contain the string ass inside of it AFTER index 5?
print(a6.find('ass'),5)
###Does the string contain the string ass BETWEEN index character 6-12 (including character 6, not including character 12)
print(a6.find ('ass'), 6,12)

print(a6.find('o'))

print(a6.rfind('o'))

print(a6.count('o'))



