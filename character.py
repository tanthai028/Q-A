import time, sys, os

# Defines person's age & name
class person():
  def __init__(self):
    self.name = ''
    self.age = 0

your = person()

# Ask for name
def name(questionName):
  
  inputName = ''
  while not inputName.isalpha():
    for x in questionName:
      sys.stdout.write(x)
      sys.stdout.flush()
      time.sleep(.03)

    inputName = input("> ")
    if not inputName.isalpha():
      os.system('clear')
      print("Invalid Input\n")
    
    your.name = inputName
  
# Ask for how old
def age(questionAge):
  inputAge = ''
  while not inputAge.isdigit():
    for x in questionAge:
      sys.stdout.write(x)
      sys.stdout.flush()
      time.sleep(.03)
    
    inputAge = input("> ")
    if not inputAge.isdigit():
      os.system('clear')
      print("Invalid Input\n")
    
    your.age = inputAge
    
# Baby / Child / Teenager / Adult / Old according age input
def old():
  your.age = int(your.age)
  if your.age < 1:
    os.system('clear')
    print('Invalid Age\n')
    age("How old are you %s?\n" % your.name.capitalize() )

  elif your.age == 1:
    baby = your.name.capitalize() + ', you are a baby.\n\n'
    
    for character in baby:
      sys.stdout.write(character)
      sys.stdout.flush()
      time.sleep(0.03)

  elif 1 <= your.age < 13:
    child = your.name.capitalize() + ', you are a child.\n\n'
    
    for character in child:
      sys.stdout.write(character)
      sys.stdout.flush()
      time.sleep(0.03)

  elif 12 < your.age < 18:
    teenager = your.name.capitalize() + ', you are a teenager.\n\n'
    
    for character in teenager:
      sys.stdout.write(character)
      sys.stdout.flush()
      time.sleep(0.03)

  elif your.age >= 18 and your.age < 60:
    adult = your.name.capitalize() + ', you are an adult.\n\n'
    
    for character in adult:
      sys.stdout.write(character)
      sys.stdout.flush()
      time.sleep(0.03)

  elif your.age >= 60:
    old = your.name.capitalize() + ', you are really old.\n\n'
    
    for character in old:
      sys.stdout.write(character)
      sys.stdout.flush()
      time.sleep(0.03)
    
  time.sleep(1)

# Confirmation about name & age
def areyousure(questionConfirm):
  inputConfirm = ''
  while inputConfirm.lower() not in ['yes','no']:
    for x in questionConfirm:
      sys.stdout.write(x)
      sys.stdout.flush()
      time.sleep(.03)
    
    inputConfirm = input("> ")
    if inputConfirm.lower() not in ['yes','no']:
      os.system('clear')
      print("Invalid Input\n")
    elif inputConfirm.lower() == "yes":
      return False
    elif inputConfirm.lower() == "no":
      return True

# Starts program
repeat = True
while repeat:
  name("Hi, what is your name?\n")
  age("How old are you %s?\n" % your.name.capitalize() )
  old()
  repeat = areyousure("So your name is %s and you are %s years old? (yes/no)\n" % (your.name.capitalize(), your.age) ) 
