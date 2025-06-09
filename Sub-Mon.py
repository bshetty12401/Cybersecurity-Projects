from scapy.layers.l2 import Ether,ARP,srp
from datetime import datetime


with open("white_list.txt", 'r') as f:
    trusted_mac = set(line.strip().lower() for line in f)
trusted_ip = "192.168.31.0/24"
eth = Ether(dst="ff:ff:ff:ff:ff:ff")
arp = ARP(pdst=trusted_ip)
packet = eth / arp
result = srp(packet, timeout=3, verbose=0)[0]


un = []
for sent, received in result:
    ip = received.psrc
    mac = received.hwsrc.lower()
    if mac not in trusted_mac:
        print("ALERT...!  \n unknown device detected with IP=",ip, "MAC=",mac)
        un.append((ip, mac))


if un:
    with open("unlog.txt", 'a') as l:
        for ip, mac in un:
            l.write(f"{datetime.now()} ip= {ip} mac= {mac}\n")

