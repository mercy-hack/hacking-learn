from socket import timeout
from tabnanny import verbose
import scapy.all as scapy

def scan(ip):
#    scapy.arping(ip)
    arp_request = scapy.ARP(pdst=ip)
    broadcast = scapy.Ether(dst='ff:ff:ff:ff:ff:ff')
    arp_request_broadcast = broadcast/arp_request
    answered_list = scapy.srp(arp_request_broadcast, timeout=1, verbose=False)[0] #return two couple list
    
    #print('IP\t\t\tMAC Address\n--------------------------------------') --1
    
    clients_list = []
    
    for element in answered_list:
        client_dict = {'ip': element[1].psrc, 'MAC': element[1].hwsrc}
        #print(element[1].psrc + '\t\t' + element[1].hwsrc) --1
        clients_list.append(client_dict)
        #print('--------------------------------------') --1
    return clients_list

    #print(answered_list.summary())

def print_result(result_list):
    print('IP\t\t\tMAC Address\n--------------------------------------')
    for client in result_list:
        print(client['ip']+'\t\t'+client['MAC'])


scan_result = scan('192.168.8.1/24')
print_result(scan_result)



