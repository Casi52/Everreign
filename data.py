import random as r

#--Global variables--

days = 0
dead = False
vow = ["A","E","O","I","U","Y","a","e","o","i","u","y"]
yes = ["Yes", "yes", "Y", "y"]
no = ["No", "no", "N", "n"]
twpn = ["Stick","Sword","Staff","Bow"]
pwpn = {"Stick":2,"Sword":30,"Staff":100,"Bow":50}
titm = ["Health Potion", "Flash Bomb", "Cursed Scroll"]
pitm = {"Health Potion":15, "Flash Bomb":30, "Cursed Scroll":60}
gfeel = ["rested", "good", "energetic", "calm"]
ofeel = ["okay", "fine", "decent"]
bfeel = ["hurt", "unmotivated", "bad", "worried"]
seeds = ["Queen's Lilac","Cart Wild Rose","Woolly Sugarplum","Prairie White-Root","African Dindle","Soft Perennial Cucumber","Poke True Fern","Champion Evergreen Ivy","Poor Leatherleaf Willow","Soldier's Thin-Leaved Grapevine"]
eseeds = [None,None,None,None,None,None,None,None,None,None]
gundifir = False

#--Items/Combat--


class weapons:
  BluntAtt = ["hit"]
  BladeAtt = ["hit", "strike", "stab"]
  MagicAtt = ["cast a fireball at", "shoot lightning bolts at", "place a curse upon"]
  RangedAtt = ["shoot", "snipe", "hit"]
  lvl1pf = ["common", "uncommon", "rare"]
  lvl2pf = ["rare", "special", "epic"]
  lvl3pf = ["legendary", "mythical", "godly"]
  pfs = [lvl1pf, lvl2pf, lvl3pf]

class weapon:
  def __init__(self,name,power,attack,pf,price):
    self.name = name
    self.power = power
    self.attack = attack
    self.pf = pf
    self.price = price

stick = weapon("stick", r.randint(1,10), weapons.BluntAtt, r.sample(weapons.lvl1pf, 1)[0], 2)
sword = weapon("sword", r.randint(10,16), weapons.BladeAtt, r.sample(weapons.lvl1pf, 1)[0], 30)
staff = weapon("staff", r.randint(20,30), weapons.MagicAtt, r.sample(weapons.lvl2pf, 1)[0], 100)
bow = weapon("bow", r.randint(15,25), weapons.RangedAtt, r.sample(weapons.lvl1pf, 1)[0], 50)

wepl = [stick,sword,staff,bow]

class eweapon:
  name = stick.name
  power = stick.power
  pf = stick.pf
  attack = stick.attack
  cn = pf + " " + name

  def swap(newname, newpower, newpf, newtype):
    eweapon.name = newname
    eweapon.power = newpower
    #pf = r.sample(1,weapons.pfs[newlvl])
    eweapon.pf = newpf
    eweapon.attack = newtype
    eweapon.cn = eweapon.pf + " " + eweapon.name


class inventory:
  items = {"Hpotion": 2, "Flash bomb": 2, "Cursed scroll": 0}


def HPotion():
  print("You drank the health potion\n")
  p.health += 50
  print(p.health)
  print(p.maxHP)
  if p.health > p.maxHP:
    p.health = p.maxHP


#--Characters--


class dragon:
  name = "Smaug"
  age = 2000
  power = 1000
  health = 10000


class p:
  name = ""
  age = ""
  strength = 5
  power = strength + eweapon.power
  armor = 5
  health = 100
  maxHP = 100
  luck = 1
  agility = 20
  charisma = 30
  lvl = 1
  money = r.randint(50,250)
  choose = input("Gender (M/F): ")
  if choose == "F" or choose == "f":
    sex = "woman"
    grand = "granddaughter"
  else:
    sex = "man"
    grand = "grandson"
  

#--Encounters/Events/Functions--

def part(lst,low,high):
  i = low - 1
  p = lst[high]

  for q in range(low,high):
    if lst[q] < p:
      i += 1
      lst[i],lst[q] = lst[q],lst[i]
      
  lst[i + 1],lst[high] = lst[high],lst[i + 1] 
  return i+1

def quickSort(lst,low,high):
  if low < high:
    point = part(lst,low,high)
    quickSort(lst, low, point - 1) 
    quickSort(lst, point + 1, high)

