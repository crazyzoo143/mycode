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
      break

  elif answer == "b":
      print("no but I’d go to that zoo")
      break

  elif answer == "c":
      print("yea that me")
      break

  elif answer == "d":
      print("no and idk if I want to run into that")
      break

  else:
      print("You must pick A, B, C, or D!")
