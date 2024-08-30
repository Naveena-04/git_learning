import random
rock = '''
    _______
---'   ____)
      (_____)
      (_____)
      (____)
---.__(___)
'''

paper = '''
    _______
---'   ____)____
          ______)
          _______)
         _______)
---.__________)
'''

scissors = '''
    _______
---'   ____)____
          ______)
       __________)
      (____)
---.__(___)'
'''
image=[rock,paper,scissors]
choice=int(input("what do you choose? type 0 for rock, 1 for paper,2 for scissors\n"))
print(image[choice])
ch=random.randint(0,2)
print("computer choose ")
print(image[ch])
if choice>=3 and choice<0:
    print("you typed invalid number so you lose :(")
elif choice==0 and ch==2: # rock and scissors
    print("you win !")
elif ch==0 and choice==2:# rock of comp and man has scissors
    print("you lose")
elif choice>ch: # 2>1,2>0,1>0 is scissors >paper,rock  paper>rock
    print("you win!")
elif ch>choice: #2>1,2>0,1>0
    print("you lose")
elif ch==choice: #if both same
    print("it is draw")
