import mymodule

howMany = int(input("How many cards do you want to make?: "))
setOfCards = []

for x in range(howMany):
    setOfCards.append(mymodule.Card("Card " + str(x+1)))

for x in setOfCards:
    print(x.name + ": " + str(x.rarity))

customRare = mymodule.Card("This is a Rare Card: ", mymodule.rare[0])

#print(customRare.name + ": " + str(customRare.rarity))