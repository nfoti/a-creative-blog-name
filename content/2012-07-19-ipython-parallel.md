Title: IPython parallel
Date: 2012-07-19 14:01
Category: Python
Tags: ipython
Slug: ipython-parallel
Author: Nick Foti

When I start IPython the first two commands I run are
``` python
%load_ext autoreload
%autoreload 2
```
which forces IPython to reload code before running it so that the newest
version is always used.
However, when developing code to run in parallel with the IPython.parallel 
module on a cluster started with ipcluster the code will invariably break.
The engines will continue using the old version until they are
explicitly reloaded using <code>%px reload(broken_module)</code>.  
Alternatively, we could use the autoreload extension
``` python
%px %load_ext autoreload
%px %autoreload 2
```
This will cause the engines to reload code before it tries to execute it.
All of this assumes that the engines are using the same filesystem as the
user's IPython session.
