'''_____________________________________________________________________________________________'''

# Exercise 6: Rewrite your pay computation with time-and-a-half for overtime and create a function 
# called computer pay which takes two parameters
# (hours and rate).
# Enter Hours: 45
# Enter Rate: 10
# Pay: 475.0

'''def computerate(hours, rate):
	pay = 0
	if hours > 40:
		hours = hours * 1.5
	pay = hours * rate 
	return pay

hours = input('Enter Hours: ')
rate = input('Enter Rate: ')
print(computerate(float(hours), float(rate)))'''

'''_____________________________________________________________________________________________'''

# Exercise 7: Rewrite the grade program from the previous chapter using
# a function called computegrade that takes a score as its parameter and
# returns a grade as a string.

# Score Grade
# >= 0.9 A
# >= 0.8 B
# >= 0.7 C
# >= 0.6 D
# < 0.6 F


'''def computegrade(score):
	if score > 1:
		print('bad number, re-enter please')
	if score <= 1.0 and score >= .895:
		print('A')
	if score <= .894 and score >= .795:
		print('B')
	if score <= .794 and score >= .695:
		print('C')
	if score <= .694 and score >= .595:
		print('D')
	if score <= .594:
		print('Ha you Failed')
		
grade = input('Enter score:')

try:
	computegrade((float(grade)))
except:
	print('enter a number')'''

'''_____________________________________________________________________________________________'''

# Exercise 1: Write a program which repeatedly reads numbers until the
# user enters “done”. Once “done” is entered, print out the total, count,
# and average of the numbers. 
# If the user enters anything other than a
# number, detect their mistake using try and except and print an error
# message and skip to the next number.

'''total = []
while True:
	inny = input('Enter a non decimal number: ')
	if inny == 'done':
			print()
			print('List total: {}'.format(sum(total)))
			print('List count: {}'.format(len(total)))
			print('List average: {}'.format(sum(total) / len(total)))
			print()
			quit()	
	try:
		non = int(inny)
		total.append(non)
	
	except:
		print('Please enter a non-decimal number')
		continue
	print(total)
print(total)'''

'''_____________________________________________________________________________________________'''

# Exercise 2: Write another program that prompts for a list of numbers
# as above and at the end prints out both the maximum and minimum of
# the numbers instead of the average.

'''total = []
while True:
	inny = input('Please enter a non decimal number: ')
	if inny == 'done':
		print()
		print('The max of your list is: {}'.format(max(total)))	
		print('The min of your list is: {}'.format(min(total)))
		print()
		quit()
	try:
		num = int(inny)
		total.append(num)
	except:
		print('Wrong format, please enter a non decimal number')
		continue
	print(total)
print(total)'''

# Exercise 1: Write a function called chop that takes a list and modifies
# it and returns a new list that contains all but the first and last elements.

'''def chop(t):
	first = t[0]
	last = t[-2]
	return (first, last)

listy = []
while True:
	inny = input('Please enter a value: ')
	listy.append(inny)
	if inny == 'done':
		rest = chop(listy)
		print(rest)
		quit()
print(listy)'''
	
# Write a program to open the file romeo.txt and read it line by line. For
# each line, split the line into a list of words using the split function.
# For each word, check to see if the word is already in a list. If the word
# is not in the list, add it to the list. When the program completes, sort
# and print the resulting words in alphabetical order.

'''fhand = open('romeo.txt')

romeo = []
for line in fhand:
	words = line.split()
	for word in words:
		if word not in romeo:
			romeo.append(word)
			romeo.sort()
		else:
			continue
print(romeo)'''

# Write a program that reads the words in words.txt and stores them as
# keys in a dictionary. It doesn’t matter what the values are. Then you
# can use the in operator as a fast way to check whether a string is in the
# dictionary

'''fhand = open('words.txt')
dic = dict()

for line in fhand:
	word = line.split()
	for words in word:
		if words not in dic:
			dic[words] = 1
		else:
			dic[words] += 1'''

# Exercise 2: Write a program that categorizes each mail message by
# which day of the week the commit was done. To do this look for lines
# that start with “From”, then look for the third word and keep a running
# count of each of the days of the week. At the end of the program print
# out the contents of your dictionary (order does not matter).
		
'''fhand = open('mbox.txt')
dic = dict()


for line in fhand:
	word = line.split()	
	if line.startswith('From') and len(word) > 2:
		if word[2] not in dic:
			dic[word[2]] = 1
		else:
			dic[word[2]] += 1
print(dic)'''


# Exercise 3: Write a program to read through a mail log, 
# build a histogram using a dictionary to count how many messages have come from
# each email address, and print the dictionary.

