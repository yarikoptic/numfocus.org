there is something broken in how pelican translates image paths.  The path
static/images/foo.jpg

should turn into:
	http://example.com/static/iamges/foo.jpg

but for files in the *pages* dir, they become

	http://example.com/pages/static/iamges/foo.jpg

note the extra pages level.  For this reason, paths to images must prepend a .. to the path.  ie

../static/images/foo.jpg
