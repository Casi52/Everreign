import data as d
import random as r

def story1():
  print("As you open your eyes on the first day on your great journey, you are greeted by an old man.\n")
  print("- Hello, weary traveller. Excuse my intruding, but I had to speak to you. I hear of many people who travel here to kill the infamous dragon, but few survive. Maybe i can offer you some advice to increase your chances of surviving or even defeating the dragon.\n")
  print("- Remember to always carry health potions, these are the key to your survival. There are many traders in the region who are willing to sell these to you. In fact, here, have two of mine.\n")
  print("- And also, remember that you will not be a high value target for enemies until you increase your health, so you most likely do not need to worry about encountering, for example, an orc early on.\n")
  print("- Lastly, remember that not giving an answer defaults to a yes in most situations, or the first alternative. This is a custom of this region.\n")
  print("- Good luck on your journey, adventurer.\n")
  input()
  print("\nThe old man turned and walked away, vanishing between the trees.")

def story2():
  print("You encounter an old lady.\n")
  print("- Hello my dear ", d.p.grand, ". It's been a long time since we last saw each other.\n", sep = "")
  if d.p.money < 100:
    print("- I can see that you did not inherit a lot of money from your parents. Let grandma help.")
    print()
    choose = input("Accept grandma´s help? (y/n) ")
    print()
    if choose in d.no:
      print("You are so humble and considerate, my dear ", d.p.grand, ".", sep = "")
    else:
       d.p.money += 100
  elif d.p.money >= 100:
    print("- I can see that you inherited a lot of money from your parents. Would you mind helping your grandma out?.\n")
    choose = input("Give your grandma some money? (y/n) ")
    if choose in d.no:
      print("\n- Fine, you were never my favorite anyway.")
    else:
      d.p.money -= 50
      print("\n- Thank you dear!") 

def story3():
  print("As you walked in the woods you suddenly hear a screech closeby.\n")
  choose = input("Rush to help? (y/n)")
  print()
  if choose in d.no:
    pass
  else:
    print("As you rush to the scene you see a group of bandits robbing a goblin.\n")
    choose = input("Defend the goblin? (y/n) ")
    if choose in d.no:
      print("As you turn around the goblins screams for help are interrupted by the sound of a stab. You quickly left the scene.+")
    else:
      print("lol")

def story4():
  print("A strange elf hopped down from a tree above you.\n")
  choose = input("- Hello, I am Gundífir, the elven mage. I have been sent by the committe of the tree elves to assist you in your journey to kill the dragon tyrant. Will you accept my help? (y/n) ")
  if choose in d.no:
    print("\nThis will be saddening news for the council, they thought you were a", d.p.sex, "of reason.")
    pass
  else:
    print("\n- I shall be joining you in your battles, just tell me if you need my help.\n")
    print("-"*50)
    print("New combat function: Ask gundífir for help")
    print("-"*50)
    d.gundifir = True
  
def story5():
  print("You arrive in front of a large cave. For some reason, although there is bright daylight outside, the cave remains completely dark right from the entrance. There is a sign next to the entrance. Most text is scratched out, but some is readable:\n\n- Traveler, do not ... the cave of the ... beware of him, for he does not ... other ... never. Not a single ... from the cave. \n")
  choose = input("Will you enter the cave? (y/n)")
  print()
  if choose in d.no:
    print("You are easily frightened and thus obeyed what little the sign said and walked away.")
  else:
    input("\nYou take no heed to the readable parts of the sign and continue into the cave.")
    input("\nAs you step inside, ")

def story6():
  print("\nYou encounter an old lady who is picking up seeds from the ground. She is visibly upset.\n\n- Will you help me?\n")
  choose = input("Help the old lady? (y/n)")
  if choose in d.no:
    print("\nBeing the horrible, socially incompetent human being that you are, you quietly pass by.\n")
  else:
    print("- Thank you dear! I will read the list of seeds and you only need to place them in alphabetic order. Easy!\n")
    choose = input("Ready? (y/n)")
    if choose in d.no:
      input("Tough luck, let's go.")
    else:
      print("Wonderful, let us begin.")
    input("- These are the seeds:\n Queen's Lilac,\n Cart Wild Rose,\n Woolly Sugarplum,\n Prairie White-Root,\n African Dindle,\n Soft Perennial Cucumber,\n Poke True Fern,\n Champion Evergreen Ivy,\n Poor Leatherleaf Willow Bark,\n Soldier's Thin-Leaved Grapevine")
    print()
    facit = list(d.seeds)
    d.quickSort(facit, 0, len(facit)-1)
    pseeds = list(d.seeds)
    chosen = list()
    x = 0
    while x < 10:
      try:
        s = r.sample(pseeds, 1)[0]
        print("\n- Ok, the ", s, ".", sep = "")
        string = str("At what place in the list should the " + s + " be? (1-10)")
        choose = int(input(string))
        if choose in chosen:
          print("You obviously can't put two seeds in the same place idiot.")
        else:
          chosen.append(choose)
          d.eseeds[choose - 1] = s
          pseeds.remove(s)
          x += 1
      except:
        print("What? You managed to write a number wrong? This is embarrasing.")
    print("\n- This is how you sorted the seeds:\n")
    for i in enumerate(d.eseeds):
      print(i[0], i[1])
    print("\n- And this is how they are supposed to be sorted:\n")
    print(facit)
    for i in enumerate(facit):
      print(i[0], i[1])
    if d.eseeds == facit:
      input("Well done.")
      print()
      input("- Did you expect a reward? Haha, don't be stupid. Goodbye!")
    else:
      input("How could you possible fail this bad. I am ashamed to be in your presance. Begone!")
    
      
      
      
storys = [story1,story2,story3,story4,story5,story6]