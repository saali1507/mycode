#!/usr/bin/env python3

# import new code
import netifaces
print(netifaces.interfaces())

# create for loop, and iterate over interfaces
for i in netifaces.interfaces():
    print('\n**************Details of Interface - ' + i + ' *********************')
    print(netifaces.ifaddresses(i))

