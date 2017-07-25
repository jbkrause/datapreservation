#!/usr/bin/env python3
help = """
REMOVES files from a BagIt bag. Bag informations and checksum manifests are updated.

Syntax : bagRemoveFiles.py <path-to-bag> <files-to-remove>

   <path-to-bag>    : relative or absolute path to the bag
                      examples: "MyProject" , "Work/Myproject" 
   <files-to-remove>: file(s) to remove
                      examples: "data.csv" , "measurements/data.csv" , "data.*" 
                      Notes:  - if using * the double quotes are mendatory
                              - path to files are given relatively to the "data" folder

Requirements: Python3 , bagit.py .

Author : Jan Krause
Date   : 2017-07-25 (first version)
License: GNU-GPLv3, see: gpl-3.0.txt or http://www.gnu.org/licenses/gpl-3.0.html
"""

import bagit
import sys
import os
import shutil
import glob

# giving help if needed
if (len(sys.argv)==1) or '-h' in sys.argv or '-help' in sys.argv or '--help' in sys.argv :
    print(help)
    sys.exit()

# computing bag path
pathToBag = sys.argv[1]
if pathToBag.endswith(os.sep):
    pathToBag = pathToBag[:-1]
if not pathToBag.startswith(os.sep):
    os.getcwd() + os.sep + pathToBag
    
# if the path is not a bag, we exit here
msg = '%s is not a bagit Bag' % (pathToBag)
if not os.path.isdir(pathToBag):
    print(msg)
    sys.exit()
elif not os.path.isfile(pathToBag + os.sep + 'bagit.txt' ):
    print(msg)
    sys.exit()

# files to add to bag
fnames = glob.glob(sys.argv[2])

# removing files and updating metadata
bag = bagit.Bag(pathToBag)
for fname in fnames:
    os.remove(pathToBag + os.sep + 'data' + os.sep + fname)
bag.save(manifests=True)

