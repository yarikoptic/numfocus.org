#!/usr/bin/env python
# -*- coding: utf-8 -*- #
from __future__ import unicode_literals


#AUTHOR = u'NumFOCUS Foundation'
SITENAME = u'NumFOCUS Foundation'
SITEURL = ''

TIMEZONE = 'Europe/Paris'

DEFAULT_LANG = u'en'

THEME = u'theme'

# Put Articles in News
ARTICLE_DIR = 'articles'
ARTICLE_URL = 'news/{date:%Y}/{date:%m}/{date:%d}/{slug}/'
ARTICLE_SAVE_AS = 'news/{date:%Y}/{date:%m}/{date:%d}/{slug}/index.html'

# Put Pages at top-level
PAGES_DIR = 'pages'
PAGES_URL = '{slug}.html'
PAGES_SAVE_AS = '{slug}.html'

CATEGORY_URL = 'news/categories/{slug}.html'
CATEGORY_SAVE_AS = 'news/categories/{slug}.html'

TAG_URL = 'news/tags/{slug}.html'
TAG_SAVE_AS = 'news/tags/{slug}.html'

AUTHOR_URL = 'news/author/{slug}.html'
AUTHOR_SAVE_AS = 'news/author/{slug}.html'


# Feed generation is usually not desired when developing
FEED_ALL_ATOM = None
CATEGORY_FEED_ATOM = None
TRANSLATION_FEED_ATOM = None

# not Blogroll
#LINKS =  (('Pelican', 'http://getpelican.com/'),
#          ('Python.org', 'http://python.org/'),
#          ('Jinja2', 'http://jinja.pocoo.org/'),
#          ('You can modify those links in your config file', '#'),)

# Social widget
SOCIAL = (
    ('mailto:numfocus+subscribe@googlegroups.com', 'Join our mailing list'),
    ('https://groups.google.com/forum/#!forum/numfocus', 'Read the archives'),
)

GITHUB_URL = 'https://github.com/numfocus'
TWITTER_URL = 'https://twitter.com/numfocus'
GOOGLEPLUS_URL = 'https://plus.google.com/communities/100008130850352595608'

MENUITEMS = []
# MENUITEMS = [('About', 'about.html'),
#              ('Projects', 'projects.html'),
#              ('Board', 'board.html'),
#              ('Membership', 'membership.html'),
#              ('Fellowships', 'fellowships.html'),
#              ('Donations', 'donations.html'),
#              ('Sponsors', 'sponsors.html'),
#              ('Contact', 'contact.html'),
#              ]

DIRECT_TEMPLATES = ('news/tags', 'news/categories', 'news/archives', 'news/index')

#EXTRA_TEMPLATE  _PATHS = ('templates',)
PAGINATED_DIRECT_TEMPLATES = ['news/index']
DEFAULT_PAGINATION = 12

# the intended way to add articles to the news feed is to add them to a
# pre-defined category (i.e. it has a directory) or to explicitly give it a
# category
# the default category is "nofeed"
DEFAULT_CATEGORY = 'nofeed'

TYPOGRIFY = True

MARKUP = ('rst', 'md', 'html')

# Uncomment following line if you want document-relative URLs when developing
RELATIVE_URLS = True
#RELATIVE_URLS = False

STATIC_PATHS = [
    'images',
    'pdfs',
    'media',
#    'johnhunter/index.html',
    ]
