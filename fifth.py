# person = input("Nationality? ").lower()

# if person == "french" or person == "francais":
#     name = input("Comment tu t'appelle? ").title()
#     going_to_school = input("Allez-vous à l'école? ")
    
#     if going_to_school == "yes":
#         print(f"Bienvenue chez au univelcity, {name}.")
#     else:
#         print(f"Au revoir, {name}. Bonne journée.")
    
# elif person == "italian":
#     print("Preferisci parlare italiano?")
# else:
#     print("You are neither French nor Italian.")
#     print("So, let us speak English!")



# def factorial(n):
#     if n == 1:
#         return 1
    
    
#     return n * factorial(n-1)


# print(factorial(7))


import random as rd

from numpy import average
# from random import choice

# name = "Desmond"

# print(choice(name))


# print(list(range(2, 10, 2)))

##### LIST

# my_list = [4,3,5,7,36,7]
# print(my_list)

# my_list[3]=90

# print(my_list)


# num = list(range(50,53805))
# rd.shuffle(num)

# print(sorted(num, reverse=True)[:5])


#### guess gamee

# import random

# print("Welcome to my game")
# num = list(range(53, 74))

# random.shuffle(num)

# print("You can select from the list below.")
# print(num)
# user_choice = int(input(">"))
# com_choice = random.choice(num)

# if user_choice in num:
#     if user_choice == com_choice:
#         print("You win!")
#     else:
#         if user_choice > com_choice:
#             print("Too High")
#         else:
#             print("Too low")
            
#     print(f"Computer choice: {com_choice}")
# else:
#     print("Invalid input")
    
    


### LISTS AGAIN

# list1 = [4,3,5,6,7,8]
# list2 = [9,4,2,5,7,9]

# list3 = list1.copy()

# list1[0]=50

# print(list1)
# print(list3)



# list1.append(list2) #add element to the end of the list

# list1.extend(list2)

# list1.clear()

# list1.insert(3,"Inserted")

# list1.remove(7)
# a = list1.pop(4)
# print(a)
#list1.sort()

# list1.reverse()

# print(list1)

# data=[i for i in range(1,12)]
# chosen = [7,4]
# for i in chosen:
#     data.remove(i)

# a = rd.choice(data)


# print(a)



##### CORRECTION ############

#Q1
# a = float(input("enter first number: "))
# b = float(input("enter second number: "))
# c = float(input("enter third number: "))
# sum_of_3 = a + b + c 
# frequency = 3
# average = sum_of_3 / frequency
# print(average)


###Q2
# user = input("enter your sentence:  ")
# a = user.split()
# print(a)
# a[0] = a[0].upper()
# print(a)
# print(" ".join(a))


###Q3
#Write a program with the sentence "I am learning python". When your program is run, the string "I" should be changed to "you"


a = "I am learning python"
print(a.replace("I", "You"))


## Q4
# Write a program that takes the string "I hope you had fun today in class". Print the number of times that the string "a" appears in the sentence.


b = "I hope you had fun today in class"
print(b.count("a"))


##Q5
def check_fermat(a,b,c,n):
    if n > 2 and (a**n + b**n == c**n):
        print("Holy smokes, Fermat was wrong!")
    else:
        print("No, that doesn't work.")
        
        
        
def get_data():
    a =int(input())
    b =int(input())
    c =int(input())
    n =int(input())
    
    check_fermat(a,b,c,n)
    
    
get_data()
    