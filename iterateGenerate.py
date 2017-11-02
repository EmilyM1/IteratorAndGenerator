#!/usr/bin/python 3 

#counts letters in words
words = """When we speak we are afraid our words will not be heard or welcomed. 
But when we are silent, we are still afraid. So it is better to speak.""".split()
print(words)

numberoflettersineachword = [len(word) for word in words]
print(numberoflettersineachword)
#FOR EACH VALUE ON THE RIGHT, EVALUATE ITEMS ON LEFT


numbers = [1,2,4,8]
squares = [number**2 for number in numbers]
print(squares)

#dictionry comp
capitals = {"UK": "London", "Brazil": "Brasilia", "France": "Paris", "Sweden": "Stockholm"}

printcap = [capitals for k,v in capitals.items()]
print(printcap)

printval = [capitals for v in capitals.values()]
print(printval)

listofnumb = [1,2,34]
iterator = iter(listofnumb)
print(next(iterator))
print(next(iterator))

def iterator(listt):
	iterate = iter(listt)
	try:
		return next(iterate)
	except StopIteration:
		raise ValueError("no more to iterate")
print(iterator([1,2,3]))
print(iterator([1,2,3]))
print(iterator([1,2,3]))
print(iterator([1,2,3]))

#Generators next value on command, need yield, at least once or return with no arg

def generator123():
	yield 1
	yield 2
	yield 3
#returns interable object
g = generator123()
print(g)
print(next(g))
print(next(g))
print(next(g))


for v in generator123():
	print(v)
#generator function that counts and teminates at a count

def take(count, iterable):
	counter = 0
	for item in iterable:
		if counter == count:
			return
		counter +=1
		yield item

def runtake():
	iterable = [2,4,6,8,10,12]
	for iterable in take(2, iterable):
		for v in iterable:
			print(v)

print(runtake)
print(runtake)
print(runtake)

def fib():
	a, b = 0,1
	while b < 25:
		yield a
		a, b, = b, a + b

print(fib())
it = [b for b in fib()]
print(it)

#or use list to print fib
print("list form  {}" .format(list(fib())))

adict = dict(a=1, b=2, c=3)
print(adict)
dictcomp = [a for a in adict.items()]
print(dictcomp)

monday = [1,8,15]
tuesday = [2,9,16]

print([temp for temp in zip(monday, tuesday)])
a,b,c = [temp for temp in zip(monday, tuesday)]
print(a,c,b) #unpacking

#count words and show words and count of words in input string

def count_words_in_dictionary(d):
	frequency = {}
	for word in d.split():
		frequency[word] = frequency.get(word, 0) +1
	return frequency

print(count_words_in_dictionary("will it work"))