'''fname = open('mbox.txt')
dic = dict()

for line in fname:
	if line.startswith('From'):
		word = line.split()
		dic[word[1]] = 1
	else:
		dic[word[1]] += 1
print(dic)'''

# Exercise 4: Add code to the above program to figure out who has the
# most messages in the file. After all the data has been read and the 
# dictionary has been created, look through the dictionary using a maximum
# loop (see Chapter 5: Maximum and minimum loops) to find who has
# the most messages and print how many messages the person has.

'''fname = open('mbox.txt')
dic = dict()

for line in fname:
	if line.startswith('From'):
		word = line.split()
		dic[word[1]] = 1
	else:
		dic[word[1]] += 1

largest = -1
theword = None
for k,v in dic.items():
	if v > largest:
		largest = v
		theword = k

smallest = 100000
small_word = None

for k,v in dic.items(): 
	if v < smallest:
		smallest = v
		small_word = k

print('The most common address is: {} shown {} times'.format(theword, largest))
print('The least common address is: {} shown {} times'.format(small_word, smallest))'''

# Exercise 5: This program records the domain name (instead of the
# address) where the message was sent from instead of who the mail came
# from (i.e., the whole email address). At the end of the program, print
# out the contents of your dictionary.

'''inny = input('Please enter a file name: ')
if len(inny) < 1:
	mbox = open('mbox.txt')
else:
	try: 
		mbox = open(inny)
	except:
		print('File not found: ',inny)
		exit()

dic = dict()

for line in mbox:
	line = line.strip().lower()
	if line.startswith('by'):
		word = line.split()
		if word[1] not in dic:
			dic[word[1]] = 1
		else:
			dic[word[1]] += 1

largest = -1
word = None

for k,v in dic.items():
	if v > largest:
		largest = v
		word = k

print(word, largest) '''

# Exercise 1: Read and parse the “From” lines and pull out the addresses from the line. 
# Count the number of messages from each person using a dictionary.
# After all the data has been read, print the person with the most commits
# by creating a list of (count, email) tuples from the dictionary. Then
# sort the list in reverse order and print out the person who has the most
# commits.

'''inny = input('Enter a file name: ')
if len(inny) < 1:
	mbox = open('mbox.txt')
else:
	try: 
		mbox = open(inny)
	except:
		print('File not found', inny)
		quit()

dic = dict()

for line in mbox:
	line = line.rstrip()
	if line.startswith('From'):
		word = line.split()
	if word[1] not in dic:
		dic[word[1]] = 1
	else:
		dic[word[1]] += 1 

lst = list()
for key, val in list(dic.items()):
	lst.append((val, key))

lst.sort(reverse=True)

for key, val in lst[:5]:
	print(key, val)'''


# Exercise 2: This program counts the distribution of the hour of the day
# for each of the messages. You can pull the hour from the “From” line
# by finding the time string and then splitting that string into parts using
# the colon character. Once you have accumulated the counts for each
# hour, print out the counts, one per line, sorted by hour as shown below.

'''fname = open('mbox.txt')

dic = dict()

for line in fname:
	line = line.strip()
	if line.startswith('From '):
		word = line.split()
		time = word[5]
	if time[:2] not in dic:
		dic[time[:2]] = 1
	else:
		dic[time[:2]] += 1

lst = list()
 
for key, value in dic.items():
	lst.append((key, value))
	lst.sort()

for key, value in lst:
	print(key, value) '''

'''fname = open('mbox.txt')

dic = dict()

for line in fname:
	line = line.strip()
	if line.startswith('From '):
		word = line.split(':') 
		for hour in word:
			hour = word[-3]
			hours = hour[-2:]	

	if hours not in dic:
		dic[hours] = 1
	else:
		dic[hours] += 1


lst = list()

for key, value in dic.items():
	lst.append((key, value))
	lst.sort()

for key, value in lst:
	print(key, value)'''

# Exercise 3: Write a program that reads a file and prints the letters
# in decreasing order of frequency. Your program should convert all the
# input to lower case and only count the letters a-z. Your program should
# not count spaces, digits, punctuation, or anything other than the letters
# a-z. Find text samples from several different languages and see how
# letter frequency varies between languages	

'''import string


fname = open('mbox.txt')

dic = dict()

for line in fname:
	line = line.lower()
	line = line.strip()
	words = line.translate(str.maketrans('', '', '!"#$%&\'()*+,-./\t:;<=>?@[]^_`{|}~\ 1234567890'))


	for word in words:
		if word not in dic:
			dic[word] = 1
		else:
			dic[word] += 1

lst = list()

for key, value in dic.items():
	lst.append((key, value))
	lst.sort()

for key, value in lst:
	print(key, value)'''






# STILL TRYING TO REMOVE THE NONE FROM BOTTOM OF PROGRAM OUTPUT
		
















