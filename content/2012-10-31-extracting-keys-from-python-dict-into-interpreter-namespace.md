Title: Extracting keys from Python dict into interpreter namespace
Date: 2012-10-31 10:36
Category: Python
Tags: ipython
Slug: extracting-keys-from-python-dict-into-interpreter-namespace
Author: Nick Foti

I run a lot of experiments in ipython, the results of which I pickle and save
to disk.  When I reload the results with pickle I end up with a dict whose keys
are the variable names that I saved.  It is tedious to have to reference these
values through the dict, what I would really like is behavior like ```load```
in Matlab such that when I load the pickle file the variables are available in
the global namespace.

I figured this was possible in Python but had no idea how to do this until 
I found
[this](http://stackoverflow.com/questions/4357851/creating-or-assigning-variables-from-a-dictionary-in-python) 
question on stack overflow that answers the question.

``` python Load pickle file variables into global namespace
    try:
        import cPickle as pickle
    except ImportError:
        import pickle

    def loadvars(filename, namespace=None):
        if namespace is None:
            namespace = globals()
        
        with open(filename, 'r') as f:
            d = pickle.load(f)
            namespace.update(d)
```

If you try to put this code in a module and import the function then you will
have to pass ```globals()``` to the function explicitly as the ```globals()```
in the function is not the IPython global namespace.  However, you can put the
above code inside your ~/.ipython/profile_PROFILE/startup/startup.ipy file and
it will work as expected.  PROFILE is the name of the profile that you plan to
start IPython with.
