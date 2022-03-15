print("="*50)
import data as d
import random as r
import story as s
print("="*50)
choose = input("Play tutorial (y/n): ")
if choose in d.no:
  d.days = 1
else:
  pass
  
def day():
  print("=" * 50)
  print()
  if d.p.health > 75:
    print("You wake up feeling ", r.sample(d.gfeel,1)[0],".", sep = "")
  if 75 >= d.p.health >= 25:
    print("You wake up feeling ", r.sample(d.ofeel,1)[0],".", sep = "")
  if d.p.health < 25:
    print("You wake up feeling ", r.sample(d.bfeel,1)[0],".", sep = "")
  print()
  print("Day", d.days)
  print()
  print("Money:", d.p.money)
  print()
  print("HP:", d.p.health)
  print()

  if d.days % 5 != 0:
    end_day = False
    while end_day == False:
      print("=" * 50)
      print()
      print("What do you want to do?\n")
      choices = ["Explore", "Rest", "Check inventory"]
      for i in enumerate(choices):
        print(i[0] + 1, i[1])
      print()
      choose = input()
      print("\n", "=" * 50, "\n", sep = "")
  
      print(choose)
  
      if choose == "test":        
        d.trader(d.p.money)

      elif choose == "story":
        d.cheat.forceStory(int(input()))
  
      elif choose == "2":
        print()
        d.rest()
        end_day = True
  
      elif choose == "cheat":
        choices = ["WeaponSwap", "Invulnerability", "Stats"]
        for i in enumerate(choices):
          print(i[0] + 1, i[1])
        print()
        choose = input()
        if choose == "1":
          d.cheat.NewWeapon(input("Name: "), input("Power: "), input("Prefix: "))
        elif choose == "2":
          d.cheat.inv()
        elif choose == "3":
          try:
            d.cheat.stats(
                input("Name: "),
                int(input("Age: ")),
                int(input("Strength: ")),
                int(input("Armor: ")),
                int(input("HP: ")),
                int(input("Max HP: ")),
                int(input("Luck: ")),
                int(input("Agility: ")),
                int(input("Charisma: ")),
                int(input("Lvl: "))
              )
          except:
            print("Error")
        end_day = True
            
      elif choose == "3":
        print("In your bag you find:\n")
        for item in d.inventory.items:
          print("Item: ", item, " | Amount: ", d.inventory.items[item], sep = "")
        print()

      else:
        #x = r.randint(1,[number of types of encounters])
        x = r.randint(1,2)
        if x == 1:
  
          #Combat
  
          #x = r.randint(1,[amount of enemies])
          x = r.randint(1,4)
          if x == 1:
            d.basicEnc(d.goblin.name[0],d.goblin.power[0],d.goblin.health[0],d.goblin.agility[0],d.goblin.rage[0], d.gundifir)
          if x == 2:
            d.basicEnc(d.orc.name[0],d.orc.power[0],d.orc.health[0],d.orc.agility[0],d.orc.rage[0], d.gundifir)
          if x == 3:
            d.basicEnc(d.knight.name[0],d.knight.power[0],d.knight.health[0],d.knight.agility[0],d.knight.rage[0], d.gundifir)
          if x == 4:
            d.basicEnc(d.griffin.name[0],d.griffin.power[0],d.griffin.health[0],d.griffin.agility[0],d.griffin.rage[0], d.gundifir)
        
        elif x == 2:
  
          #Trader
  
          d.trader(d.p.money)
        end_day = True
  else:
    print("=" * 50)
    s.storys[d.days // 5]()

  d.days += 1