def combat(name, power, ehealth, agility, gndfr):
  global dead

  pow = p.power
  battle = True
  crit = 1
  pturn = True
  ehp = ehealth
  print(p.health)
  PHPDisplay = int(p.health / (p.maxHP / 10) * 3)
  print(PHPDisplay)
  print("\n          " + "+" + "=" * 30 + "+")
  print("Your HP:  " + "|" + ("#" * PHPDisplay) + "|")
  print("          " + "+" + "=" * 30 + "+")

  print(ehp)
  EHPDisplay = int(ehp / (ehealth / 10)) * 3
  print(EHPDisplay)
  print("\n           " + "+" + "=" * 30 + "+")
  print(name.capitalize(), ":  " + "|" + ("#" * EHPDisplay) + "|", sep="")
  print("           " + "+" + "=" * 30 + "+")
  while p.health > 0 and ehp > 0 and battle == True:
    print("=" * 50)
    print()

    #Player and enemy HP bars

    if pturn == True:
      choices = ["Attack with " + eweapon.name, "Use item", "Attempt escape"]
      if gndfr == True:
        choices.append("Ask gundifir for help")
      for i in enumerate(choices):
        print(i[0] + 1, i[1])
      print()
      choose = input()
      if choose == "2":
        for i in enumerate(inventory.items):
          print(i[0] + 1, i[1], "| Amount:", inventory.items[i[1]])
        choose = input()
        if choose == "1":
          HPotion()
          inventory.items["Hpotion"] -= 1
        elif choose == "2":
          print("WIP")
        elif choose == "3":
          print("WIP")
        pturn == False
      elif choose == "3":
        esc = r.randint(p.agility - agility, 20)
        if esc >= 15:
          print("\nYou escaped\n")
          battle = False
        else:
          print("\nYou were hunted down and died\n")
          dead = True
      elif gndfr == True and choose == "4":
        print("Gundífir uses his magic to temporarily boost your power.")
        pturn = False
        p.power += 5
      else:
        x = r.randint(1, 10)
        if x == 10:
          crit = 1.25
        else:
          crit = 1
        dmg = (r.randint(int(p.power - (p.power / 10)),int(p.power + (p.power / 10))) * crit) + eweapon.power
        x = r.randint(agility, 10)
        if x == 10:
          print("You", r.sample(eweapon.attack, 1)[0], "the", name, "with your", eweapon.name, "but it avoids the attack!")
        else:
          print("You",
            r.sample(eweapon.attack, 1)[0], "the", name,
            "with your", eweapon.name)
          ehp -= dmg
        pturn = False
        PHPDisplay = int(p.health / 10) * 3
        print("\n          " + "+" + "=" * 30 + "+")
        print("Your HP:  " + "|" + ("#" * PHPDisplay) + "|")
        print("          " + "+" + "=" * 30 + "+")

        EHPDisplay = int(ehp / (ehealth / 10)) * 3
        print("\n           " + "+" + "=" * 30 + "+")
        print(name.capitalize(), ":  " + "|" + ("#" * EHPDisplay) + "|", sep="")
        print("           " + "+" + "=" * 30 + "+")

        input()

  else:
    x = r.randint(1, 10)
    if x == 10:
      crit = 1.25
    else:
      crit = 1
    edmg = r.randint(int(power - (power / 10)), int(power + (power / 10))) * crit
    x = r.randint(agility, 10)
    if x == 10:
      print("The", name, "tries to strike you but you avoid the attack!")
    else:
      print("The", name, "strikes you")
      p.health -= edmg
    pturn = True

    PHPDisplay = int(p.health / 10) * 3
    print("\n          " + "+" + "=" * 30 + "+")
    print("Your HP:  " + "|" + ("#" * PHPDisplay) + "|")
    print("          " + "+" + "=" * 30 + "+")

    EHPDisplay = int(ehp / (ehealth / 10)) * 3
    print("\n           " + "+" + "=" * 30 + "+")
    print(name.capitalize(), ":  " + "|" + ("#" * EHPDisplay) + "|", sep="")
    print("           " + "+" + "=" * 30 + "+")

    input()
  if ehp <= 0:
    print("You win")
    p.power = pow
  elif p.health <= 0:
    dead = True


def calm(erage, ename):
  calm = r.randint(1, p.charisma)
  if calm < erage:
    print("You tried to calm the", ename,
      "but instead you just aggrevated it.")
    return False
  if calm >= erage:
    print(
      "Using your superior charismatic skills, you successfully calm the",
      ename)
    return True


