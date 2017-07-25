# BagIt Data Preservation Tools

A set of utilities build on top of BagIt to simplify data preservation: batch creation, validation, update and comparison tools.

## Included utilities

* bagBatchCreate.py : **create** BagIt archives in batch
* bagValidateRecursively.py : **checks recursively archives** in a file system (starting for one or a list of folders)
* bagAddFiles.py : **adds or replaces files ** in an existing archive (checksums and metadata are update)
* bagRemoveFiles.py : **removes files** from an existing archive (checksums and metadata are update)
* bagCompareTwo.py : **compares two archives** and reports files that were added, deleted or modified

For more detailed information use the option -h with any of these command.

## Requirements

* Python >= 3
* [bagit.py](https://pypi.python.org/pypi/bagit/), installation: `pip install bagit`

# Compatibility

Any POSIX system (e.g. GNU/Linux, MacOS).