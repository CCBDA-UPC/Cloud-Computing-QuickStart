# Python Development Environment Quick Start

* [About this hands-on](#about)
* [Python Development Environment](#environment)
    * [Download and installing Anaconda](#anaconda)
    * [New iPython notebook](#notebook)

<a name="about"/>
Until now we discover how to write our first program in Python and how to install the required environment.  Alternately, we can download and install an environment that can simplify package management and deployment (which comes with pre-installed libraries). 
This hand-on is intended to be a "Simple Beginner’s guide" that provides a fast-paced introduction to the Python Development Environments.

<a name="environment"/>
## Python Development Environment
 
I would recommend for beginners downloading [Anaconda](https://www.continuum.io/downloads) available for Windows, OS X or Linux, 32- or 64-bit. Anaconda is a freemium open source distribution of the Python and R programming languages for large-scale data processing, predictive analytics, and scientific computing.

Another option could be [Enthought Canopy Express](https://store.enthought.com/downloads/#default). I personally prefer iPython Notebooks from Anaconda because it provides a lot of good features for documenting while writing the code itself and you can choose to run the code in blocks rather than the line by line execution in the terminal environment. We will use iPython environment for this complete hands-on tutorial.

<a name="anaconda"/>
### Download and installing Anaconda
Visit the [Anaconda](https://www.continuum.io/downloads) web page and download the correct version of package acording your OS system and follow the instructions. 

After your installation proces is finished you can start iPython notebook by writing `ipython notebook` on your terminal:
``` 
torres@vm:~$ jupyter notebook

```


This will launch a new browser window (or a new tab) showing the Notebook Dashboard on a localhost to the URL of your Notebooks, by default http://127.0.0.1:8888. Windows users need to open up their Command Prompt. You'll see a dashboard with all your Notebooks. You can launch your Notebooks from this control panel that allows (among other things) to select which notebook to open or create a new one. 

<a name="notebook"/>
### iPython notebooks
You can create a new iPython notebook by simply clicking on the **new** button  in the top. The interface shows **In\[\*\]**  for inputs and **Out\[\*\]** for output. You can execute a code by pressing *“Shift + Enter”* or *“ALT + Enter”*, if you want to insert an additional row after.  Copy \& paste the previous code example `GuessNumber.py` at **In\[1\]**, press “Shift + Enter” and introduce your guess number.

![ipythonnotebookExample](https://github.com/jorditorresBCN/Python-Quick-Start/blob/master/img/ipythonnotebookExample.png)


