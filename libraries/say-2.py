import sys

#calls function from sayings.py file
from sayings import goodbye

if len(sys.argv) == 2:
    goodbye(sys.argv[1])

