import time, os, random

rNumbers = []
card = [[0,0,0],[20," BINGO!",0],[10,0,11]]

# create a list of 8 random numbers from 1-99
for i in range(0,99):
  newNumber = random.randint(1,99)
  # print(newNumber)
  if newNumber not in rNumbers:
    rNumbers.append(newNumber)
  if len(rNumbers) == 8:
    break

# print random numbers list
print()
print("rNumbers:",rNumbers)
print()

# iterate over rNumbers to find lowest value
# add that to the ordered list oNumbers and remove it from rNumbers. The outer loop repeats that until rNumbers is empty.
currentNumber = 100
oNumbers = []
cardPos = 0
while len(rNumbers) > 0:
  for j in rNumbers:
    # print("j:",j)
    # time.sleep(1)
    if j < currentNumber:
      currentNumber = j
      # print("currentNumber:",currentNumber)
     # time.sleep(1)
  oNumbers.append(currentNumber)
  # print("oNumbers;",oNumbers)
  rNumbers.remove(currentNumber)
  # print("rNumbers:",rNumbers)
  cardPos+=1
  currentNumber = 101
  # print("New j loop")
  # time.sleep(1)

# now insert our numbers is ascending order into the correct positions in the bingo card
card[0][0] = oNumbers[0]
card[0][1] = oNumbers[1]
card[0][2] = oNumbers[2]
card[1][0] = oNumbers[3]
card[1][2] = oNumbers[4]
card[2][0] = oNumbers[5]
card[2][1] = oNumbers[6]
card[2][2] = oNumbers[7]

def goBingo():
  print()
  print(f"{card[0][0]:<5} | {card[0][1]:^7} | {card[0][2]:>4}")
  print("-----------------------")
  print(f"{card[1][0]:<5} | {card[1][1]:^6} | {card[1][2]:>4}")
  print("-----------------------")
  print(f"{card[2][0]:<5} | {card[2][1]:^7} | {card[2][2]:>4}")
  print()

xCount = 0
print("Teach your gran to suck eggs Bingo!")
time.sleep(1)
while True:
  time.sleep(0.5)
  os.system("clear")
  time.sleep(0.5)
  goBingo()
  while True:
    try:
      nextNumber = int(input("The next number called is: "))
      break
    except ValueError: 
      print("That's not a bingo number!")
  for i, row in enumerate(card):
    for j, yourNumber in enumerate(row):
      if yourNumber == nextNumber:
          time.sleep(0.5)
          print()
          print(f"I have {nextNumber}!")
          # print(list(enumerate(row)))
          # print(yourNumber)
          card[i][j] = "X"
          xCount +=1
          # print(xCount)
  if xCount == 8:
    break

time.sleep(1)
goBingo()
print("Bingo! Congratulations!")          