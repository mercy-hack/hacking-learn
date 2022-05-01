from concurrent.futures import process
import queue
import netfilterqueu

def proecss_packet(packet):
    print(packet)
    packet.drop()

queue = netfilterqueu.NetfilterQueue()
queue.bind(0, process_packet)
queue.run