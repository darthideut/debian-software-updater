#!/usr/bin/python
import os
print("Beginning the update process")
os.system ("sudo apt-get update")
os.system ("sudo apt-get dist-upgrade")
print("All done, your system is now up to date!")
