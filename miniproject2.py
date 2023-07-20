# Goal: how well do you know you cohort member Maria
# Two guesses per question
# Two wrong you get pushed to next question

gamerounds= 0

while True:
  gamerounds += 1
  print("Question 1: What is Maria’s online name, \na) crazyfox431, \nb) foxzoo143, \nc) crazyzoo143 \nd) crazyfox431")
  answer= input(">")
  answer= answer.lower().strip()

  if answer == "a":
      print("no I do not know that person")

  elif answer == "b":
      print("no but I’d go to that zoo")

  elif answer == "c":
      print("yea that me")
      break

  elif answer == "d":
      print("no and idk if I want to run into that")

  else:
      print("You must pick A, B, C, or D!")

while True:
  gamerounds += 1
  print("Question 2:Which one of these does Maria want to do? \na) Go in a shark cage, \nb) Skydiving \nc) Run with bulls, \nd) Bungee jumping")
  answer= input(">")
  answer= answer.lower().strip()

  if answer == "a":
      print("You are correct! but everyone else is to afraid")
      break

  elif answer == "b":
      print("NO!!! if I am afraid of planes why would I jump out of one")

  elif answer == "c":
      print("NO! I do not run I will die")

  elif answer == "d":
      print("........no...... let me tell you something......")

  else:
      print("You must pick A, B, C, or D!")

while True:
  gamerounds += 1
  print("Question 3: What is Maria NOT allergic too? \na) Chocolate, \nb) The devil's lettuce, \nc) Mangos, \nd) Carrots")
  answer= input(">")
  answer= answer.lower().strip()

  if answer == "a":
      print("WRONG I am allergic but I eat it anyway")

  elif answer == "b":
      print("Wrong I am allergic to everyone's favorite plant")

  elif answer == "c":
      print("CORRECT, I am not allergic I just do not like them")
      break

  elif answer == "d":
      print("WRONGGGGGGGGGGGGGGGGGGGGGGGGG")

  else:
      print("You must pick A, B, C, or D!")

while True:
  gamerounds += 1  
  print("Question 4:What is Maria's Favorite type of food? \na) Japanese \nb) Greek \nc) Italian \nd) Polish")
  answer= input(">")
  answer= answer.lower().strip()

  if answer == "a":
      print("Incorrect WOW YOU JUST THINK I AM A WEEB HUHHHHHHHHH")

  elif answer == "b":
      print("YOU ARE CORRECT I LOVE GREEK FOOD")
      break

  elif answer == "c":
      print("Incorrect, just because I am half Italian doesn't mean it has to be my favorite")

  elif answer == "d":
      print("Incorrect, wow so because I am half Polish it has to be my favorite")

  else:
      print("You must pick A, B, C, or D!")
