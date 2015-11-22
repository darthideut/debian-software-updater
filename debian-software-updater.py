#!/usr/bin/python
import os
print("Beginning the update process")
updates = os.popen("sudo apt-get update && sudo apt-get -s dist-upgrade").read()
print (updates)
#updates = "Hello /n World"
index1 = updates.find("upgraded,")
index2 = index1
while updates[index1] != "\n":
	index1 = index1 -1
print (updates [index1:index2])
print (index1)
print (index2)
number = updates [index1:index2]
numupdates = int(number.strip())
print numupdates
#os.system ("sudo apt-get dist-upgrade")
print("All finished, your computer is now ready to roll!")
