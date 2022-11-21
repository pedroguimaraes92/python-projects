from scapy.all import ARP, Ether, srp

target_ip = "192.168.1.1/24"
# Destino do IP
# Criar pacote ARP
arp = ARP(pdst=target_ip)
# Criar o pacote broadcast Ether
# ff:ff:ff:ff:ff:ff = broadcasting
ether = Ether(dst="ff:ff:ff:ff:ff:ff")
# Empilhar
packet = ether/arp

result = srp(packet, timeout=3, verbose=0)[0]

# Lista dos clientes
clients = []

for sent, received in result:
    # Pra cada resposta, adicionar ip e mac address para lista 'clients'
    clients.append({'ip': received.psrc, 'mac': received.hwsrc})

# print clients
print("Available devices in the network:")
print("IP" + " "*18+"MAC")
for client in clients:
    print("{:16}    {}".format(client['ip'], client['mac']))
