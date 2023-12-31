    
import netifaces
print(netifaces.interfaces())
for i in netifaces.interfaces():

    print('\n**************Details of Interface - ' + i + ' *********************')

    print(netifaces.ifaddresses(i)[netifaces.AF_LINK])
    print(netifaces.ifaddresses(i)[netifaces.AF_LINK][0]['addr'])
    print(netifaces.ifaddresses(i)[netifaces.AF_INET][0]['addr'])
    print(netifaces.ifaddresses(i)[netifaces.AF_INET][0]['addr'])
#!/usr/bin/env python3

import netifaces

print(netifaces.interfaces())

for i in netifaces.interfaces():
    print('\n********Details of Interface - ' + i + ' ************')
    try:    # This is a new line, you also need to indent the code below this line by 4 whitespaces
        print((netifaces.ifaddresses(i)[netifaces.AF_LINK])[0]['addr']) # Prints the MAC address
        print((netifaces.ifaddresses(i)[netifaces.AF_INET])[0]['addr']) # Prints the IP address
#!/usr/bin/env python3

import netifaces

print(netifaces.interfaces())

for i in netifaces.interfaces():
    print('\n********Details of Interface - ' + i + ' ************')
    try:
        print((netifaces.ifaddresses(i)[netifaces.AF_LINK])[0]['addr']) # Prints the MAC address
        print((netifaces.ifaddresses(i)[netifaces.AF_INET])[0]['addr']) # Prints the IP address
    except:          # This is a new line
        print('Could not collect adapter information') # Print an error message
#!/usr/bin/env python3

import netifaces

print(netifaces.interfaces())

for i in netifaces.interfaces():
    print('\n****** details of interface - ' + i + ' ******')
    try:
        print('MAC: ', end='') # This print statement will always print MAC without an end of line
        print((netifaces.ifaddresses(i)[netifaces.AF_LINK])[0]['addr']) # Prints the MAC address
        print('IP: ', end='')  # This print statement will always print IP without an end of line
        print((netifaces.ifaddresses(i)[netifaces.AF_INET])[0]['addr']) # Prints the IP address
    except:          # This is a new line
        print('Could not collect adapter information') # Print an error message

