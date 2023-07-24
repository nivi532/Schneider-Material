# Printing in python
print("This is for testing\n")

# Variable assignment and getting input in python
var = 25
var2 = input("Enter any number: ")
print(var, " and ", var2)

# Elif ladder
num = 4
print("\nTesting elif ladder:")
if num > 2:
    print(num, "\n")
elif num == 0:
    print("0\n")
else:
    print("wasted\n")

# for loop
for i in range(5,10,22):
    print(i)

# while loop
count = 0
print()
while (count < 3):
    count = count + 1
    print("Testing while loop ", count)

# String functions:
str = "Testing string"
print("\n string declared: ", str)

# Accessing characters of the string
print("\nThird character of String is: ")
print(str[2])

# Reverse a string
str = "".join(reversed(str))
print(str)

# slicing of a string:
print("\nSlicing characters between " + "3rd and 2nd last character: ")
print(str[3:-2])

# Deleting a string:
del str 

# list, tuple, dictionary and set
ls = [2, "hello", 4.2]
tp = (1, 2, 3, 4)
dict = {1: "hi", 2: "hello", 3: "hey"}
sets = {"yo",}

print()
print (ls, " - ", type(ls))
print (tp, " - ", type(tp))
print (dict, " - ", type(dict))
print (sets, " - ", type(sets))

#methods of list
ls = [1, "hello", 3.5, 5, "test", 5.78]
print("\n3rd element", ls[2]) #accessing ls element
print("Negative indexing: ", ls[-2]) 
print("Length of ls - ", len(ls)) # length of ls

#list input:
string = input("Enter elements (Space-Separated): ")
ls = string.split()  
print('The ls is:', ls)

ls = []
print("Initial blank ls: ", ls)
  
# Addition of Elements
ls.append(1)
ls.append(2)
ls.append(4)
print("\nls after Addition of Three elements: ")
print(ls)
  
# using Iterator
for i in range(1, 4):
    ls.append(i)
print("\nls after Addition of elements from 1-3: ")
print(ls)
  
# Adding Tuples to the list
ls.append((5, 6))
print("\nls after Addition of a Tuple: ")
print(ls)
  
# Addition of list to a list
ls2 = ['For', 'Geeks']
ls.append(ls2)
print("\nList after Addition of a list: ")
print(ls)

# Insertion in a list:
print("\nInsertion in a list: ")
ls.insert(2, "yes")
print(ls)

# Remove elements in a list:
ls.remove(2)
print(ls)

# Slicing in a list
ls = ['G', 'E', 'E', 'K', 'S', 'F', 'O', 'R', 'G', 'E', 'E', 'K', 'S']
print("Slicing in a List: ")
print(ls)
Sliced_ls = ls[3:8]
print("\nSlicing elements in a range 3-8: ")
print(Sliced_ls)

# Negative slicing
Sliced_ls = ls[-6:-1]
print("\nElements sliced from index -6 to -1")
print(Sliced_ls)

# List comprehension
even_square = [x ** 2 for x in range(1, 11) if x % 2 == 0]
print(even_square)

# Nested dictionary
dict = {1: 'test', 2: 'is', 3: {'A': 'for', 'B': 'fun', 'C': 'hahaha'}}
print(dict)
print(dict[3]['A'])

# another way to initialize dictionary
dict[0] = 'loool'
dict[2] = 'yo'
dict[3] = 1
print("\nDictionary after adding 3 elements: ")
print(dict)

# accessing a element using key
print("Accessing a element using key:")
print(dict[2])

#Deleting some of the Dictionary data
del(dict[1]) 

# user-defined functions
def add(num1, num2):
    num3 = num1 + num2
    return num3
 
num1, num2 = 5, 15
ans = add(num1, num2)
print(f"The addition of {num1} and {num2} results {ans}.")

# Classes:
class testing:
    attr1 = "x"
    attr2 = "y"
 
    def fun(self):
        print("letter ", self.attr1)
        print("letter", self.attr2)

example = testing()
print(example.attr1)
example.fun()

# self in class:
class test:
    def __init__(self, name, company):
        self.name = name
        self.company = company
 
    def show(self):
        print("Hello my name is " + self.name+" and I" +
              " work in "+self.company+".")
         
obj = test("Nivi", "Schneider")
obj.show()

# set and get
class Dog:
	animal = 'dog'
	def __init__(self, breed):
		self.breed = breed

	def setColor(self, color):
		self.color = color

	def getColor(self):
		return self.color

Rodger = Dog("pug")
Rodger.setColor("brown")
print(Rodger.getColor())