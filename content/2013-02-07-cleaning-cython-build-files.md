Title: Cleaning Cython Build Files
Date: 2013-02-07 16:32
Category: Python
Tags: cython
Slug: cleaning-cython-build-files
Author: Nick Foti

Whenever I use a setup.py script to build Cython code a variety of files are
created including a `.so` file, one or more `.c` files and perhaps others.
Until today I would delete these by hand as I did not have the patience to
delve into what a setup.py file was actually doing and using the command
`python setup.py clean` never worked.

The code snippet below is my new skeleton setup.py file for Cython projects.The
notable features are the creation of the `cleanall` rule that deletes the files
that Cython creates, enforcing that the `--inplace` option is passed
to the `build_ext` rule and only building 64-bit targets (I have previously posted 
on how to do this with environment variables in the shell).

These ideas are based off of the setup.py file that can be found in tand always 
[this](https://groups.google.com/forum/?fromgroups=#!topic/cython-users/m22o0kq_EfM)
discussion.

``` python
import numpy as np

import os
import sys
import subprocess

from distutils.core import setup
from distutils.extension import Extension
from Cython.Distutils import build_ext


args = sys.argv[1:]

# Make a `cleanall` rule to get rid of intermediate and library files
if "cleanall" in args:
    print "Deleting cython files..."
    # Just in case the build directory was created by accident,
    # note that shell=True should be OK here because the command is constant.
    subprocess.Popen("rm -rf build", shell=True, executable="/bin/bash")
    subprocess.Popen("rm -rf *.c", shell=True, executable="/bin/bash")
    subprocess.Popen("rm -rf *.so", shell=True, executable="/bin/bash")

    # Now do a normal clean
    sys.argv[1] = "clean"

# We want to always use build_ext --inplace
if args.count("build_ext") > 0 and args.count("--inplace") == 0:
    sys.argv.insert(sys.argv.index("build_ext")+1, "--inplace")

# Only build for 64-bit target
os.environ['ARCHFLAGS'] = "-arch x86_64"

# Set up extension and build
cy_ext = Extension("cy_ext",
                   ["cy_ext.pyx"],
                   include_dirs=[np.get_include()],
                   #extra_compile_args=["-g"],
                   #extra_link_args=["-g"]
                   )

setup(cmdclass={'build_ext': build_ext},
      ext_modules=[cy_ext])
```
