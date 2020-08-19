import time, random, cmd, textwrap, os, sys


class character:
  def __init__(self):
    self.name = ''
    self.age = 0
myCharacter = character()

# Introduction
def start():
  os.system('clear')
  question1()
  
def question1(): 
  question1 = "Hi, what's your name?\n"
  for character in question1:
    sys.stdout.write(character)
    sys.stdout.flush()
    time.sleep(0.03)
  character_name = input('> ')
  myCharacter.name = character_name
  confirmation1 = "Your name is " + myCharacter.name + "?" + " (Y/N)\n"
  for character in confirmation1:
    sys.stdout.write(character)
    sys.stdout.flush()
    time.sleep(0.03)
  c1 = input("> ")
  if c1.lower() == "y":
    question2()
  while c1.lower() == "n" or c1.lower() not in ["y", "n"]:
    os.system('clear')
    for character in question1:
      sys.stdout.write(character)
      sys.stdout.flush()
      time.sleep(0.03)
    character_name = input('>')
    myCharacter.name = character_name
    confirmation1 = "Your name is " + myCharacter.name + "?" + " (Y/N)\n"
    for character in confirmation1:
      sys.stdout.write(character)
      sys.stdout.flush()
      time.sleep(0.03)
    c1 = input(">")
    if c1.lower() == "y":
      question2()





def question2():
  question2 = "Hi " + myCharacter.name + ", how old are you?\n"
  for character in question2:
    sys.stdout.write(character)
    sys.stdout.flush()
    time.sleep(0.03)
  character_age = int(input('> '))
  myCharacter.age = character_age
  if character_age < 0:
    print('Invalid Age\n')
    character_age = int(input('> '))
  elif character_age <= 1:
    baby = myCharacter.name + ', you are a baby\n'
    for character in baby:
      sys.stdout.write(character)
      sys.stdout.flush()
      time.sleep(0.03)
  elif character_age < 13:
    child = myCharacter.name + ', you are a child\n'
    for character in child:
      sys.stdout.write(character)
      sys.stdout.flush()
      time.sleep(0.03)
  elif character_age < 18:
    teenager = myCharacter.name + ', you are a teenager\n'
    for character in teenager:
      sys.stdout.write(character)
      sys.stdout.flush()
      time.sleep(0.03)
  elif character_age >= 21:
    adult = myCharacter.name + ', you are an adult\n'
    for character in adult:
      sys.stdout.write(character)
      sys.stdout.flush()
      time.sleep(0.03)
  elif character_age > 60:
    old = myCharacter.name + ', you are really old\n'
    for character in old:
      sys.stdout.write(character)
      sys.stdout.flush()
      time.sleep(0.03)
  summary()

def summary():
  time.sleep(1)
  confirmation2 = ("\nSo your name is " + myCharacter.name + " and you are " + str(myCharacter.age) + " years old?" + " (Y/N)\n")
  for character in confirmation2:
    sys.stdout.write(character)
    sys.stdout.flush()
    time.sleep(0.03)
  
  c2 = input("> ")
  if c2.lower() == "y":
    sys.exit()
  else:
    start()


start()

