import os, time

health = 100
sword = False
chemicalexplosive = False
flamethrower = False

def startGame():
  os.system('clear') 
  print("Greetings Carolina Day School student. There has been a new variant of coronavirus and two people have been infected. They are now zombies. They are outside the school and are after you. It's your job to gather resources and defend yourself against them")
  print()
  print()
  print("Go check the classrooms!")
  time.sleep(5) 
  Hallway() 

def Hallway():
  global sword 
  os.system('clear')
  if not sword:
    print("You hear a banging noise in the front door which room do you want to go to first? The Chemistry Room, History Room, or Auditorium?")
    decision = input(">>").strip().lower()
    if "chemistry" in decision:
      Chemistryroom()
    elif "history" in decision:
      Historyroom()
    elif "auditorium" in decision:
      Auditorium()
    else:
      print("Sorry, that command is not found.")
      time.sleep(3)
      Hallway()

def Auditorium():
    os.system('clear')
    print("You're in the auditorium and you see swords from the stage combat class. You also see boxing gloves. Which one would you like to the equip?")
    decision = input(">>").strip().lower()
    if "sword" in decision:
        print("You grabbed the sword")
    elif "boxing gloves" in decision:
        print("You grabbed the boxing gloves")
    else:
        print("You didn't grab anything")
    
  
    print ("Oh No! There's two zombies behind you! Will you fight them with your weapon or will you run?")
    decision = input(">>").strip().lower()

    if "fight" in decision:
        print("The zombies killed you!")
    elif "run" in decision:
        print("The zombies caught up to you and you died!")
   
    

def Historyroom():
  global explosives, health
  os.system('clear')
  print("The zombies were in this room and took you down. You died")
  
def Chemistryroom():
  global explosives, health
  os.system('clear')
  print("Welcome to the Chemistry room")
  os.system('clear')
  print("You are in the chemistry room there are is a bag of Mercury (II) Fulminate which when thrown can blow up a whole room. There is also a flamethrower. Which one would you like to equip?")
  decision = input(">>").strip().lower()
  if "mercury" in decision:
    

    print("You grabbed the bag of Mercury (II) Fulminate")
  elif "flamethrower" in decision:
    print("You grabbed the flamethrower")
  else:
    print("You didn't grab anything")

  print()

  print("Oh No! There's two zombies behind you! Will you fight them with your weapon or will you run?")
  
  decision = input(">>").strip().lower()
  os.system('clear')
  if "fight" in decision:
    print("You successfully blew the zombies and survived")
  elif "run" in decision:
    print("You have succesfully escaped the zombies and trapped them in the room")

def endGame():
  os.system("clear")
  print("Story Over!")
  exit()

startGame()
print()
print()
print("STORY OVER")