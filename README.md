# Python Quick Start

Python is a widely used programming language (source code is now available under the GNU General Public License – GPL) started by [Guido van Rossum](http://en.wikipedia.org/wiki/Guido_van_Rossum) that supports multiple programming paradigms.

Although it is an interpreted language rather than compiled language, hence might take up more CPU time (important detail in our Computer Architecture department), Python has a gentle learning curve, Python is readable, writeable, and endlessly powerful. Its simplicity lets you become productive quickly. 

This hand-on will show some basic characteristics of Python to help to enter those **students of my course who have no prior knowledge of python**. At the end of the page you will find very useful links to advance on your own and some tips that could help you.  

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

If you need to install Python, you can download the most recent stable version of Python 2 or Python 3 from [general download page](https://www.python.org/downloads/).


Alternately, you can download and install a package, which comes with pre-installed libraries. I would recommend for beginners downloading [Anaconda](https://www.continuum.io/downloads) available for Windows, OS X or Linux, 32- or 64-bit.
Another option could be [Enthought Canopy Express](https://store.enthought.com/downloads/#default).

## Development environment

As we mentioned earlier you can use your terminal/shell based environment. However I personally prefer iPython Notebooks from Anaconda because it provides a lot of good features for documenting while writing the code itself and you can choose to run the code in blocks rather than the line by line execution in the terminal environment. We will use iPython environment for this complete hands-on tutorial.

You can start iPython notebook by writing “ipython notebook” on your terminal:
``` 
torres@vm:~$ ipython notebook

```
You can create a new iPython notebook by simply clicking on the **new** button  in the top. The interface shows **In\[\*\]**  for inputs and **Out\[\*\]** for output. You can execute a code by pressing * *“Shift + Enter”* * or * *“ALT + Enter” * *, if you want to insert an additional row after.


Before we deep dive into problem solving, lets take a step back and understand the basics of Python. As we know that data structures and iteration and conditional constructs form the crux of any language. In Python, these include lists, strings, tuples, dictionaries, for-loop, while-loop, if-else, etc. Let’s take a look at some of these.


