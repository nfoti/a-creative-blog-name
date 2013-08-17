Title: Setting up python in virtualenv for data analysis on OSX
Date: 2012-07-17 14:35
Category: Python
Tags: virtualenv, osx
Slug: setting-up-python-in-virtualenv-for-data-analysis-on-osx
Author: Nick Foti

I have decided to use python for my research code as I have become fed up with
needing an internet connection to work with Matlab and not being able to
check out a license for toolboxes I need (e.g. the statistics toolbox) right
before a paper deadline.  I have
used python for while for munging raw data for input to Matlab, but have just
recently felt that I could work with python as effectively as I could with
Matlab.

I wanted my Python installation to use the newest versions of the various
modules used for data analysis (e.g. numpy,
scipy, ipython, matplotlib, etc.).  Since I already had the source for many of
these projects I decided to build the current master branches (after a git pull
to get the latest sources) with all of the bells and whistles like the ipython
qt console and notebook.  Additionally, I wanted to put everything in a
virtualenv to isolate it from my system Python in case I broke anything.  In
the process I ran into a few problems and eventually figured out how to get a
working system, in this post I want to document the process in case I need to
reinstall any of it in the future.

<!-- more -->

**Note**: Not everything is built from source, the main modules I work with
are, but some dependencies are installed with pip.  Additionally, I assume
that you will be using python 2.7 and that the directory where you store source
code is SRC, the directory with virtualenvs is VENV and the name of the
virtualenv is myvenv (you should name yours something meaningful though).
Also, it is assumed that all <code>git clone ...</code> commands should be run
in the SRC directory.

#### Install virtualenv and virtualenv wrapper.  

