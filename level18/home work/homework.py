#1. Nested for loop-ის გამოყენებით დაბეჭდეთ 3x3 ვარსკვლავების კვადრატი.

#2. Nested while loop-ის გამოყენებით დაბეჭდეთ 4 სტრიქონი, თითოეულში 5 ვარსკვლავით.

#3. Nested for loop-ის გამოყენებით დაბეჭდეთ ყველა შესაძლო წყვილი 1-დან 3-მდე რიცხვებით.

#4. Nested while loop-ის გამოყენებით დაბეჭდეთ 1-დან 5-მდე რიცხვების გამრავლების ტაბულა.

#5. Nested for loop-ის გამოყენებით შექმენით ვარსკვლავების სამკუთხედი.

#6. Nested while loop-ის გამოყენებით შექმენით რიცხვების სამკუთხედი 1-დან 5-მდე.

#7. Nested for loop-ის გამოყენებით შექმენით 5x5 კვადრატი, მაგრამ მესამე ვარსკვლავი არ დაბეჭდოთ. გამოიყენეთ continue.

#8. მომხმარებელს შემოატანინეთ ორი რიცხვი და Nested while loop-ის გამოყენებით შექმენით ვარსკვლავების მართკუთხედი, სადაც პირველი რიცხვი იქნება სტრიქონების რაოდენობა, ხოლო მეორე — თითოეულ სტრიქონში ვარსკვლავების რაოდენობა.

for i in range(3):
    for j in range(3):
        print("*",end="")
    print()

for i in range(5):
    for j in range(4):
        print("*",end="")
    print()

for i in range(1,4):
    for j in range(1,4):
        print(i,j)

i=1
while i<=4:
   print(i)
j=1
while j<=4   



for i in range(0,10):
    for j in range(0,10-i):
         print(" ",end="")
    for k in range(0 ,2*i + 1):
      print("*",end="")
    print("")

i=1
while i<=5:
     
 j=5
 while j<=4:
     print(i,end="")

     j +=1 

 print()
i+=1
 