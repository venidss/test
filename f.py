score = 0
a=input("1.(K ^ B) v (L --> E \n2.~(K ^ B) \n3.~E \t/~L \nType your answer:")
r=input("What rule?:")
b=input("1.(K ^ B) v (L --> E \n2.~(K ^ B) \n3.~E \t/~L \n4.L --> E DS \nType your answer:")
e=input("What rule?")
if a =="L --> E" or "l --> e" and r == "DS" and b =="~L" and e == "MT":
	print("Correct")
	score += 1
else:
	("Incorrect")
	
print("You got a score of:",score, "out of 10")
