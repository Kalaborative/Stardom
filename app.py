from flask import Flask, render_template
from random import choice


app = Flask(__name__)

discord_list = ["Fargas", "localhater", "L.", "nekopara", "Papa Bill", "Zeckar", "Soap", "Rampo", "Marcos", "Popo"]
animals = ["deer.gif", "dog_1.gif", "dog_2.gif", "elephant.gif", "fox.gif", "koala.gif", "lion.gif", "monkey.gif", "moose.gif", "pig.gif", "raccoon.gif", "squirrel.gif"]
indexed = []
animaled = []

for d in discord_list:
	animaled.append([d, choice(animals)])


for a in enumerate(animaled):
	indexed.append(a)

numAnimals = [(i[0], i[1][0], i[1][1]) for i in indexed]

@app.route('/')
def index():
	return render_template('index.html', users=numAnimals)

if __name__ == "__main__":
	app.run(debug=True)