#!/usr/bin/env python3
help = """
Transforms all directories of the working directory into BagIT bags (using sha256 checsums).
Hidden directories (i.e. directories starting with "." are skipped).

Syntax : bagBatchCreate.py

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

checksum = 'sha256'
ls = os.listdir()

for f in ls:
    if os.path.isdir(f):
        if not f[0]=='.':
            print('\nCreating bag for: %s' % (f,))
            print('======================================')
            os.system('bagit.py --%s "%s"' % (checksum, f))
            print('======================================')

