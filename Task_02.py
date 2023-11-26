import random
user_action=input("enter a choice(rock,paper,scissors):")
possible_actions=["rock","paper","scissors"]
computer_action=random.choice(possible_actions)
print(f"\n you chose:", (user_action), "computer chose:",(computer_action))
if user_action==computer_action:
    print("both have selected",user_action,"its a tie")
elif user_action=="rock":
    if computer_action=="scissors":
        print("rock breaks scissors, you won")
    else:
        print("paper covers rock you lose!!")
elif user_action=="paper":
    if computer_action=="scissors":
        print("scissors cut paper, you lose")
    else:
        print("paper covers rock, you won")
elif user_action=="scissors":
    if computer_action=="paper":
        print("scissors cut paper, you won")
    else:
        print("rock breaks scissors, you lose")