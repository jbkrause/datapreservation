#!/usr/bin/env python3
help = """
Walks recursively the filesystem and:
- Detects BagIt bags
- Detected bags are checked
- Invalid bags are reported

Syntax 1: bagValidateRecursively.py
          -> starts recursively form current directory

Syntax 2: bagValidateRecursively.py directory1 [directory2 [directory3] ...]
          -> starts recursively form directory / directories given in argument


Requirements: Python3 , bagit.py .

Author : Jan Krause
Date   : 2017-07-25 (first version)
License: GNU-GPLv3, see: gpl-3.0.txt or http://www.gnu.org/licenses/gpl-3.0.html
"""

import bagit
import sys
import shutil
import os

# giving help if needed
if '-h' in sys.argv or '-help' in sys.argv or '--help' in sys.argv :
    print(help)
    sys.exit()

def check_if_is_bag(path):
    """If "path" is a bag returns True, otherwise returns False."""
    if os.path.isdir(path):
        if os.path.exists(path + os.sep + 'bagit.txt'):
            return True
        else:
            return False
    else:
        return False
            
def check_if_bag_is_valid(path):
    """If "path" is a valid bag returns True, otherwise returns False."""
    bag = bagit.Bag(path)
    if bag.is_valid():
        return True
    else:
        return False
# If onw argument
if len(sys.argv)>1:
    paths = sys.argv[1:] 
else:
    paths = [os.getcwd()]

n_folders = 0
n_bags = 0
n_bags_not_valid = 0
for path in paths:
    for root, subFolders, files in os.walk(path):
        n_folders += 1
        if check_if_is_bag(root):
            n_bags += 1
            if not check_if_bag_is_valid(root):
                n_bags_not_valid += 1
                print('BagIsNotValid: %s' % (root))
        for folder in subFolders:
            n_folders += 1
            fpath = root + os.sep + path
            if check_if_is_bag(fpath):
                n_bags += 1
                if not check_if_bag_is_valid(fpath):
                    n_bags_not_valid += 1
                    print('BagIsNotValid: %s' % (fpath))
            

print('\nSummary')
print('=======================')
print('Number of folders checked : %s' % (n_folders,))
print('Number of bags found      : %s' % (n_bags,))
print('Number of NOT VALID bags  : %s' % (n_bags_not_valid,))

