import math

i=0
while i<=50:
    print(i)
    i=i+5


sum=0
for i in range(1,101):
    sum = sum+i

print(sum)


for i in range (1,4):
    print("i",i)
    for j in range (1,4):
        print(" j",j)
        for k in range (1,4):
            print("  k",k)



i,j,breakbreak = 0,0,0
while True:
    i+=1
    j=0
    while j<=3:
        print(i, j, '\n')
        j+=1
        user_input=input('Continue? (y/n):')
        if(user_input=='n'):
            breakbreak=1
            break
    if(breakbreak==1):
        break





# Initialize the first two terms
prev_prev_term = 0
prev_term = 1

# Define the number of terms you want to generate
num_terms = 10

# Print the first two terms
print(prev_prev_term)
print(prev_term)

# Loop to generate and print the remaining terms
for _ in range(num_terms - 2):
    current_term = prev_prev_term + prev_term
    print(current_term)
    
    # Update previous terms for the next iteration
    prev_prev_term = prev_term
    prev_term = current_term
