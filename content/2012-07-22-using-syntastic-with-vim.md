Title: Using syntastic with vim (and a vim bug on OSX)
Date: 2012-07-22 13:21
Category: Vim
Tags: vim, osx, syntastic
Slug: using-syntastic-with-vim-(and-a-vim-bug-on-osx)
Author: Nick Foti

Syntastic is a syntax checking plugin for vim that supports many different
languages.  I decided to give it a try in my current vim setup for my current
projects written in python.  Additionally, I decided to try out 
[flake8](http://pypi.python.org/pypi/flake8/), a wrapper for pyflakes, 
pep8 and mccabe.

Setting up flake8 is simple, just execute
``` bash
$ pip install flake8
```

To install syntastic follow the instructions on the github page 
[here](https://github.com/scrooloose/syntastic) (if you're not using pathogen,
to manage your vim plugins you should).  In your vimrc file add these lines
``` bash
let g:syntastic_check_on_open=1
let g:syntastic_python_checker="flake8"
```
See the README file for instructions on how to use syntastic.

#### Caveat

There is a bug in vim that causes a segfault when you execute wq in vim and
have a single python source file and the errors window open.  Supposedly this
was fixed in vim 7.3.449, however, I am using vim 7.3.608 and the bug is still
present.  Some simple workarounds are:
  
1. close the errors window before quitting vim
2. have multiple source files open 

The bug is still annoying though and will hopefully be fixed at some point.
