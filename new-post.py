"""
$ python blog-post.py 'Fight Club (1999)' movies --tags 2000-movies masterpiece
$ cat "~/projects/blog/posts/movies/Fight Club (1999).rst"
Fight Club (1999)
================

:date: 2012-04-09
:tags: masterpiece 2000-movies


$ python startpost.py 'I love Python' computing
$ cat "~/projects/blog/posts/computing/I love Python.rst"
I love Python
=============

:date: 2012-04-09

"""

import argparse
import datetime
import os
import subprocess
import shlex


def main():
    parser = argparse.ArgumentParser()
    parser.add_argument('title')
    parser.add_argument('-a', '--author', default="Nick Foti")
    parser.add_argument('-d', '--date')
    parser.add_argument('-c', '--category', default="")
    parser.add_argument('-t', '--tags', nargs='+')
    parser.add_argument('-s', '--slug')
    parser.add_argument('--path', default="content")

    args = parser.parse_args()

    if args.date is None:
        args.date = datetime.date.today()

    if args.slug is None:
        args.slug = args.title.lower().replace(" ", "-")

    filename = "%s.md" % (args.title,)
    filename = os.path.join(args.path, filename)
    filename = os.path.expanduser(filename)

    if args.tags is None:
        tag_str = ""
    else:
        tag_str = ", ".join(args.tags)

    if os.path.exists(filename):
        print("File already exists: %s" % (filename,))
    else:
        with open(filename, 'w') as f:
            f.write("Title: %s\n" % (args.title,))
            f.write("Date: %s\n" % (args.date,))
            f.write("Category: %s\n" % (args.category,))
            f.write("Tags: ")
            f.write(tag_str + "\n")
            f.write("Slug: %s\n" % (args.slug,))
            f.write("Author: %s\n" % (args.author,))
            f.write("\n\nYour post here!")

            print "Created new post at: %s" % (filename,)

if __name__ == "__main__":
    main()
