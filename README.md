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

For this to work, please set your github remote 'upstream' to 
'git@github.com:numfocus/numfocus.org.git'.

Dependecies
===========
Note that you have to have the following packages installed for everything to work properly:

* pelican
* typogrify
