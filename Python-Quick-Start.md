# Python Quick Start

* [About this hands-on guide](#about)
* [How to Install Python](#install)
* [Python Basics](#basics)
    * [Line indentation](#indentation)
    * [Variables and operators](#variables)
    * [Data types](#datatypes)
    * [Flow control statements](#flow)
    * [Functions](#functions)
    * [Lambda Functions](#lambda)
    * [Classes](#classes)
    * [Iterators](#iterators)
    * [Exceptions](#exceptions)
    * [Importing](#importing)
    * [Read/Write files](#files)
* [Python Environment](#environment)
    * [Python packages](#packages)
    * [Pip and virtualenv](#pip)
* [Warming up: Running your first Python program](#first)

<a name="about"/>

Python is a widely used programming language (source code is now available under the GNU General Public License – GPL) started by [Guido van Rossum](http://en.wikipedia.org/wiki/Guido_van_Rossum) that supports multiple programming paradigms.

Although it is an interpreted language rather than compiled language and therefore programs might take up more CPU time (important detail for us, people from Computer Architecture department), Python has a gentle learning curve. Python is readable, writeable, and endlessly powerful. Its simplicity lets you become productive quickly.

Python is the programming language of choice for many of my courses at the Facultat d'Informàtica de Barcelona (Barcelona School of Informatics, FIB), the teaching institution of the Universitat Politècnica de Catalunya - BarcelonaTech (UPC) in charge of university education in the fields of computer science, computer engineering, and related matters.

This hand-on quickstart guide is a "Simple Beginner’s guide" that provides a fast-paced introduction to the basic characteristics of Python. It is intended for those students of any CS Master Courses who have no prior knowledge of Python to help them learn the required background knowledge by themselves.

<a name="install"/>

## How to install Python

We can install Python 2 or Python 3. This is one of the debated topics in Python. There is no right/wrong choice here, specially if you are a beginner. Python 2 has an awesome community support, plethora of third-party libraries. On the other hand Python 3 is cleaner and faster. For the purpouse of this hands-on guide the used version is not important, the student should focus on learning Python as a language. If you need advice on choosing between Python 2 and Python 3 see [Python 2 or 3](https://wiki.python.org/moin/Python2orPython3).

For the most part, Python 2 code will work with Python 3. Of course, most new features introduced with Python 3 versions are not backwards compatible. The place where your Python 2 code will fail most often is the `print` statement.
For most of Python's history including Python 2, printing was done like so:
```python
print "Hello", "world!"
> Hello world!
```
This was changed in Python 3 into a function.

```python
print("Hello", "world!")
> Hello world!
```

Before you continue, you will need Python on your computer, but you may not need to download it. Nowadays many Linux and UNIX distributions include a recent Python versions. Even some Windows computers nowadays come with Python already installed. First of all check that you don’t already have Python installed by entering python in the command line. If you see a response from a Python interpreter it will include a version number in its initial display:

``` 
username@vm:~$ python
Python 2.7.10 (default, Sep 23 2017, 04:34:14) 
[GCC 4.2.1 Compatible Apple LLVM 7.0.0 (clang-700.0.72)] on darwin
Type "help", "copyright", "credits" or "license" for more information.
>>> 
```
to warm up you can run your first Python program. You can use Python as a simple calculator to start with:
``` 
>>> 15+10
25
>>> 
```
Congratulations, good job!

>Note: Lines beginning with ">>>" and "..." indicate input to Python (these are the default prompt of the interactive interpreter). Everything else is output from Python.

If you need to install Python, you can download the most recent stable version of Python 2 or Python 3 from [general download page](https://www.python.org/downloads/).

<a name="basics"/>

## Python Basics

<a name="indentation"/>

### Line indentation

Python has no mandatory statement termination characters and blocks are specified by indentation (there are no braces to indicate blocks of code for class and function definitions or flow control). Statements that expect an additional indentation level at next line end with a colon (:). The number of spaces in the indentation is variable, but all statements within the block must be indented the same amount of spaces. Python will advise you if there is an unclear line indentation showing the following warning:

``` 

IndentationError: unexpected indent

```
Comments start with the pound (#) sign and are single-line, multi-line strings are used for multi-line comments.

<a name="variables"/>

### Variables and operators

Python is an implicitly typed language (i.e. you don’t have to declare variables), case sensitive (i.e. Barcelona and BARCELONA are two different variables) and object-oriented (i.e. everything is an object). Help in Python is always available within the interpreter. Type *help()* for interactive help, or *help(object)* to get help about object. If you want to know how an object works, all you have to do is call *help(\<object\>)* Another useful command is *dir()*, which shows you all the object’s methods:


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
Addition, subtraction, multiplication, and division operations work as expected. The modulus operator (%) is also available. It divides the left side operand by the right side operand and returns the remainder. The floor division operator (//) divides both operands and rounds down the result. The double * is just an easy way to provide exponents to Python.

Values are assigned using the equal sign “=”, in fact, objects are bound to names (the equality testing is done using two equal signs “==”). It is also possible use the += and -= operators on many datatypes, strings included. You can also use multiple variables and swap variables in one line. It doesn’t violate variable typing because values aren’t actually being assigned, but new objects are bound to the old names.

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
<a name="datatypes"/>

### Data types

The data structures available in Python are lists, tuples and dictionaries. Lists are like one-dimensional arrays and we can also have lists of other lists or lists of tuples. Tuples are **immutable** one-dimensional arrays. There are abundant methods that can be applied to lists (methods follow the list name). 

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

Python dictionaries are associative arrays that use keys to retrieve the elements of the dictionary. Dictionaries aren’t exactly based on an index, there is no particular order in dictionaries (we could add a key: value and, it will appear in random order). A big caution here is that you cannot create different values associated to the same key (Python will just overwrite the value of the duplicate keys).

``` 
>>> myDicc = {'someItem': 2, 'otherItem': 20}
>>> print(myDicc['otherItem'])
20
>>>

```
Python lists/dictionaries/tuples can be of any type, therefore you can mix them in. Variables can also point to functions. The index of the first element is 0 and negative numbers used as index count from the end of the data structure towards the beginning (being -1 the last element).

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

Finally, Python strings use either single or double quotation marks, and we can have quotation marks of one kind inside a string that uses the other kind (i.e. "He said 'I enjoy Barcelona'." ). Multiline strings are enclosed by three double (or single) quotes  ("""). Another interesting feature is that Python supports Unicode encoding out of the box, using the syntax u”This is a unicode string example”. To compose a string with values of different types, we use the % operator and a tuple. Each %s gets replaced by an item from the tuple, left to right, and we can also use dictionary replacements as we show in the following example:

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

<a name="flow"/>

### Flow control statements
Flow control statements are *if*, *for*, and *while*.  Often partnered with the if statement are *else if* and *else*. However, Python's *else if* is shortened into *elif*. After every conditional statement we have a colon. Next, we could proceed to a new indented line to tell Python we only want this code to be run when the previous conditional is satisfied. 

``` 
>>> a = 20
>>> if a >= 22:
...     print("Paris")
... elif a >= 21:
...     print("London")
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
You can exit the loop using the “break” statement.

In the above example we use the range keyword (used to enumerate through members of a list and to obtain a list of numbers) to set the starting point and the point **right after the end** (that is precisely why number 4 didn’t print). Python is quite fond of this idea of all the way up to a number, but not including it.

<a name="functions"/>
### Functions
We can define a function by using the keyword *def* before the function name. Optional arguments are set in the function declaration after the mandatory arguments by being assigned a default value. Functions can return a tuple (and by using tuple unpacking you can effectively return multiple values).

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

<a name="lambda"/>

### Lambda Functions
Python supports the creation of anonymous functions (i.e. functions that are not bound to a name) at runtime, using a construct called “lambda”. 

>This is not exactly the same as lambda in functional programming languages

This piece of code shows the difference between defining a regular function ("Jordi") and a lambda function ("George"):

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
As you can see, Jordi() and George() do exactly the same and can be used in the same way. Note that the lambda definition does not include a "return" statement. Also we can put a lambda definition anywhere a function is expected, and we don't have to assign it to a variable at all, as we could see in the following examples:

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

<a name="classes"/>

### Classes

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
>>> myCalc = Calculator() # make myCalc a Calculator object
>>> myCalc.add(2) #use myCalc’s new add method derived from the Calculator class>>> print(myCalc.getCurrent())  
2
>>> myCalc.add(2)
>>> print(myCalc.getCurrent())
4
>>> 
```
In the previous example the first part defines a Class. def __init__ is the *constructor function*, the function that is called when a new instance of the class is created. The actual new instance is created in the line myCalc = Calculator(). The second part shows how to use that class in Python.

<a name="iterators"/>

### Iterators

Python defines an object type for taking each item from an structured data type, one after another. Any time you use a loop, explicitly or implicitly, to go over a group of items, that is iteration.

An **iterable** is an object that has an __iter__ method which returns an iterator, or which defines a __getitem__ method that can take sequential indexes starting from zero.

An **iterator** is an object with a next (Python 2) or __next__ (Python 3) method.

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
<a name="exceptions"/>

### Exceptions

Exceptions in Python are handled using try-except blocks. See the following code as an example:

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

<a name="importing"/>

### Importing
External libraries are used with the import \[libname\] keyword. We can also use from \[libname\] import \[funcname\] to import individual functions.

```
>>> import random
>>> randomint = random.randint(1, 100)
67
>>> print randomint
>>>
>>> from random import randint
>>> randomint = random.randint(1, 100)
>>> print randomint
84
>>> randomint = random.randint(1, 100)
>>> print randomint
44
>>>
```
In the above example we first import the whole library and then access an individual function of that library, and then how we can import just the individual function and use it directly without needing to read the whole library.



<a name="files"/>

### Read/Write files
Python uses the following sintax to read/write files:
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
<a name="#environment"/>

## Python Environment

<a name="packages"/>

### Python Packages
We already know how to import packages. You can find nearly 100.000 packages [here](https://pypi.python.org/pypi). However let us go through some of them as an example, since we could need them for scientific computation and data analysis:

* **NumPy** and **SciPy** stand for Numerical Python and Scientific Python respectively. The most powerful feature of NumPy is n-dimensional array. This library also contains linear algebra functions or advanced random number capabilities. SciPy stands for Scientific Python and it is built on NumPy. Numpy and Scipy took python from a general purpose programming language to a very powerful matrix-oriented one.

* **Pandas** is a library for structured data operation and manipulation. It is built on top of NumPy and it offers convenient data structures, called *Series* and *DataFrame*, which allow us to perform data manipulation in a flexible and concise way. Let's consider the following example, run from the Python interactive interpreter, using a small made-up toy example of user data:
     
```
   >>> import pandas as pd
   >>> data = {'user_id': [1, 2, 3, 4], 'age': [25, 31, 31, 55]}
   >>> frame = pd.DataFrame(data, columns=['user_id', 'age'])
   >>> frame.head()
   user_id age
   0 1 25
   1 2 31
   2 3 31
   3 4 55 
```

* **Matplotlib** for plotting vast variety of graphs, starting from histograms to line plots to heat plots. You can use Pylab feature in ipython notebook ( `ipython notebook –pylab = inline` ) to use these plotting features inline (we will use this in the next section).

* **Scikit_Learn** for machine learning. Built on top of NumPy, SciPy and matplotlib, this library contains a lot of effiecient tools for machine learning and statistical modeling.

<a name="pip"/>

### Pip and virtualenv
virtualenv is a tool for creating and managing different isolated Python environments. By using an isolated virtual environment, we can maintain multiple projects that require different configurations and easily switch from one to the other.  To install `virtualenv` we can use pip from a terminal (Linux/Unix) or command prompt (Windows):

```
$ [sudo] pip install virtualenv
```
Once `virtualenv` is available, we can define a separate Python environment for each project where dependencies are installed in isolation, without tampering with the global environment. In order to set up a virtual environment ( `my_env` ) you can follow these steps:

```
$ mkdir my_new_project 
$ cd my_new_project 
$ virtualenv my_env 
```
In order to activate the environment, we can type the following command:

```
$ source my_env/bin/activate
```
Once the environment is active, the following will be added on the prompt:

```
(my_env)$
```
Python packages can be installed for this particular environment using `pip`:

```
(my_env)$ pip install [package-name]
```
When we want to deactivate the virtual environment, we can simply type the following
command:
```
$ deactivate
```

<a name="first"/>

## Warming up: Running your first Python program

Using the “random” library, we have written some code that generates a random number between 1 and 20. Then let the player guess the number drawn, replying if the user's introduced number is above or below. The game ends when the number is correctly guessed.

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

Now, we are ready to start a new hands-on guide. Enjoy!

**First version: 30/11/2013. Updates 5/02/2014, 29/01/2017, 1/06/2017.**
