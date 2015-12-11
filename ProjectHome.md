# Note: This project has been moved to [trentm/python-p4lib on GitHub](https://github.com/trentm/python-p4lib). #

**Note: I'm currently still in the process of moving this project here. Not everything is up yet.**

This project provides two things: the `p4lib.py` Python module and the `px` command-line tool.


# p4lib.py #

`p4lib.py` is a Python interface to the Perforce client application.  If you are a Python programmer and script Perforce you might find this module helpful. Currently, most common commands (though your definition of "common" may differ from mine) are supported. The `p4lib.py` module docstring says exactly which -- read it TODO [/url/to/p4lib.py here] or run:

> pydoc p4lib

Note: `p4lib.py` is a pure-Python wrapper that shells-out to `p4`. I.e. it is not using Perforce's C++ `P4Client` API. This has the benefit of not requiring binary builds (hence works on a lot of platforms easily) and the drawback of not automatically supporting the whole set of `p4` client commands.

An unrelated benefit of `p4lib.py` is that it attempts to provide a somewhat Pythonic interface to the p4 client commands. YMMV.

See GettingStartedWithP4lib for more.

# px #

Perforce is a source code control system (like CVS or Subversion).  The standard command-line command for working with Perforce is `p4`.  `px` is a wrapper around `p4`.  It provides all the functionality of p4 (defering work to it) plus it extends some standard p4 commands and adds a few new ones. If you are a Perforce user you might find these extensions useful.

See GettingStartedWithPx for more.


# Project Status #

`p4lib.py` is mature (though, as mentioned above, it might not cover some of the p4 commands you care about). It has been heavily used in the commercial [Komodo IDE](http://www.activestate.com/komodo/) product for a number of 3 years.

`px` hasn't been updated in a while so is likely showing its age in some places (e.g. 'px annotate' was added before p4 grew an annotate command).  That said, the commands it **does** add to `p4` should still work well.