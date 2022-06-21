Appendix D: Customizing and Contributing to the Book
Note: the following instructions assume that you are connected to the Internet and that you have both the main and universe package repositories enabled. All unix shell commands are assumed to be running from your home directory ($HOME). Finally, any command that begins with sudo assumes that you have administrative rights on your machine. If you do not — please ask your system administrator about installing the software you need.

This book is free as in freedom, which means you have the right to modify it to suite your needs, and to redistribute your modifications so that our whole community can benefit.

That freedom lacks meaning, however, if you the tools needed to make a custom version or to contribute corrections and additions are not within your reach. This appendix attempts to put those tools in your hands.

Thanks!

Jeffrey Elkner
Governor’s Career and Technical Academy in Arlington
Arlington, Virginia

D.1. Getting the Source
This book is marked up in ReStructuredText using a document generation system called Sphinx.

The source code is located at https://code.launchpad.net/~thinkcspy-rle-team/thinkcspy/thinkcspy3-rle.

The easiest way to get the source code on an Ubuntu computer is:

run sudo apt-get install bzr on your system to install bzr.
run bzr branch lp:thinkcspy.
The last command above will download the book source from Launchpad into a directory named thinkcspy which contains the Sphinx source and configuration information needed to build the book.

D.2. Making the HTML Version
To generate the html version of the book:

run sudo apt-get install python-sphinx to install the Sphinx documentation system.
cd thinkcspy - change into the thinkcspy directory containing the book source.
make html.
The last command will run sphinx and create a directory named build containing the html version of the text.

Note: Sphinx supports building other output types as well, such as PDF. This requires that LaTeX be present on your system. Since I only personally use the html version, I will not attempt to document that process here.
