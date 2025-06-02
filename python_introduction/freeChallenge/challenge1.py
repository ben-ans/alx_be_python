# import random
# secret_number = 7
# guess = int(input("Guess a number to win: "))

# match guess:
#     case 4:
#         print("Congratulation you gussed it, You  have won 10,000 dollars")

#     case _:
#         print("Opps you didnt guess right, you loss")
        

row = 5
i=1
# star = "*"
while i <= row:
    # printing Space
    space = row-i
    star = 2*i - 1
    print(" " * space, "*" * star)
    i+=1
    
    
    
    