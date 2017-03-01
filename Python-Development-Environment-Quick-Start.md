# Python Development Environment Quick Start

* [About this hands-on](#about)
* [Anaconda](#AnacondaChapter)
* [Download and installing Anaconda](#installing)
* [Managing environments](#managing)
* [New iPython notebook](#ipython)
* [Kernels for Python 2 and 3](#kernels)



<a name="about"/>
Until now we discover how to write our first program in Python and how to install the required environment.  Alternately, we can download and install an environment that can simplify package management and deployment (which comes with pre-installed libraries). 
This hand-on is intended to be a "Simple Beginner’s guide" that provides a fast-paced introduction to the Python Development Environment  [Anaconda](https://www.continuum.io/why-anaconda). Note that codes in these hands-ons are using Python 2.7.

<a name="AnacondaChapter"/>
## Anaconda
 
I would recommend use [Anaconda](https://www.continuum.io/why-anaconda) available for Windows, OS X or Linux, 32- or 64-bit. Anaconda is a freemium open source distribution of the Python and R programming languages for large-scale data processing, predictive analytics, and scientific computing.

Why Anaconda? Anaconda is a distribution of packages built for data science. It comes with conda, a package and environment manager. In a real project You will be using conda to create environments for isolating your projects that use different versions of Python and different packages. You could also use it to install, uninstall, and update packages in your environments. 

With Anaconda, it's simple to install the packages you will often use in real data science work. You'll also use it to create virtual environments that make working on multiple projects much less mind-twisting. Anaconda solved a lot of issues related with packages and multiple Python versions. 

<a name="Conda"/>
#### Conda
Anaconda is actually a distribution of software that comes with `conda`, `Python`, and many scientific packages and their dependencies. The application conda is a package and environment manager. Anaconda is a fairly large download (~500 MB) because it comes with the most common data science packages in Python. There is also [**Miniconda**](https://conda.io/miniconda.html), a smaller distribution that includes only conda and Python. You can still install any of the available packages with conda, it just doesn't come with them. Using conda to manage your packages and environments will reduce future issues dealing with the various libraries you'll be using. 

<a name="managing"/>
#### Managing Packages
Package managers are used to install libraries and other software on your computer. You are already familiar with `pip`, it’s the default package manager for Python libraries. `Conda` is similar to `pip` except that the available packages are focused around data science while `pip` is for general use. `conda` is not Python specific and can also install non-Python packages. However, not all Python libraries are available from the Anaconda and conda and for this reason you can still use `pip` alongside `conda` to install packages.

<a name="environments"/>
#### Environments
Along with managing packages, Conda is also a virtual environment manager. It's similar to [`virtualenv`](http://docs.python-guide.org/en/latest/dev/virtualenvs/). **Environments allow you to separate and isolate the packages you are using for different projects**. Sometimes you could be working with code that depends on different versions of some library. For example, you could have code that uses new features of a package, or code that uses old features that have been removed from the package. It’s practically impossible to have two versions of the same package installed at once. Instead, you should make an environment for each version of the package then work in the appropriate environment for the project.  This issue happens a lot when dealing with Python 2 and Python 3 at the same time.

We can also export the list of packages in an environment to a file, then include that file with your code. This allows other people to easily load all the dependencies for our code. Pip has similar functionality with `pip freeze > requirements.txt` (“freeze” the current state of the environment packages creating a `requirements.txt` file, which contains a simple list of all the packages in the current environment, and their respective versions).

<a name="installing"/>
## Download and installing Anaconda
Visit the [Anaconda](https://www.continuum.io/downloads) web page and download the correct version of package acording your OS system and follow the instructions. Anaconda is available for Windows, Mac OS X, and Linux.  If you already have Python installed on your computer, this won't break anything. Instead, the default Python used by your scripts and programs will be the one that comes with Anaconda.

After installation, you’re automatically in the default conda environment with all packages installed which you can see below. You can check out your own install by entering `conda list` into your terminal. Once you have Anaconda installed, managing packages is fairly straightforward. To install a package, type `conda install package_name` in your terminal. Conda  automatically installs package dependencies for you (for instance, installing `pandas` by itself will also install `numpy` since `numpy` is a dependency of `pandas`). Conda makes sure to also install any packages that are required by the package you're installing..  To uninstall, use `conda remove package_name`. To update a package `conda update package_name`. If you want to update all packages in an environment you can use `conda update --all`. 


<a name="managing"/>
## Managing environments

### Create environments
As  We mentioned before, conda can be used to create environments to isolate a project. To create an environment, we can use `conda create -n env_name list of packages`. Here `-n env_name` sets the name of your environment and `list of packages` is the list of packages you want installed in the environment. For example, to create an environment named `my_env` and install `numpy` in it, we need to type `conda create -n my_env numpy`.


A very important point is that when creating an environment, we can specify which **version of Python to install** in the environment. This is useful when we are working with code in both Python 2.x and Python 3.x. To create an environment with a specific Python version we can type `conda create -n my_py3_env python=3` or `conda create -n my_py2_env python=2`. These commands will install the most recent version of Python 3 and 2, respectively. To install a specific version, use `conda create -n py python=3.6` for Python 3.6.

### Activate environments
Once we have an environment created, we can use `source activate my_env` to enter it on OSX or Linux (on Windows use `activate my_env`).

When we are in the environment, we will see the environment name in the terminal prompt between brakets. Something like `(my_env) ~ $`. The environment has only a few packages installed by default, plus the ones you installed when creating it. You can check this out with conda list. Installing packages in the environment is the same as before, use `conda install package_name`. Only this time, the specific packages you install will only be available when you're in the environment. 

### Deactivate environments
To leave the environment, type `source deactivate` on OSX or Linux. On Windows, use `deactivate`.

### Listing environments
You can use `conda env list` to list out all the environments you've created. 

### Removing environments
If there are environments you don't use anymore, you can use `conda env remove -n env_name` to remove the specified environment.

For more detailed information about conda you can read the [conda documentation](https://conda.io/docs/using/index.html)  and how it fits in the Python ecosystem you can read [this article](https://jakevdp.github.io/blog/2016/08/25/conda-myths-and-misconceptions/).


<a name="ipython"/>
## New ipython notebook

After your installation proces is finished you can start iPython notebook by writing `ipython notebook` on your terminal:
``` 
torres@vm:~$ jupyter notebook

```


This will launch a new browser window (or a new tab) showing the Notebook Dashboard on a localhost to the URL of your Notebooks, by default http://127.0.0.1:8888. Windows users need to open up their Command Prompt. You'll see a dashboard with all your Notebooks. You can launch your Notebooks from this control panel that allows (among other things) to select which notebook to open or create a new one. 


You can create a new iPython notebook by simply clicking on the **new** button  in the top. The interface shows **In\[\*\]**  for inputs and **Out\[\*\]** for output. You can execute a code by pressing *“Shift + Enter”* or *“ALT + Enter”*, if you want to insert an additional row after.  Copy \& paste the previous code example `GuessNumber.py` at **In\[1\]**, press “Shift + Enter” and introduce your guess number.

![ipythonnotebookExample](https://github.com/jorditorresBCN/Python-Quick-Start/blob/master/img/ipythonnotebookExample.png)


acknowledgements: This "Quick Start" has borrowed some ideas and phrases from the course ["Artificial Intelligence"](https://www.udacity.com) Udacity Nanodegree.

<a name="kernels"/>

##  Kernels for Python 2 and 3
If you’re running Jupyter on Python 3, you can set up a Python 2 kernel like this:
```
conda create -n ipykernel_py2 python=2 ipykernel
source activate ipykernel_py2    # On Windows, remove the word 'source'
python -m ipykernel install --user
```

To activate this environment, use:
```
source activate ipykernel_py2
```

To deactivate this environment, use:

```
source deactivate ipykernel_py2
```


If you’re running Jupyter on Python 2 and want to set up a Python 3 kernel, follow the same steps, replacing `2` with `3`.

The last command installs a [kernel spec](https://jupyter-client.readthedocs.io/en/latest/kernels.html#kernelspecs) JSON file for the current python installation.

_**Acknowledgements: This "Quick Start" has borrowed some ideas and content from the Udacity Nanodegree course ["Artificial Intelligence"](https://www.udacity.com).**_

