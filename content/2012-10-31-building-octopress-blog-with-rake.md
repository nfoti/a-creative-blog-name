Title: Building octopress blog with rake
Date: 2012-10-31 18:39
Category: Octopress
Tags:
Slug: building-octopress-blog-with-rake
Author: Nick Foti


If you experience the symptoms in octopress issue
[#759](https://github.com/imathis/octopress/issues/759), i.e. ```rake
generate``` breaks because ```ffi``` tries to load ```lib.dylib```, you 
should check that the shell you are trying to build your blog from 

1. is not running a tmux session (the wrong ruby will be used)
2. does not have a python virtualenv active (the wrong python will be used)

This worked for me on OSX at least.
