# Python Quick Start
Table of contents
=================

  * [How to Install Python](#How-to-Install-Python)
  * [HPython Basics](#Python-Basics)

- How to Install Python
- Python Basics
- Warming up: Running your first Python program
- Python Development Environment


Python is a widely used programming language (source code is now available under the GNU General Public License – GPL) started by [Guido van Rossum](http://en.wikipedia.org/wiki/Guido_van_Rossum) that supports multiple programming paradigms.

Although it is an interpreted language rather than compiled language, hence might take up more CPU time (important detail in our Computer Architecture department), Python has a gentle learning curve, Python is readable, writeable, and endlessly powerful. Its simplicity lets you become productive quickly. 

This hand-on will show some basic characteristics of Python to help to enter those **students of my course who have no prior knowledge of python**. 



## How to install Python?

We can install Python 2 or Python 3. This is one of the debated topics in Python. There is no right/wrong choice here, specially if you are a beginner. Python 2 has an awesome community support, plethora of third-party libraries. On the other hand Python 3 is cleaner and faster. For the purpouse of this hands-on it is not important, the student should focus on learning Python as a language. For advice on choosing between Python 2 and Python 3 see [Python 2 or 3](https://wiki.python.org/moin/Python2orPython3).

Before you start, you will need Python on your computer, but you may not need to download it. Nowadays many Linux and UNIX distributions include a recent Python. Even some Windows computers now come with Python already installed. First of all check that you don’t already have Python installed by entering python in a command line. If you see a response from a Python interpreter it will include a version number in its initial display. If you use are in a environment you will see:

``` 
torres@vm:~$ python
Python 2.7.10 (default, Sep 23 2015, 04:34:14) 
[GCC 4.2.1 Compatible Apple LLVM 7.0.0 (clang-700.0.72)] on darwin
Type "help", "copyright", "credits" or "license" for more information.
>>> 
```
For Warming up you can run your first Python program. You can use Python as a simple calculator to start with:
``` 
>>> 15+10
25
>>> 
```
Congratulations, good job!

>Note: Lines beginning with ">>>" and "..." indicate input to Python (these are the default prompts of the interactive interpreter). Everything else is output from Python.

If you need to install Python, you can download the most recent stable version of Python 2 or Python 3 from [general download page](https://www.python.org/downloads/).

## Python basics
###Line indentation

Python has no mandatory statement termination characters and blocks are specified by indentation (there are no braces to indicate blocks of code for class and function definitions or flow control). Statements that expect an indentation level end in a colon (:). The number of spaces in the indentation is variable, but all statements within the block must be indented the same amount. Python will advise you if there is a unclear line indentation with the following warning:

``` 

IndentationError: unexpected indent

```
Comments start with the pound (#) sign and are single-line, multi-line strings are used for multi-line comments.

###Variables and operators

Python is implicitly typed language (i.e. you don’t have to declare variables), case sensitive (i.e. Barcelona and BARCELONA are two different variables) and object-oriented (i.e. everything is an object). Help in Python is always available right in the interpreter. Type *help()* for interactive help, or *help(object)* for help about object. If you want to know how an object works, all you have to do is call *help(\<object\>)* Also useful are *dir()*, which shows you all the object’s methods:


```

>>> help (int)

Help on int object:
class int(object)
| int(x=0) -> int or long
| int(x, base=10) -> int or long
| 
…

| Methods defined here:
| 
| __abs__(…)
| x.__abs__() <==> abs(x)
…

(type q to exit)

```
The addition, subtraction, multiplication, and division operations work just like expected. In addition we can use the modulus operator (%). All the modulus operator does is to divide the left side by the right side and get the remainder. The floor division operator (//) just divides the number and rounds down. The double * is just an easy way to provide exponents to Python.

Values are assigned with the sign “=”, in fact, objects are bound to names (the equality testing is done using two equal signs “==”). It is possible use the += and -= operators on many datatypes, strings included. You can also use multiple variables and swaps variables in one line. It doesn’t violate variable typing because values aren’t actually being assigned, but new objects are bound to the old names.

``` 
>>> IntegerVar = 10
>>> IntegerVar += 10
>>> print IntegerVar
20
>>> StringVar = "Welcome"
>>> StringVar += " to Barcelona"
>>> print StringVar
Welcome to Barcelona
>>> IntegerVar, StringVar = StringVar, IntegerVar
>>> print IntegerVar
Welcome to Barcelona
>>> print StringVar
20
>>> help (StringVar)
Help on int object:

class int(object)
| int(x=0) -> int or long
| int(x, base=10) -> int or long
| 
…

```
###Data types

The data structures available in Python are lists, tuples and dictionaries. Lists are like one-dimensional arrays and we can also have lists of other lists or tuples. There are number of methods for lists (methods follow the list name). Tuples are immutable one-dimensional array.

``` 
>>> sampleList = [1,2,3,4,5,6,7,8]
>>> print (sampleList[1])
2
>>> sampleTuple = (1,2,3,4,5,6,7,8)
>>> print (sampleTuple)
(1, 2, 3, 4, 5, 6, 7, 8)
>>> print sampleList
[1, 2, 3, 4, 5, 6, 7, 8]
>>> sampleList.append(9)
>>> print sampleList
[1, 2, 3, 4, 5, 6, 7, 8, 9]
>>> sampleTuple.append(9)
Traceback (most recent call last):
  File “<stdin>”, line 1, in <module>
AttributeError: 'tuple' object has no attribute ‘append’
>>>

```

Python dictionaries are associative arrays that has keys to obtain the elements of the dictionary. Dictionaries aren’t exactly based on an index, there is no particular order in dictionaries (we could add a key: value and, it will appear in random places). A big caution here is that you cannot create different values with the same key (Python will just overwrite the value of the duplicate keys).

``` 
>>> myDicc = {'someItem': 2, 'otherItem': 20}
>>> print(myDicc['otherItem'])
20
>>>

```
Python lists/dictionaries/tuples can be of any type, so you can mix them in. Variables can point to functions. The index of the first element is 0 and negative numbers count from the end towards the beginning ( -1 is the last element).

``` 
>>> Example = [1, "BCN", ["another", "list"], {"and","a","tuple"}]
>>> print Example
[1, 'BCN', ['another', 'list'], set(['a', 'and', 'tuple'])]
>>> myfunction = len
>>> print myfunction (Example)
4
>>> print Example[-1]
set(['a', 'and', 'tuple'])
>>> print Example[3]
set(['a', 'and', 'tuple'])

```

Finally, Python strings can use either single or double quotation marks, and we can have quotation marks of one kind inside a string that uses the other kind (i.e. "He said 'I enjoy Barcelona'." ). Multiline strings are enclosed in triple double (or single) quotes  ("""). Another interesting feature is that Python supports Unicode out of the box, using the syntax u”This is a unicode string example”. To fill a string with values, we use the % operator and a tuple. Each %s gets replaced with an item from the tuple, left to right, and we can also use dictionary substitutions as we show in the following example:

``` 
>>> MultiString = """ Example of 
… a multiline
… string"""
>>> print MultiString
 Example of 
a multiline
string
>>> 
>>> print "Arrival: %s from %s" % ( "BA230", "Barcelona")
Arrival: BA230 from Barcelona
>>> print "Arrival: %(fly)s from %(city)s" % {"fly":"BA230", "city":"Barcelona"}
Arrival: BA230 from Barcelona

```

###Flow control statements
Flow control statements are *if*, *for*, and *while*.  Often partnered with the if statement are else if and else. However, Python's else if is shortened into elif. After every conditional we have a colon. Next, we could proceed to a new line with number of spaces to tell Python we only want this code to be run when the previous conditional is satisfied. 

``` 
>>> a = 20
>>> if a >= 22:
...     print("Paris")
... elif a >= 21:
...     print("Londres")
... else:
...     print("Barcelona")
... 
Barcelona
>>> 

```
Loops in Python are very versatile and simple.

``` 
>>> for a in range(1,4):
...     print (a)
... 
1
2
3
>>> 

>>> a = 1
>>> while a < 4:
...     print (a)
...     a+=1
... 
1
2
3
>>>

```
You can stop the loop using the “break” statement.

In this example we use the range keyword (used to enumerate through members of a list and to obtain a list of numbers) to set the starting point and the point right after we would finish (this is precisely why the number 4 didn’t print). Python is quite fond of this idea of all the way up to a number, but not including it.

###Functions
We can define a function by using the keyword def before your function name. Optional arguments are set in the function declaration after the mandatory arguments by being assigned a default value. Functions can return a tuple (and using tuple unpacking you can effectively return multiple values).

```
>>> 
>>> def someFunction():
...     print("Barcelona")
... 
>>> someFunction()
Barcelona
>>> 
>>> def fib(n):    # write Fibonacci series up to n
...     a, b = 0, 1
...     while b < n:
...             print b,
...             a, b = b, a+b
... 
>>> fib(1000)
1 1 2 3 5 8 13 21 34 55 89 144 233 377 610 987
>>> 
```

###Lambda Functions
Python supports the creation of anonymous functions (i.e. functions that are not bound to a name) at runtime, using a construct called “lambda”. 

>This is not exactly the same as lambda in functional programming languages

This piece of code shows the difference between a normal function definition("Jordi") and a lambda function ("George"):

```
>>> def Jordi (x): return x**2
... 
>>> print Jordi(10)
100
>>> 
>>> George=lambda x:x**2
>>> print George(10)
100
>>> 

```
As you can see, Jordi() and George() do exactly the same and can be used in the same ways. Note that the lambda definition does not include a "return" statement. Also we can put a lambda definition anywhere a function is expected, and we don't have to assign it to a variable at all as we could see in the following examples:

```
>>>
>>> fibonacci = (lambda x: 1 if x <= 2 else fibonacci(x-1) +  fibonacci(x-2))
>>> fibonacci(10)
55
>>> foo = [2, 18, 9, 22, 17, 24, 8, 12, 27]
>>> for i in filter(lambda x: x % 3 == 0, foo):
...     print (i)
... 
18
9
24
12
27
>>> 

```

###Classes

Python supports a limited form of multiple inheritance in classes.

```
>>> 
>>> class Calculator(object):
... #define class to simulate a calculator
...     def __init__ (self):
...             #start with zero
...             self.current = 0
...     def add(self, amount):
...             #add number to current
...             self.current += amount
...     def getCurrent(self):
...             return self.current
... 
>>> myCalc = Calculator() # make myCalc into a Calculator object
>>> myCalc.add(2) #use myCalc’s new add method derived from the Calculator class>>> print(myCalc.getCurrent())  
2
>>> myCalc.add(2)
>>> print(myCalc.getCurrent())
4
>>> 
```
In the previous example the first part defines a Class. def __init__ is the constructor function, the function that is called when a new instance of the class is created. The actual new instance is created in the line myCalc = Calculator(). The second part shows how to use this class in Python.

###Iterators

Python define a object type for taking each item of something, one after another. Any time you use a loop, explicit or implicit, to go over a group of items, that is iteration

An iterable is an object that has an __iter__ method which returns an iterator, or which defines a __getitem__ method that can take sequential indexes starting from zero.

An iterator is an object with a next (Python 2) or __next__ (Python 3) method.

```
>>> vec = [1, 2, 3]
>>> it = iter (vec)
>>> next (it)
1
>>> next (it)
2
>>> next (it)
3
>>> type (vec)
<class ‘list’>
>>> type (it)
<class ‘list_iterator’>
```
###Exceptions

Exceptions in Python are handled with try-except blocks. See the following code for one example:

```
>>> def function():
...     try:
...             # Division by zero raises an exception
...             10 / 0
...     except ZeroDivisionError:
...             print "Invalid operation."
... 
>>> function()
Invalid operation.
>>> 

```

###Importing
External libraries are used with the import \[libname\] keyword. We can also use from \[libname\] import \[funcname\] for individual functions.

```
>>> from random import randint
>>> randomint = random.randint(1, 100)
>>> print randomint
84
>>> randomint = random.randint(1, 100)
>>> print randomint
44
>>>
```
In this example we are showing how first we are importing the whole library and then accessing and individual function of that library, and then how we can import just the individual function and use it directly without needing to write the library.

###Read/Write files
Python uses the following sintax for read/write files:
```
>>> f = open("test.txt","w") #opens file with name of "test.txt"
>>> f.write("Barcelona, ")
>>> f.write("is the best city of the world.")
>>> f.write("With an excellent weather.")
>>> f.close()
>>> 
>>> f = open("test.txt","r") #opens file with name of "test.txt"
>>> print(f.read())
Barcelona, is the best city of the world.With an excellent weather.
>>> f.close()

```
## Warming up: Running your first Python program

Using the “random” library, we write a code that generates a random number between 1 and 20. Then let the player guess the number introduced, displaying if the number is to low or high. The game ends either when the number is guesses correctly.

``` 
import random
randomNumber = random.randrange(0,20)
print("Random number between 0 and 20 has been generated")
guessed = False
while guessed==False:
    userNumber = int(input("Introduce your guess number: "))
    if userNumber==randomNumber:
        guessed = True
        print("Excellent, Well done!")
    elif userNumber>randomNumber:
        print("Try one more time, a bit lower")
    elif userNumber < randomNumber:
        print("Try one more time, a bit higher")
print("Yes, you can!")

```

To run a python script, simply use the following terminal command, where <file path> is the path to the file containing your script (python scripts must have the .py extension):

```
 torres@vm:~$ python guessnumber.py
```

## Python Development Environment
 
Until now we discover how to write our first programb in Python and how to install the required environment. 

Alternately, we can download and install an environment that can simplify package management and deployment (which comes with pre-installed libraries). 

I would recommend for beginners downloading [Anaconda](https://www.continuum.io/downloads) available for Windows, OS X or Linux, 32- or 64-bit. Anaconda is a freemium open source distribution of the Python and R programming languages for large-scale data processing, predictive analytics, and scientific computing.

Another option could be [Enthought Canopy Express](https://store.enthought.com/downloads/#default). I personally prefer iPython Notebooks from Anaconda because it provides a lot of good features for documenting while writing the code itself and you can choose to run the code in blocks rather than the line by line execution in the terminal environment. We will use iPython environment for this complete hands-on tutorial.

### Download and installing Anaconda
Visit the [Anaconda](https://www.continuum.io/downloads) web page and download the correct version of package acording your OS system and follow the instructions. 

After your installation proces is finished you can start iPython notebook by writing `ipython notebook` on your terminal:
``` 
torres@vm:~$ ipython notebook

```


This will launch a new browser window (or a new tab) showing the Notebook Dashboard on a localhost to the URL of your Notebooks, by default http://127.0.0.1:8888. Windows users need to open up their Command Prompt. You'll see a dashboard with all your Notebooks. You can launch your Notebooks from this control panel that allows (among other things) to select which notebook to open or create a new one. 

You can create a new iPython notebook by simply clicking on the **new** button  in the top. The interface shows **In\[\*\]**  for inputs and **Out\[\*\]** for output. You can execute a code by pressing *“Shift + Enter”* or *“ALT + Enter”*, if you want to insert an additional row after.


![ipythonnotebookExample](https://github.com/jorditorresBCN/Python-Quick-Start/blob/master/img/ipythonnotebookExample.png)

Open the [GuessNumber.ipynb](https://github.com/jorditorresBCN/Python-Quick-Start/blob/master/GuessNumber.ipynb) file with your **Anaconda** environment. You can copy \& paste the code at **In\[1\]**, press “Shift + Enter” and introduce your guess number.


**First version: 30/11/2013. Updates 5/02/2014, 29/12/2016.**
