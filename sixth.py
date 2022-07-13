# import random

# def play_game(user:str, computer:str):
#     """This function plays the rock paper scissors game with the rules that:
#         scissors wins paper
#         rock wins scissors
#         paper wins rock.
#     Rock is represented as R
#     Paper is represented as P
#     Scissors is represented as S.
    
#     Args:
#         user (str): This is the user's choice.
#         computer (str): This is the computer's choice
        
#     Returns:
#         (str): This is the result of the game.
#     """
    
    
#     if user == "s" and computer == "p":
#         return "You win"
#     elif user == "p" and computer == "r":
#         return "You win"
#     elif user == "r" and computer == "s":
#         return "You win"
#     elif user == computer:
#         return "It's a tie"
#     else:
#         return "You lose"

# print("Welcome to the rock paper scissors game")
# print("Enter R for Rock, S for Scissors and P for Paper")

# user = input("> ").lower()
# options = "rps"
# computer = random.choice(options)

# if user in options:
#     print(play_game(user, computer))
# else:
#     print("Invalid input")

# print(computer)





first_data = [2,3,4,5,6,7,5,3]
second = [4,5,6,9,8]


# zipped = zip(first_data, second)

# print(list(zipped))


# print(list(enumerate(first_data)))

# arr = [50000, 43546, 675758,4353,5636]

# pay_raise = list(map(lambda x: x + (x*0.1), arr))

# print(pay_raise)

# print("Enter numbers separate them by comma")
# str_num = input(">").split(",")
# mapped = list(map(int, str_num))
# print(sum(mapped)/len(mapped))


# a = range(1, 10)


# odd = list(filter(lambda x: x % 2==0, a))
# print(odd)


#### SETS


my_set = {1,2,3,5,6,7,8,9}
my_set2 = {1,2,4,16,6,7,12}
my_set.add(100)
print(my_set)


