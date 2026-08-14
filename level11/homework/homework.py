#1) შექმენი ცვლადი balance = 1000.
#მომხმარებელს შეაყვანინე თანხა.
#თუ თანხა დადებითია, შიგნით შეამოწმე ბალანსზე მეტია თუ არა.
#- თუ არა, დაბეჭდე "თანხა წარმატებით გაიტანეთ"
#- თუ მეტია, დაბეჭდე "არასაკმარისი ბალანსი"
#თუ თანხა 0 ან უარყოფითია, დაბეჭდე "არასწორი თანხა"

#2) მომხმარებელს შეაყვანინე გამოცდის ქულა.
#თუ ქულა 50 ან მეტია, შიგნით შეამოწმე 90 ან მეტია თუ არა.
#3- თუ არის, დაბეჭდე "A"
#- თუ არა, დაბეჭდე "ჩააბარა"
#თუ ქულა 50-ზე ნაკლებია, დაბეჭდე "ჩაიჭრა"

#3) მომხმარებელს შეაყვანინე ტემპერატურა.
#თუ ტემპერატურა 0-ზე მეტია, შიგნით შეამოწმე 30-ზე მეტია თუ არა.
#- თუ არის, დაბეჭდე "ცხელა"
#- თუ არა, დაბეჭდე "თბილა"
#თუ ტემპერატურა 0 ან ნაკლებია, დაბეჭდე "ცივა" 

#4) მომხმარებელს შეაყვანინე წელი.
#თუ წელი 2000-ზე მეტია, შიგნით შეამოწმე ლუწია თუ კენტი.
#- თუ ლუწია, დაბეჭდე "ლუწი წელია"
#- თუ კენტია, დაბეჭდე "კენტი წელია"
#თუ წელი 2000-ზე ნაკლები ან ტოლია, დაბეჭდე "ძველი წელია"

#5) მომხმარებელს შეაყვანინე პროდუქტის რაოდენობა.
#თუ რაოდენობა 0-ზე მეტია, შიგნით შეამოწმე 10-ზე მეტია თუ არა.
#- თუ არის, დაბეჭდე "მარაგი საკმარისია"
#- თუ არა, დაბეჭდე "მარაგი ცოტაა"
#თუ რაოდენობა 0-ია, დაბეჭდე "მარაგი არ არის"


balence=1000
amount=int(input("enter youre amount:"))
if amount<balence:
    if amount>balence:
        print("The amount was successfully transferred")
    else:
        print("Incorrect amount")
        print("Insufficient balance")
else:
    print("incorrect amount")

point=int(input("enter youre point:"))    
if point>=90:
    if point>=50:
        print("passed") 
    else:
        print("ჩაიჭრა")
        print("A")
else:
    print("ჩაიჭრა")

temperture=int(input(":enter temperture"))
if temperture>=30:
    if temperture<30:
        print("თბილია")
    else:
        print("ცივა")
        print("ცხელა")
else:
    print("ცივა")

year=int(input("enter year:"))
if year>2000:
    if year==2%0:
        print("even year")
    else:
        print("old year")

        print("kent year")
else:
    print("old year")

product=int(input("enter product quanity:"))
if product>0:
    if product>10:
        print("მარაგი ცოტაა")
    else:
        print("მარაგი არ არის")

        print("მარაგი საკმარისია")
else:
    print("მარაგი არ არის")