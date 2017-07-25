#!/usr/bin/env python3
help = """
Compares two BagIt bags and outputs:
- files deleted
- files added
- files modified

Note: It is required that the two bags use the same checksum algorithm.

Syntax : bagCompareTwo.py <Bag1> <Bag2> [<checksum-algorithm>]

    <Bag1> : path to bag 1
    <Bag2> : path to bag 2
    [<checksum-algorithm>] : optional: md5|sha1|sha256|sha512 (default is sha256)

Requirements: Python3

Author : Jan Krause
Date   : 2017-07-25 (first version)
License: GNU-GPLv3, see: gpl-3.0.txt or http://www.gnu.org/licenses/gpl-3.0.html
"""

import sys
import shutil
import os

# giving help if needed
if (len(sys.argv)==1) or '-h' in sys.argv or '-help' in sys.argv or '--help' in sys.argv :
    print(help)
    sys.exit()

pathToBag1 = sys.argv[1]
if pathToBag1.endswith(os.sep):
    pathToBag1 = pathToBag1[:-1]
if not pathToBag1.startswith(os.sep):
    os.getcwd() + os.sep + pathToBag1

pathToBag2 = sys.argv[2]
if pathToBag2.endswith(os.sep):
    pathToBag2 = pathToBag1[:-1]
if not pathToBag2.startswith(os.sep):
    os.getcwd() + os.sep + pathToBag2
    
# if the path is not a bag, we exit here
msg = '%s is not a bagit Bag' % (pathToBag1)
if not os.path.isdir(pathToBag1):
    print(msg)
    sys.exit()
elif not os.path.isfile(pathToBag1 + os.sep + 'bagit.txt' ):
    print(msg)
    sys.exit()
msg = '%s is not a bagit Bag' % (pathToBag2)
if not os.path.isdir(pathToBag2):
    print(msg)
    sys.exit()
elif not os.path.isfile(pathToBag2 + os.sep + 'bagit.txt' ):
    print(msg)
    sys.exit()

# if checksum given in command, we use it
checksum_type = 'sha256'
checksum_types = ['md5', 'sha1', 'sha256', 'sha512']
if len(sys.argv)==4:
    checksum_type = sys.argv[3]
    if checksum_type not in checksum_types:
        print('%s is not a valid checksum algorithm.' % (checksum_type))
        sys.exit()

manifest = 'manifest-%s.txt' % (checksum_type)

list1 = open(pathToBag1+os.sep+manifest).readlines()
list2 = open(pathToBag2+os.sep+manifest).readlines()
l1 = [l.replace('\n','') for l in list1]
l2 = [l.replace('\n','') for l in list2]

# counting files
s1 = set(l1)
s2 = set(l2)

# files that have changed
d1 = {}
for x in l1:
    s = x.split('  ')
    d1[s[1]]=s[0]
d2 = {}
for x in l2:
    s = x.split('  ')
    d2[s[1]]=s[0]
common_files = list( set(d1.keys()) & set(d2.keys()) )
n_changed = 0
for x in common_files:
    if not d1[x]==d2[x]:
        print('CHANGED:  %s' % (x,))
        n_changed+=1

# files deleted
in1_not2 = set(d1.keys()) - set(d2.keys())
for x in list(in1_not2):
     print('DELETED: %s' % (x,))

# files added
in2_not1 = set(d2.keys()) - set(d1.keys())
for x in list(in2_not1):
     print('ADDED:   %s' % (x,))

# numbers for the summary
n1 = len(l1)
n2 = len(l2)
l_in1_not2 = len(in1_not2)
l_in2_not1 = len(in2_not1) 

print( """
Summary
=======

Set1 : %s files
Set2 : %s files

Files removed  (in Set1 not in Set2)   : %s
Files added    (in Set2 not in Set1)   : %s
Files modified (checksum is different) : %s
""" % (n1, n2, l_in1_not2, l_in2_not1, n_changed) )
