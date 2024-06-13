howmany=input("How many pizzas will you order?")

number_of_tops=input("How many toppings")
number_of_tops=int

if number_of_tops==0:
    print("Cheese only it is!")
elif number_of_tops==1:
    topping1= input("What is your first topping")
    print(f' {topping1.upper()} will be added to your pizza!')
elif number_of_tops==2:
    topping2= input("What is your second topping")
    print(f' {topping2.upper()}  will be added to your pizza!')
elif number_of_tops == 3:
    topping3:("What will your third topping be?")
    print(f' {topping3.upper()}  will be added to your pizza!')
else:
    print("You have ordered too many toppings. Please enter 0-3 toppings")



