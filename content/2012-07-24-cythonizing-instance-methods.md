Title: Cythonizing instance methods
Date: 2012-07-24 20:45
Category: Python
Tags: cython, instance methods
Slug: cythonizing-instance-methods
Author: Nick Foti

A large amount of my work involves writing MCMC samplers.  The models I work
with have a lot of parameters and the samplers require a lot of state to be
recorded.  Normally, I stuff all of the parameters and state into a Python
class and implement the different steps of the sampler as instance methods.
One advantage of this approach is that the methods that perform the sampling
don't require many arguments.
Some of these methods run slowly due to for-loops that cannot be vectorized.
[Cython](http://www.cython.org) seems like a viable way to improve 
performance of these methods.

The simplest way to implement the sampling functions with Cython would be to 
define stand-alone functions in a .pyx file and pass all required data to 
the functions (the functions could then be added to the class if desired).
This defeats the purpose of using a class to store the state of the sampler 
though as we would need to deal with unwieldly function prototypes.  It would
be better to implement the instance method in a .pyx file (i.e. the first
argument to the function is a sampler object) and then add the instance 
method to the class.

In this post I describe how to do this for a contrived class
and record some helpful references for working with Cython.
This is nothing new, it is described on the 
[Cython Wiki](http://wiki.cython.org/FAQ/#HowdoIimplementasingleclassmethodinaCythonmodule.3F)
as well as
[here](http://bfroehle.com/2012/01/instance-methods-and-cython-functions/#more-121)
.  I have adapted my example from these sources.  Additionally, I provide an
example of calling a function from the Gnu Scientific Library ([GSL](http://www.gnu.org/software/gsl/))
from Cython code.

<!-- more -->

Let's define a (not very creative) simple class as in the following code
{% gist 3173622 basic.py %}

Suppose that (after profiling) we have determined that the (also uncreative) 
instance method `fun` is very inefficient and that we want to implement it 
with cython.  A first attempt at this is 
{% gist 3173622 cy1fun.pyx %}

To incorporate the Cython implementation of `fun` into `MyClass` we would like
to be able to do
``` python
MyClass.fun = cy1fun.fun
```
**This does not work as all Cython functions are unbound** (see 
[this](http://wiki.cython.org/FAQ/#HowdoIimplementasingleclassmethodinaCythonmodule.3F)).
The solution is to use the `MethodType` method of the `types` module shown 
here
{% gist 3173622 cy1.py %}

[This gist](https://gist.github.com/3173622) contains all of the code that is
used in this post.  The `setup.py` file that was used to build the code can be 
found there as well.  This is all we have to do to implement instance methods 
in Cython.

One dissatisfactory aspect of `cy1fun.pyx` is that we are just calling the 
Python function `scipy.special.gammaln`.  In `cy2fun.pyx` shown below I 
instead call the [GSL function](http://www.gnu.org/software/gsl/manual/html_node/Gamma-Functions.html) 
that computes the natural logarithm of the gamma function (based off of
[this](http://dpinte.wordpress.com/2010/04/22/interfacing-gsl-with-python-using-cython-comparison-with-weave/)).
I could have done the same with `np.random.rand` and used a GSL random number 
function, but I think the point has been made (see
[this](https://gist.github.com/757090) for how to use GSL random numbers in
Cython code). 
{% gist 3173622 cy2fun.pyx %}
and the corresponding Python code
{% gist 3173622 cy2.py %}
