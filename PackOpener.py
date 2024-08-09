import mymodule


howMany = 10
setOfCards = []

for x in range(howMany):
    setOfCards.append(mymodule.Card("Card " + str(x)))

for x in setOfCards:
    print(x.name + ": " + str(x.rarity))

customRare = mymodule.Card("This is a Rare Card: ", mymodule.rare[0])

print(customRare.name + ": " + str(customRare.rarity))