def basicEnc(name, pow, hp, agi, rage, gndfr):
  global dead

  if name[0] in vow:
    aan = "an"
  else:
    aan = "a"
  print("You encounter ", aan, " ", name, ". What will you do?", sep="")
  choices = ["Attack with your " + eweapon.cn, "Try to calm it", "Run"]
  for i in enumerate(choices):
    print(i[0] + 1, i[1])
  print()
  choose = input()
  if choose == "2":
    x = calm(rage, name)
    if x == False:
      combat(name, pow, hp, agi, gndfr)
  elif choose == "3":
    esc = r.randint(p.agility - agi, 20)
    if esc >= 15:
      print("\nYou escaped\n")
    else:
      print("\nYou were hunted down and died\n")
      dead = True
  else:
    print("You decide to attack the", name, "with your", eweapon.name, "\n")
    combat(name, pow, hp, agi, gndfr)


def rest():
  print("You rest until the next day.\n\nYour HP has been refilled\n")
  p.health = 100


def death(days):
  print("=" * 50)
  print("\nYou died\n")
  print("Your adventure lasted for", days, "days.")

def trader(money):
  print("\nBefore you a trader appears.\n")
  choose = input("- Greetings! Do you wish to buy any wares? ")
  if choose in no:
    print("\n- Good day to you then!\n")
  else:
    while True:
      choose = input("- Wonderful! Would you like to buy a weapon (w) or an item (i)? ")
      if choose == "w" or choose == "W":
        print("\nThese are the weapons I have on offer:\n")
        for i in enumerate(twpn):
          print(i[0] + 1,i[1], "| Price:", pwpn[i[1]])
        print()
        choose = input("What weapon will you buy? ")
        if p.money - pwpn[twpn[int(choose) - 1]] < 0:
          print("\nInsufficient money.\n")
          continue
        #Find better system for this:
        if choose == "1":
          eweapon.swap(stick.name, stick.power, stick.pf, stick.attack)
        elif choose == "2":
          eweapon.swap(sword.name, sword.power, sword.pf, sword.attack)
        elif choose == "3":
          eweapon.swap(staff.name, staff.power, staff.pf, staff.attack)
        elif choose == "4":
          eweapon.swap(bow.name, bow.power, bow.pf, bow.attack)
        print("\n- Thank you for your purchase!\n")
        p.money -= pwpn[twpn[int(choose) - 1]]
      elif choose == "i" or choose == "I":
        print("\nThese are the items I have on offer:\n")
        for i in enumerate(titm):
          print(i[0] + 1,i[1], "| Price:", pitm[i[1]])
        print()
        choose = input("What item will you buy? ")
        print("\n- Thank you for your purchase!\n")
        p.money -= pitm[titm[int(choose) - 1]]
      elif choose in no:
        print("\n- Good day to you then!\n")
        break

#--Enemies--

class Enemy:
  def __init__(self, name, power, health, agility, rage):
    self.name = name,
    self.power = power,
    self.health = health,
    self.agility = agility,
    self.rage = rage,

goblin = Enemy("goblin",5 * p.lvl, 50 * p.lvl, 8, 22)
orc = Enemy("orc",12 * p.lvl, 200 * p.lvl, 2, 30)
knight = Enemy("knight",20 * p.lvl, 120 * p.lvl, 5, 15)
griffin = Enemy("griffin",50 * p.lvl, 400 * p.lvl, 8, 40)
dragon = Enemy("dragon", 200, 1000, )

#--Cheat functions--

import story as s

class cheat:
  def forceStory(index):
    s.storys[index]()

  def NewWeapon(newname, newpower, newpf):
    eweapon.name = newname
    eweapon.power = newpower
    #pf = r.sample(1,weapons.pfs[newlvl])
    eweapon.pf = newpf
    eweapon.cn = eweapon.pf + " " + eweapon.name

  def inv():
    p.health = 1000000000000000000

  def stats(newName, newAge, newStrength, newArmor, newHP, newMaxHP, newLuck, newAgility, newCharisma, newLvl):
    p.name = newName
    p.age = newAge
    p.strength = newStrength
    p.power = p.strength + eweapon.power
    p.armor = newArmor
    p.health = newHP
    p.maxHP = newMaxHP
    p.luck = newLuck
    p.agility = newAgility
    p.charisma = newCharisma
    p.lvl = newLvl