There are a number of introductions on this.  The one
[here](http://www.thisisthegreenroom.com/2011/installing-python-numpy-scipy-matplotlib-and-ipython-on-lion/)
is good.

#### Create a virtualenv

virtualenvwrapper makes this really easy, see the documentation for 
instructions.  Name it whatever you'd like.  As long as it is active 
any modules you install (via pip or setup.py install) will be installed 
for that python.

#### IMPORTANT: Fix the python executable

virtualenv only copies the python executable, however, for the application
manager in OSX to recognize running python processes then, python must be 
called from an application bundle (also see pythonw in the python framework).  
This step is necessary so that figures opened with matplotlib can be brought 
to the front via cmd-tab (or clicking the icon in the dock).  If this step 
is not performed then matplotlib figures open behind all other windows and 
the only way to find them is to move all open windows.

``` bash
$ git clone git://github.com/gldnspud/virtualenv-pythonw-osx.git
$ python install_pythonw.py `which python`/../..
```

#### numpy

{% codeblock lang:bash %}
$ cd your/src/directory
$ git clone git://github.com/numpy/numpy.git  # or git pull
$ cd numpy
$ python setup.py build
$ python setup.py install
{% endcodeblock %}

#### nose

{% codeblock lang:bash %}
$ pip install nose
{% endcodeblock %}

#### Test numpy

``` bash
    python -c 'import numpy; numpy.test()'
```

#### scipy

{% codeblock lang:bash %}
$ cd your/src/directory
$ git clone git://github.com/scipy/scipy.git  # or git pull
$ cd scipy 
$ python setup.py build
$ python setup.py install
$ python -c 'import scipy; scipy.test()'
{% endcodeblock %}

#### readline

{% codeblock lang:bash %}
$ easy_install readline
{% endcodeblock %}
We use easy_install because readline won't be picked up if we install it
with pip.

#### Install other dependencies

{% codeblock lang:bash %}
$ pip install python-dateutil sphinx pygments tornado
{%endcodeblock %}

#### Install the ZMQ library 

Describing how is beyond the scope of this post,
but there is a lot of information available elsewhere.  

#### pyzmq

{% codeblock lang:bash %}
$ pip install pyzmq
{% endcodeblock%}

#### Install PySide system-wide

There is a dmg to do this, instructions for which can be found online.  
Then create a symbolic link in this virtualenv to the system installation
``` bash
    ln -s path-to-sys-PySide VENV/myvenv/lib/python2.7/site-packages/PySide
```

#### ipython  

By default the build script will use the system installation of python.  
Instead, use the following so that the correct version of python is used.
``` bash
    python setup.py build --executable "VENV/myvenv/bin/python" 
    python setup.py install
``` 
See <a href="https://github.com/ipython/ipython/issues/1171">this</a> discussion for more
information.  Alternatively <code>\`which python\`</code> can be 
used to specify the executable.

Also, install mathjax if you'd like for the notebook.  In an IPython session
run
``` python
from IPython.external.mathjax import install_mathjax
install_mathjax()
```

You should now have a working ipython with qtconsole and notebook
functionality (though you can't plot yet until we've installed matplotlib).

#### matplotlib

Building matplotlib on OSX is a pain.  Installing using pip might be best
``` bash
$ pip install -e https://github.com/matplotlib/matplotlib.git#egg=Package
```

However, if you really want to build matplotlib from source then
``` bash
$ git clone git://github.com/matplotlib/matplotlib.git
```
and follow the instructions in README.osx and make.osx

#### cython

I chose to build the latest stable version of cython rather than the master
branch since so many other modules use it.
``` bash
$ git clone git://github.com/cython/cython.git
$ make local
$ python setup.py install
$ python runtests.py -vv
```
Just a heads up that the tests take a *very* long time to run.

#### scikit-learn
``` bash
$ git clone git://github.com/scikit-learn/scikit-learn.git
$ make all
$ python setup.py install
```

**Update:** If building scikit-learn from source it is better to not install it
system-wide with the last line about, but rather add the directory to the
repository to your PYTHONPATH after the ```make all```.

#### pandas
First install the dependencies.

##### numexpr
``` bash
$ git clone git://github.com/erdc-cm/numexpr.git
$ python setup.py build
$ python setup.py install
$ python -c "import numexpr; numexpr.test()"
```

##### PyTables
Make sure that you have the HDF5 libraries installed on your system and
that they are on PATH.  Then, clone the repository from github and follow the
instructions reproduced below
``` bash
$ git clone git://github.com/PyTables/PyTables.git
$ python setup.py build_ext --inplace
$ python -c 'import tables; tables.test()'
$ python setup.py install
```

#### h5py
I've also found it useful to have h5py built as well for easily loading 
version 7.3 mat files.  Do this as follows
``` bash
$ git clone git://github.com/qsnake/h5py.git
$ cd h5py
$ python setup.py build --hdf5=/usr/local
$ python setup.py install
```
You should replace <code>usr/local</code> above with the path that contains
the <code>include</code>, <code>lib</code>, etc. directories of your HDF5
installation.

##### rpy2
``` bash
$ pip install rpy2
```

Now, we can build and install pandas.
``` bash
$ git clone git://github.com/pydata/pandas.git
$ python setup.py build_ext --inplace
$ nosetests pandas
$ python setup.py install
```

**Update:** Again, rather than installing you can just build in place and add
the path to the pandas repository to your PYTHONPATH.  This way every time you
pull a new version and build it you will see the effects immediately.

#### statsmodels
First we install the patsy module which statsmodels uses for formulas
``` bash
$ git clone git://github.com/pydata/patsy.git
$ python setup.py install
```
Then, statsmodels itself
``` bash
$ git clone git://github.com/statsmodels/statsmodels.git
$ python setup.py install
```

#### PyMC
``` bash
$ git clone git://github.com/pymc-devs/pymc.git
$ python setup.py config_fc --fcompiler gnu95 build
$ python setup.py install
$ python -c 'import pymc; pymc.test()'
```

#### bottleneck
This modulde contains cythonized versions of certain numpy functions to speed
them up including nansum, etc.  By now the drill is standard.
Beware, this takes a very long time to build on my laptop.
``` bash
$ git clone git://github.com/kwgoodman/bottleneck.git
$ python setup.py install
$ python -c 'import bottleneck; bottleneck.test()'
```

#### CythonGSL
This wraps the GSL library for use with Cython.  This is handy if you need
things like the gamma function, or you can use it to generate random numbers
(just be careful if you're also using np.random also) .
``` bash
$ git clone git://github.com/twiecki/CythonGSL.git 
$ cd CythonGSL
$ python setup.py build
$ python setup.py install
```

#### Finished

Ok, that's it, we have a pretty complete system for data analysis and research.
