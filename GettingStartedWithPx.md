As with the `p4` command itself, the built-in documentation for `px` is pretty good. (Please add an issue if you find this isn't true!) `px` should feel and act like using `p4`.  To see the `px` extensions, enter `px help px`:

```
$ px help px
'px' entensions to 'p4':

px --help
    Add px-specific help output to the usual 'p4 -h' and 'p4 -?'.
    See 'px help usage'.

px -V, --version
    Print px-specific version information in addition to the usage
    'p4 -V' output.  See 'px help usage'.

px -g ...
    Format input/output as *un*marshalled Python objects. Compare to
    the usual 'p4 -G ...'.  See 'px help usage'.

px annotate ...
    Identify last change to each line in given file, like 'cvs
    annotate' or 'p4pr.pl'.  See 'px help annotate'.

px backout ...
    Provide all the general steps for rolling back a perforce
    change as described in Perforce technote 14.  See 'px help
    backout'.

px changes -d ...
    Print the full 'p4 describe -du' output for each listed change.
    See 'px help changes'.

px diff -sn --skip ...
    List local files not in the p4 depot. Useful for importing new
    files into a depot via 'px diff -sn --skip ./... | px -x - add'.
    See 'px help diff'.

px diff -c <change> ...
    Limit diffing to files opened in the given pending change.  See
    'px help diff'.

px genpatch [<change>]
    Generate a patch (usable by the GNU 'patch' program) from a
    pending or submitted chagelist.  See 'px help genpatch'.
```

Personally, the extensions that I find most useful are:

  * `px changes -d`

> This is very useful for grepping through a lot of changes to a particular file or area. For example: `px changes -d ./... | less`

  * `px backout CHANGENUM`

> The full procedure for backing out a check-in to Perforce is described in [Tech Note 14](http://www.perforce.com/perforce/technotes/note014.html). This can be tedious to work through. `px backout` does a decent job of handling all these steps for you.

  * `px diff -sn`

> Ever want to know what new files in your client area you've forgotten to `p4 add`. This will tell you.

> Also, this command simplifies the instructions for [Perforce Tech Note 12](http://www.perforce.com/perforce/technotes/note012.html) for importing a directory tree and part of [Tech Note 2](http://www.perforce.com/perforce/technotes/note002.html) for working offline to not have to give platform-specific commands:
```
px diff -sn ./... | px -x - add
px diff -sd ./... | px -x - delete
px diff -se ./... | px -x - edit
```