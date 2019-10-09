#!/usr/bin/env python
# -*- coding: utf-8 -*- #

from __future__ import unicode_literals
from jsmin import jsmin
import sass, os

AUTHOR = 'Pouya Abbassi'
SITENAME = 'PouyaCode'
DESCRIPTION = 'A place for my thoughts.'
SITEURL = 'http://localhost:8000'

PATH = 'content'

TIMEZONE = 'Asia/Tehran'

DEFAULT_LANG = 'en'

# Feed generation is usually not desired when developing
FEED_ALL_ATOM = 'feeds/all.atom.xml'
CATEGORY_FEED_ATOM = 'feeds/{slug}.atom.xml'
TRANSLATION_FEED_ATOM = None
AUTHOR_FEED_ATOM = None
AUTHOR_FEED_RSS = None

# Blogroll
BLOGROLL = (
        ('lxSameer', 'https://lxsameer.com'),
        ('Yottanami', 'http://blog.yottanami.com/'),
        )

# Social widget
SOCIAL = (
        ('Gitlab', 'https://gitlab.com/pouya-abbassi/', 'fab fa-gitlab'),
        ('Devheroes', 'https://devheroes.club/?u=pouya-abbassi', 'fas fa-hands-helping'),
        ('Goodreads', 'https://www.goodreads.com/pouyacode', 'fab fa-goodreads'),
        ('Atom feed', 'feeds/all.atom.xml', 'fas fa-rss'),
        )

DEFAULT_PAGINATION = 10

# Uncomment following line if you want document-relative URLs when developing
RELATIVE_URLS = False

# Theme
THEME = 'theme'

PLUGIN_PATHS = ['pelican-plugins']
PLUGINS      = ['sitemap', 'readtime', 'share_post', 'neighbors', 'optimize_images', 'optimize_files']
SITEMAP      = {'format': 'xml'}

# Sass compile
with open(THEME + '/static/css/bulma.css', 'w') as css:
    style = sass.compile(filename=('sass/bulma.sass'), output_style='compressed')
    css.write(style)
    css.close()

# JS minifier
with open('theme/static/js/main.js') as js_file:
    with open('theme/static/js/main.min.js','w') as min_file:
            minified = jsmin(js_file.read())
            min_file.write(minified)
            min_file.close()

