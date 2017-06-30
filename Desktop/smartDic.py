#!/usr/bin/env python

import argparse

myFile = open('pass.txt', 'w')

arr = ["qwerty1234","12345678","123456789","01234567","012345678","0123456789","123456","qwerty",
"111111", "1234567890", "123123","987654321","qwertyuiop","mynoob","123321","666666","123qwe",
"password","Password1","qwerty123","123123123","fuckyou","football","baseball","12341234",
"00000000","11111111","qwer1234","qwerty123","dragon","superman","f*cky*u","abc123","abcd1234"]

#birtYear lName fName name1 name2 name3 weddingYear monthBirt dayBirt 

def writeFile(arr):
	for i in arr:
		myFile.write(i+"\n")

def combine(mainArr,ar2,*other):
	for i in ar2:
		mainArr.append(i)
	if other:
		for j in other:
			for k in j:
				mainArr.append(k)
	return mainArr

def allMaj(ar):
	temp = []
	for i in ar:
		temp.append(i.upper())
	return temp

def assemble(ar):
	newArr = []
	for i in xrange(len(ar)):
		for j in xrange(len(ar)):
			newArr.append(ar[i] + ar[j])
	return newArr

def insertKeyAtTheEnd(ar,key):
	temp = []
	for i in xrange(len(ar)):
		temp.append(ar[i]+str(key))
	return temp

def insertKeyAtTheStart(ar,key):
	temp = []
	for i in xrange(len(ar)):
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
		temp.append(word)
	return temp
				

def firstLetterMaj(ar):
	newArr = []
	for i in xrange(len(ar)):
		if not ar[i][0].isupper():
			word = ar[i][0].upper() + ar[i][1:]		
		newArr.append(word)
	return newArr	

def main():

	myArr = ["king","queen"]

	parser = argparse.ArgumentParser()

	parser.add_argument("-fn", "--firstname",type = str ,help = "First Name of the target")

	parser.add_argument("-ln", "--lastname",type = str ,help = "Last Name of the target")

	parser.add_argument("-d", "--date",type = int ,help = "Birthday Year of the target")

	parser.add_argument("-m", "--month",type = int ,help = "Birthday Month of the target")

	parser.add_argument("-dd", "--day",type = int ,help = "Birthday day of the target")
	
	r = str(raw_input("Other keys? :"))	

	args = parser.parse_args()
	
	while(len(r) > 0):
		myArr.append(r)
		r = str(raw_input("Other keys? :"))

	if args.firstname:
		myArr.append(args.firstname)
	if args.lastname:
		myArr.append(args.lastname)
	if args.date:
		myArr.append(str(args.date))
	if args.month:
		myArr.append(str(args.month))
	if args.day:
		myArr.append(str(args.day))


	'''ALGORITHMS - USING FUNCTIONS'''
	myArr = combine(myArr,assemble(firstLetterMaj(myArr)),assemble(allMaj(myArr)),assemble(autoCompleteTo8(myArr)))

	writeFile(myArr)

if __name__== "__main__":
	main()
