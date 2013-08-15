#!/usr/bin/env python
# -*- coding: utf-8 -*- #
from __future__ import unicode_literals

AUTHOR = u'Nick Foti'
SITENAME = u'Research Blog'
SITEURL = ''

TIMEZONE = 'America/New_York'

DEFAULT_LANG = u'en'

DEFAULT_DATE = u'fs'

THEME = "/Users/nfoti/src/pelican-themes/pelican-octopress-theme"

PLUGIN_PATH = "/Users/nfoti/src/pelican-stuff/pelican-plugins"
PLUGINS = ['liquid_tags.img', 'liquid_tags.video',
           'liquid_tags.include_code', 'liquid_tags.notebook']
CODE_DIR = 'code'
NOTEBOOK_DIR = 'notebooks'
STATIC_PATHS = ['images', 'code']

try:
    EXTRA_HEADER = open('_nb_header.html').read().decode('utf-8')
except IOError:
    pass

# Feed generation is usually not desired when developing
FEED_ALL_ATOM = None
CATEGORY_FEED_ATOM = None
TRANSLATION_FEED_ATOM = None

# Blogroll
LINKS = (('Pelican', 'http://getpelican.com/'),
         ('Python.org', 'http://python.org/'),
         ('Jinja2', 'http://jinja.pocoo.org/'),
         ('You can modify those links in your config file', '#'),)

# Social widget
SOCIAL = (('github', 'http://github.com/nfoti'),)

DEFAULT_PAGINATION = 5

GITHUB_URL = "http://github.com/nfoti/"

# Uncomment following line if you want document-relative URLs when developing
#RELATIVE_URLS = True
