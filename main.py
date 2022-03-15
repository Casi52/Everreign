import day
import data as d

while d.p.health > 0: 
  day.day()
  if d.p.health > d.p.maxHP:
    d.p.health = d.p.maxHP