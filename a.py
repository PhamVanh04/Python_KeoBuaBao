from random import randint
print("Nhap Dam,La Keo:")
player = input()
computer = randint (0,2)

if computer == 0:
	computer= "Dam"
if computer == 1:
	computer = "La"
if computer == 2:
	computer = "Keo"

print("----")
print("You choose: "+ player)
print("computer chooses: "+ computer)

if player==computer:
	print("Draw")
else:
	if player == "Keo":
		if computer =="La":
			print("Win")
		else:
			print("Lose")

	if player == "Dam":
		if computer =="Keo":
			print("Win")
		else:
			print("Lose")

	if player == "La":
		if computer =="Dam":
			print("Win")
		else:
			print("Lose")
