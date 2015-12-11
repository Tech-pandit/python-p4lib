If you do any Python scripting of Perforce, then `p4lib.py` might be of interest to you. As mentioned above, not **all** Perforce client API commands are supported so you should make sure it has the ones you need first. The `p4lib.py` module docstring will tell you:

```
pydoc p4lib
```

All interaction is done via a "P4" instance:

```
>>> import p4lib
>>> p4 = p4lib.P4(OPTIONS)
>>> result = p4.COMMAND(OPTIONS)
```

For example, to open a file for editing:

```
>>> import p4lib
>>> p4 = p4lib.P4()
>>> p4.edit("cb.py")
[{'comment': 'opened for edit',
  'notes': [],
  'rev': 77,
  'depotFile': '//depot/main/Apps/Komodo-devel/src/codeintel/cb.py'}]
```

To verify that that file was actually opened:

```
>>> p4.opened("./...")
[{'rev': 77,
  'action': 'edit',
  'type': 'text',
  'depotFile': '//depot/main/Apps/Komodo-devel/src/codeintel/cb.py',
  'change': 'default'}]
```

The docstrings for each command should describe all you need to know to
use them. Either read `pydoc` output:

```
pydoc p4lib
```

or play around in the interactive shell:

```
>>> help(p4.edit)
```