# Installed the cowsay package using 'pip install cowsay'.
import cowsay  # Import cowsay. Documentation: https://pypi.org/project/cowsay/
import sys

if len(sys.argv) == 2:
    cowsay.trex("hello, " + sys.argv[1]) #outputs trex Ascii 

'''if len(sys.argv) == 2:
    cowsay.cow("hello, " + sys.argv[1])''' #outputs cow Ascii 
