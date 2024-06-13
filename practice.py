a=17

guess = int(input("What is your lucky number? "))

if guess == 17:
    print("YOU WIN A LIFETIME OF SATISFACTION")
else:
    print("Today is not your lucky day")


authors = []
print(len(authors))
for i in range (1,5):
    authors.append(input(f'Name of author{i}: '))
print(authors)

