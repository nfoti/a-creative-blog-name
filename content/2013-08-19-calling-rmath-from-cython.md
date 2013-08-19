Title: Calling Rmath from cython (sometimes R just does it better)
Date: 2013-08-19 13:54
Category: Python
Tags: cython, Rmath
Slug: calling-rmath-from-cython
Author: Nick Foti

Recently I was writing some code that required the quantile function of the
chi-squared distribution.  There is a function in ccipy that implements this
function, however, calling a python function from cython is slow.  The scipy
implementation calls a function in the cephes library.  Unfortunately, scipy
compiles the cephes library code directly into the corresponding scipy
functions, so I had to build my own version of cephes.  Once I had done this I
went ahead and called the cephes function from some cython code only to be
plagued with numerical errors.  This was strange because the R implementation
of the chi-squared quantile function would yield non-zero results when the
cephes function would return zero.

This experience led me to wrap the Rmath library with cython to make the
functions available to cython code.  You need to build the Rmath library for
standalone use first (having R on your system is not enough), but then you will
be able to use nice R functions for your distributional needs.

See the [project page](http://github.com/nfoti/cythonRMath) for more 
information and examples.
