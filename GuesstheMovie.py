import csv
import string
import random

vocabulary = []

# import requests

# url = 'https://wordgenerator-api.herokuapp.com/api/v1/resources/words'

# params = dict(
#     lang='IT',
#     amount='10'
# )

with open('netflix_titles.csv', newline='') as csvfile:
	reader = csv.DictReader(csvfile)
	for row in reader:
		countries = row['country'].split(',')
		if 'Italy' in countries:
			vocabulary.append(row['title'].lower())

	# vocabulary = [ row['title'].lower for row in reader if 'Italy' in row['countries'].split(',')]

# print(vocabulary)

guessed = ""
letters = [] 
attempts = 5

random.seed(a=0)
# a = 0  -> Geronimo Stilton
# a = 61 -> Suburra
# a = 9  -> Sacro GRA

word = vocabulary[random.randrange(len(vocabulary))]
# print(word)

def init_guessed(word):
	w = ""
	for l in word:
		if l.isspace() or l in string.punctuation:
			w += l
		else: 
			w += "-"
	return w

def find_occurrencies(l, w):
	res = []
	for i in range(0, len(w)):
		if l == w[i]:
			res.append(i)

	return res

def check_letter(letter, letters):
	found = False
	for i in letters:
		if i.lower() == letter.lower():
			found = True
			break

	return found

def sub_letter(choice, pos, word):
	l = list(word)
	l[pos] = choice
	return "".join(l)

guessed = init_guessed(word)

game = True

while game:

	print("Benvenuto!\nIl film misterioso è:", guessed)
	print("Hai ancora {} tentativi \n".format(attempts))

	choice = input("Qual è il film?\n")

	if choice == word:
		game = False
		print("Bravissimo, hai indovinato!")
	else:
		print("\n----------ERRORE!!-----------")
		print("Sbagliato! Estrai una lettera:")
		choice = input("Quale lettera vuoi estrarre? premi 0 per uscire\n")

		choice = choice.lower()

		if choice == "0":
			game = False
			print("Il titolo da indovinare era {}".format(word))
			print("Bye!")

		else:
			if check_letter(choice, letters):
				print("Lettera già scelta!")
			else:
				letters.append(choice)
				if choice in set(word):
					for pos in find_occurrencies(choice, word):
						guessed = sub_letter(choice, pos, guessed)
				else:
					attempts -= 1
					if attempts > 0:
						print("AHI AHI AHI! Ti mancano solo {} tentativi...".format(attempts))
					else:
						print("Hai perso! Il film era {}".format(word))
						game = False

		print
