#!/usr/bin/env python3
help = """
ADDS and/or REPLACES files in a BagIt bag. 
Bag informations and checksum manifests are updated.

Syntax : bagAddFiles.py <path-to-bag> <bag-sub-folder> <files-to-add>

   <path-to-bag>    : relative or absolute path to the bag
                      examples: "MyProject" , "Work/Myproject" 
   <bag-sub-folder> : bag folder in which the file(s) are added, 
                      relatively to the "data" folder
                      example: "Path/in/the/bag"
   <files-to-add>   : file(s) to add and/or replace
                      examples: "data.csv" , "data.*" 
                      note: if using * the double quotes are mendatory

Requirements: Python3 , bagit.py .

Author : Jan Krause
Date   : 2017-07-24 (first version)
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
 
# normalizing sub folder path
subFolder = sys.argv[2]
if subFolder.startswith(os.sep):
    subFolder = subFolder[1:]
if subFolder.endswith(os.sep):
    subFolder = subFolder[:-1]
if not subFolder == '':
    subFolder = os.sep + subFolder

# files to add to bag
fnames = glob.glob(sys.argv[3])

# if destination folder does not exist, we create it (recursively if necessary)
if not os.path.isdir(pathToBag + os.sep + 'data' +  subFolder):
    os.makedirs(pathToBag + os.sep + 'data' +  subFolder)

# copying file and updating bag
bag = bagit.Bag(pathToBag)
for fname in fnames:
    shutil.copyfile(fname, pathToBag + os.sep + 'data' +  subFolder + os.sep + os.path.basename(fname))
bag.save(manifests=True)

