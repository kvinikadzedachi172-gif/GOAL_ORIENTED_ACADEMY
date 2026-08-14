num=int(input("enter youre num"))
if num>=0:
    print("დადებითი რიცხვია")
elif num<=0:
    print("უარყოფითი რიცხვია")
else:
    print("ნულის ტოლია")

age=int(input("enteryoure age"))
if age<=18:
    print("არასრულწლოვანია")
elif age>=18:
    print("სრულწლოვანია")
else:
    print("პენსიონერი")

point=int(input("enter point"))    
if point==90-100:
    print("a")
elif point==80-89:
    print("b")
elif point==70-79:
    print("c")   
elif point==60-69:
    print("d")
else:
    ("f")    