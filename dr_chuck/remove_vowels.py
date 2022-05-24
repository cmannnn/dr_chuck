# remove_vowels
def disemvowel(string):
	vowel = ('a','e','i','o','u')
	y = string
	for x in y:
		if x in vowel:
			string = string.replace(x, '').lower()
	return string

#test 
print(disemvowel('This website is for losers LOL!'))