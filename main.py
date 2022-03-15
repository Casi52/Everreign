import day
import data as d

while True:

  if d.dead == True:
    d.death(d.days)
    break 
  day.day()
  if d.p.health > d.p.maxHP:
    d.p.health = d.p.maxHP