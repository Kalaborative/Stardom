from random import choice
animals = ["deer.gif", "dog_1.gif", "dog_2.gif", "elephant.gif", "fox.gif", "koala.gif", "lion.gif", "monkey.gif", "moose.gif", "pig.gif", "raccoon.gif", "squirrel.gif"]

discord_list = ["Fargas", "localhater", "L.", "nekopara", "Papa Bill", "Zeckar", "Soap", "Rampo", "Marcos", "Popo"]
indexed = []
animaled = []

for d in discord_list:
	animaled.append([d, choice(animals)])


for a in enumerate(animaled):
	indexed.append(a)

numAnimals = [(i[0], i[1][0], i[1][1]) for i in indexed]
print numAnimals[0][0] + 1