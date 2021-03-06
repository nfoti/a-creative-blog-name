#!/usr/bin/env python
# -*- coding: utf-8 -*- #
from __future__ import unicode_literals

import os

AUTHOR = u'Nick Foti'
SITENAME = u'(A Creative Blog Name Here)'
SITESUBTITLE = u'Code, math, and other things I find useful'
SITEURL = 'http://github.io/nfoti/a-creative-blog-name'

TIMEZONE = 'US/Pacific'
DEFAULT_LANG = u'en'

DEFAULT_DATE_FORMAT = u'%d %B %Y %I-%M %p'
DEFAULT_DATE = u'fs'

DEFAULT_PAGINATION = 10

ARTICLE_URL = 'posts/{date:%Y}/{date:%m}/{date:%d}/{slug}/'
ARTICLE_SAVE_AS = 'posts/{date:%Y}/{date:%m}/{date:%d}/{slug}/index.html'

# 'Tags' requres nfoti/tagpage-noside branch of pelican-octopress-theme
MENUITEMS = [('Archives', SITEURL + '/archives.html'),
             ('Tags', SITEURL + '/tags.html'),
             ('Home Page', 'http://nfoti.github.io')]

THEME = "/Users/nfoti/src/pelican-themes/pelican-octopress-theme"
PLUGIN_PATH = "/Users/nfoti/src/pelican-stuff/pelican-plugins"
PLUGINS = ['liquid_tags.img', 'liquid_tags.video',
           'liquid_tags.include_code', 'liquid_tags.notebook']
CODE_DIR = 'code'
NOTEBOOK_DIR = 'notebooks'
STATIC_PATHS = ['images', 'code', 'notebooks']

try:
    EXTRA_HEADER = open('_nb_header.html').read().decode('utf-8')
except IOError:
    pass

# Feed generation is usually not desired when developing
FEED_ALL_ATOM = None
CATEGORY_FEED_ATOM = None
TRANSLATION_FEED_ATOM = None

# Blogroll
#LINKS = (('Pelican', 'http://getpelican.com/'),
#         ('Python.org', 'http://python.org/'),
#         ('Jinja2', 'http://jinja.pocoo.org/'),
#         ('You can modify those links in your config file', '#'),)

# Social widget
SOCIAL = (('github', 'http://github.com/nfoti'),)
GITHUB_URL = "http://github.com/nfoti/"
FACEBOOK_LIKE = False
TWITTER_TWEET_BUTTON = False
TWITTER_LATEST_TWEETS = False
TWITTER_FOLLOW_BUTTON = False

# Search
SEARCH_BOX = True

# Uncomment following line if you want document-relative URLs when developing
#RELATIVE_URLS = True
