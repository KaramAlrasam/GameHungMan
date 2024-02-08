doll=['''
    +---+
    |   |
        |
        |
        |
        |
  =========''', '''
    +---+
    |   |
    O   |
        |
        |
        |
  =========''', '''
    +---+
    |   |
    O   |
    |   |
        |
        |
  =========''', '''
    +---+
    |   |
    O   |
   /|   |
        |
        |
  =========''', '''
    +---+
    |   |
    O   |
   /|\  |
        |
        |
  =========''', '''
    +---+
    |   |
    O   |
   /|\  |
   /    |
        |
  =========''', '''
    +---+
    |   |
    O   |
   /|\  |
   / \  |
        |
  =========''']
import random
words=["lion","cat","dog","tiger","bee"]
computer_choice= random.choice(words)
mysterious_word=list(len(computer_choice)*"_")
print(doll[0])
wrong_letters=[]
tries=6
while "_" in mysterious_word and tries>0:
  print(" ".join(mysterious_word))
  print(f"\nYou have only {tries} tries.")
  user= input("\nEnter the right letter:  ").strip().lower()
  if user in computer_choice:
    for index in range(0,len(computer_choice)):
      if computer_choice[index]==user:
        mysterious_word[index]=user
  elif user not in computer_choice and user in wrong_letters:
    print("You've tried this letter!!!")
  else :
    tries-=1
    print(doll[6-tries])
    wrong_letters.append(user)
if " ".join(computer_choice)== " ".join(mysterious_word):
  length=int(len("( ͡^ ͜ʖ ͡^ ) You win ( ͡^ ͜ʖ ͡^ )"))
  print(" ".join(mysterious_word))
  print("#"*length)
  print("( ͡^ ͜ʖ ͡^ ) You win ( ͡^ ͜ʖ ͡^ )")
  print("#"*length)
else:
  print("( ͡ಥ ͜ʖ ͡ಥ ) You lost ( ͡ಥ ͜ʖ ͡ಥ )")
  print(f"\nYou have only {tries} tries.")