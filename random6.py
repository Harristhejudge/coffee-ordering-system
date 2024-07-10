print("Hello welcome to coffee")

name = input("What is your name? ")

print("Hello " + name + "what can i get for you today")

print("Here we got this menu") 

print("Our menu includes following")
      

print("1. coffee")
print("2. latte")
print("3. cappuccino")
print("4. Tea")


choice = input("Please enter the number of the item you'd like to order: ")

if choice == '1':
    menu_item = "coffee"

elif choice == '2':
  menu_item = "Latte" 

elif choice == '3':
    menu_item = "cappucino"

elif choice == '4':
    menu_item = "Tea"

else: 
    print("Choose from 1 to 5. you entered wrong number")



if menu_item: 
    print("Thanks for ordering " + menu_item + "! we will get back at you in a minute")






 





