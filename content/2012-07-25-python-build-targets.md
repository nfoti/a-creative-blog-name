Title: Python build targets
Date: 2012-07-25 09:30
Category: Python
Tags:
Slug: python-build-targets
Author: Nick Foti

While writing the code for my
[last](/blog/2012/07/24/cythonizing-instance-methods/) 
post on Cython I encountered something strange regarding distutils.  The code
linked to the GSL library which on my machine (running OSX) is a unversal
library containing both 32- and 64-bit versions.  When I run
``` bash
$ python setup.py build_ext --inplace
```
distutils attempts to build 32- and 64-bit versions of the python
extensions.  Since I'm using a 64-bit version of Python I get a link error 
due to using the wrong architecture when the 32-bit version is built.

The simplest workaround I have found is as follows
``` bash
$ export ARCHFLAGS="-arch x86_64"
$ python setup.py build_ext --inplace
```
This causes only the 64-bit version of the extension to be built.
I'm sure there is a way to make distutils only build 64-bit versions by
default, but I haven't found it yet.  When I do I will update the post.
