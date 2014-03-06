#!/usr/bin/python
import sys
import re

if len(sys.argv) > 1:
    bigString = sys.argv[1]
    regex = sys.argv[2]

    print(' '.join(re.findall(regex, bigString)))
