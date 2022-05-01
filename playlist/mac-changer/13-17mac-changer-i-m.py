#!decode windows-1251

import subprocess
import re
def get_arguments():

def change_mac(interface, new_mac):

options = get_arguments()
    #change_mac(options.interface, options.new_mac)

ifconfig_result = subprocess.check_output(['ifconfig', options.interface])
print(ifconfig_result)


#python 13mac-changer.py -i eth0 -m 00:11:22:33:44:66

mac_address_search_result = re.search(r'\w\w:\w\w:\w\w:\w\w:\w\w:\w\w', ifconfig_result)

if mac_address_search_result:

    print(mac_address_search_result.group(0)) #iterate if need all group

else:
    print("[-] Could not MAC address")


