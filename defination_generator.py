import json
from difflib import get_close_matches
data =json.load(open('data.json'))

def defination(word):

	word = word.lower()

	if word in data:
		return data[word]
	elif word.title() in data: #if user entered "delhi" this will check for "Delhi" as well.
	    return data[word.title()]
	elif word.upper() in data: #in case user enters words like USA or NATO
	    return data[word.upper()]
	elif len(get_close_matches(word, data.keys())) > 0:
		yn = input(f'Did you mean {get_close_matches(word, data.keys())[0]} insted? Enter Y if yes or N if no.')
		if yn == 'y':
			return data[get_close_matches(word, data.keys())[0]]
		elif yn == 'n':
			return 'I don\'t understand the word. Please check again'
		else:
			return 'Wrong Input'
	else:
		return 'I don\'t understand the word. Please check again'

word = input('Enter the word')

output = defination(word)

if type(output) == list:
	for item in output:
		print(item)
else:
	print(output)