from scapy.all import Ether, ARP, srp, sniff, conf

def get_mac(ip):
    
    p = Ether(dst='ff:ff:ff:ff:ff:ff')/ARP(pdst=ip)
    result = srp(p, timeout=3, verbose=False)[0]
    return result[0][1].hwsrc

def process(packet):
    # verificar se é um pacote ARP
    if packet.haslayer(ARP):
        # verificar se é uma resposta ARP (ARP reply)
        if packet[ARP].op == 2:
            try:
                # Pegar o verdadeiro MAC Address do remetente
                real_mac = get_mac(packet[ARP].psrc)
                # Pegar o MAC Address do pacote enviado para nós
                response_mac = packet[ARP].hwsrc
                # se forem diferentes, tem um ataque acontecendo
                if real_mac != response_mac:
                    print(f"[!] You are under attack, REAL-MAC: {real_mac.upper()}, FAKE-MAC: {response_mac.upper()}")
            except IndexError:
                # incapaz de encontrar o verdadeiro mac
                # pode ser um IP falso ou firewall está bloqueando pacotes
                pass

if __name__ == "__main__":
    import sys
    try:
        iface = sys.argv[1]
    except IndexError:
        iface = conf.iface
    sniff(store=False, prn=process, iface=iface)
