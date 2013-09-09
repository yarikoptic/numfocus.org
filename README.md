numfocus.org
============

NumFOCUS Website Revamp Project

This is the source of the pelican-based NumFOCUS.org site.  These pages should be generated from these 
sources and then pushed to the actual site.

The site is based on Pelican:  http://docs.getpelican.com/en/3.2/

Building the Site
=================
Use the folowing to build the and serve the site locally:

    make devserver

Use the following to push the results up to github:

    make github

For this to work, please set your github remote 'upstream' to 'git@github.com:scopatz/numfocus.org.git'

Dependecies
===========
Note that you have to have the following packages installed for everything to work properly:

* pelican
* typogrify


Adding Content
==============

The site is organized as a blog with a set of post categories.  Each post
categorized post will show up in the news feed as well as in its designated
category.  To add new content, crate a .rst file in the appropriate category
directory in contet.  For example, to add the minutes from the most recent
board meeting, you should add a file to the "Board Meetings" directory.  Posts
should provide a title and a date i.e

    inSCIght
    ########
    :date: 07-05-2013

Posts can optionally provide a `:slug:` field.  The slug is used to generate a
direct link to the post.  If no slug is provided, the title ("inSCIght" in the
above example) will be used.


Adding Images
=============

Images should be added to the with `content/images` directory.  If the filename is
`spam.jpg`, the path image path in ReST is: `|filename|/images/spam.jpg`  The funny
`|filename|` syntax is how Pelican manages internal links.  The `content` directory
forms the root for paths.
