#!/usr/bin/python3

import os
import sys

# mes arguments
print(sys.argv)

# / unix...
# \ windows
#
# mal l'utiliser
# path = "/home/kit"

print(os.path.join("home", "kit"))
dir(os)
for x in dir(os):
    if "dir" in x:
        print(x)

# c'est du python2 print sans les ()
#        print x
