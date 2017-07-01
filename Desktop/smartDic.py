#!/usr/bin/env python

import argparse

myFile = open('pass.txt', 'w')

arr = ["qwerty1234","12345678","123456789","01234567","012345678","0123456789","123456","qwerty",
"111111", "1234567890", "123123","987654321","qwertyuiop","mynoob","123321","666666","123qwe",
"password","password1","passw0rd","qwerty123","123123123","fuckyou","football","baseball","12341234",
"00000000","11111111","qwer1234","qwerty123","dragon","superman","f*cky*u","abc123","abcd1234","king","queen"]

#birtYear lName fName name1 name2 name3 weddingYear monthBirt dayBirt 

def writeFile(arr):
	for i in arr:
		myFile.write(i+"\n")

def combine(mainArr,ar2,*other):
	for i in ar2:
		if not i in mainArr:
			mainArr.append(i)
	if other:
		for j in other:
			for k in j:
				mainArr.append(k)
	return mainArr

def allMaj(ar):
	temp = []
	for i in ar:
		if not i.upper() in ar:
			temp.append(i.upper())
	return temp

def assemble(ar):
	newArr = []
	for i in xrange(len(ar)):
		for j in xrange(len(ar)):
			if not ar[i]+ar[j] in ar:
				newArr.append(ar[i] + ar[j])
	return newArr

def insertKeyAtTheEnd(ar,key):
	temp = []
	for i in xrange(len(ar)):
		if not ar[i]+str(key) in ar:
			temp.append(ar[i]+str(key))
	return temp

def insertKeyAtTheStart(ar,key):
	temp = []
	for i in xrange(len(ar)):
		if not str(key)+ar[i] in ar:		
			temp.append(str(key)+ar[i])
	return temp

def autoCompleteTo8(ar):
	temp = []
	word = ""
	for i in xrange(len(ar)):
		word = ar[i]
		if(word<8):
			for j in xrange(1,9-len(word)):
				word += str(j)
		if not word in ar:
			temp.append(word)
	return temp
				
def nickname():
	temp = []	
	if args.username:
		temp.append(str(args.username)[:2]*2)
	if args.firstname and not str(args.firstname)[:2]*2 in temp:
		temp.append(str(args.firstname)[:2]*2)
	return temp
	

def firstLetterMaj(ar):
	newArr = []
	for i in xrange(len(ar)):
		if not ar[i][0].isupper():
			word = ar[i][0].upper() + str(ar[i][1:])
		if not word in ar:
			newArr.append(word)
	return newArr	

def upgradeWord(word):
	temp = [word]
	temp.append(str(word)+'1')
	temp.append(str(word)+'0')
	if args.favoritenumber:
		temp.append(str(args.favoritenumber)+str(word)+str(args.favoritenumber))
	return temp
	
def generateDate():
	temp = []
	if args.date and args.day and args.month:
		temp.append(str(args.day)+str(args.month)+str(args.date))
		temp.append(str(args.month)+str(args.day)+str(args.date))
	return temp

def generateMail():
	temp = []	
	if args.mail:
		word = args.mail.split("@")[0]
		if "." in word:
			temp = word.split(".")	
		else: 
			temp.append(word)
	return temp

def favoriteNumber(ar,num):
	temp = []
	if num:
		for i in xrange(len(ar)):
			if not str(ar[i])+str(num) in ar:
				temp.append(str(ar[i])+str(num))
	return temp
	

def main():

	myArr = []

	parser = argparse.ArgumentParser()

	parser.add_argument("-us", "--username",type = str ,help = "Username of the target")
	
	parser.add_argument("-fn", "--firstname",type = str ,help = "First Name of the target")

	parser.add_argument("-ln", "--lastname",type = str ,help = "Last Name of the target")

	parser.add_argument("-@", "--mail",type = str ,help = "Mail address of the target")

	parser.add_argument("-FN", "--favoritenumber",type = int ,help = "Favorite Number of the target")

	parser.add_argument("-d", "--date",type = int ,help = "Birthday Year of the target")

	parser.add_argument("-m", "--month",type = int ,help = "Birthday Month of the target")

	parser.add_argument("-dd", "--day",type = int ,help = "Birthday day of the target")

	
	r = str(raw_input("Other keys? (Important dates/Country/City/Kids name/Favorite food/Favorites Singer/President/Wedding date/Favorite movie/Favorite sport / Animals / Sport players ...) :"))	

	global args 
	args = parser.parse_args()
	
	while(len(r) > 0):
		myArr.append(r)
		r = str(raw_input("Other keys? :"))

	if args.username:
		myArr.append(args.username) #myArr = combine(myArr , upgradeWord(args.username))
	if args.firstname:
		myArr.append(args.firstname)  # myArr = combine(myArr , upgradeWord(args.firstname))
	if args.lastname:
		myArr.append(args.lastname)
	if args.date:
		myArr.append(str(args.date))
	if args.month:
		myArr.append(str(args.month))
	if args.day:
		myArr.append(str(args.day))


	'''ALGORITHMS - USING FUNCTIONS'''

	arr1 = firstLetterMaj(myArr)
	myArr = combine(myArr,nickname(),generateMail(),autoCompleteTo8(myArr),arr1,allMaj(myArr))	
	myArr = assemble(myArr)
	myArr = combine(myArr , favoriteNumber(myArr,args.favoritenumber))	
	writeFile(combine(arr,generateDate(),myArr))
	print "\n-------- SUCCESSFUL ------------"

if __name__== "__main__":
	main()
