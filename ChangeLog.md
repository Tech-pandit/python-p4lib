## v0.9.5 ##

  * Fix a problem identified by "j w" where `p4.edit(<path>, change=123)` would fail if the path was already open and part of another pending change.
  * Fixes for 'p4 fstat' parsing if process output uses '\r\n' EOLs.
  * Fix http://bugs.activestate.com/show_bug.cgi?id=73103 (Perforce submit form does not match same submit from command line).

## v0.9.4 ##

  * Diff output parsing fix.
  * `p4 describe` output parsing fix.

## v0.9.3 ##

  * Add `p4.fstat()`.

## v0.9.2 ##

  * A fix from Aku Levola so that 'p4 diff -sn ./...' works with filenames that have a '#' in them.

## v0.9.1 ##

  * Fix shebang line in 'px'

## v0.9.0 ##

  * Change version attributes and semantics. Before: had a _version_ tuple. After: version is a string, version\_info is a tuple.

## v0.8.3 ##

  * The break-up-large-sets change in 0.8.2 introduced a bug w.r.t adding up retvals (doesn't work if retval is None). Fix that.

## v0.8.2 ##

  * Add somewhat of HACK fix for doing p4.opened(), p4.sync() and p4.resolve() with a large set of files. The test case is whether 'px backout 177241' on the ActiveState Perforce repository works. Before this the back would hang on Linux and Mac OS X.

## v0.8.1 ##

  * Add px.exe to the distro (and to repo) to fix install on Windows

## v0.8.0 ##

  * Move hosting of px/p4lib.py to trentm.com. Tweaks to associated bits (README.txt, etc.)
  * Fix 'px' usage of os.wait(). (Was this an os.wait() API change?)

## v0.7.2 ##

  * Avoid a possible hang when running commands use `*` in the filespec. See test/test\_hang.py for details.
  * Change _raw output to return unsplit output._

## v0.7.1 ##

  * Add '_raw' option to each P4 command to change the return value to be the unprocessed results from running p4._

## v0.7.0 ##

  * [incompatibility](Backward.md) Drop 'optv' method of passing p4 options to P4 constructor.  Instead use named keyword args. Also add optional keyword args to every P4 command to allow overriding the instances p4 options for a specific command.  This may break `p4lib.P4()` usage. To quickly convert one may use this pattern: Change usages of `p4lib.P4(optv-argument)` to `p4 = p4lib.P4( **p4lib.parseOptv(self.__p4optv) )`

## v0.6.8 ##

  * Add interfaces in p4lib.py to 'p4 label', 'p4 labels', 'p4 flush', 'p4 branch', 'p4 branches'.
  * Fix bug in p4lib.py interface to 'p4 have' where files containing " - " could not be handled.

## v0.6.7 ##

  * Add interface to 'p4 client' and 'p4 clients' in p4lib.py.
  * Fix bugs in 'px genpatch' where opened files without changes or non-existant added files could not be handled.

## v0.6.6 ##

  * first public release