from scapy.all import sniff, IP, TCP
from collections import defaultdict

portas_acessadas = defaultdict(set)
LIMITE_PORTAS = 15

def analisar_pacote(pacote):
    if pacote.haslayer(IP) and pacote.haslayer(TCP):
        ip_origem = pacote[IP].src
        porta_destino = pacote[TCP].dport
        flags_tcp = pacote[TCP].flags

        if flags_tcp == 'S':
            portas_acessadas[ip_origem].add(porta_destino)

            if len(portas_acessadas[ip_origem]) > LIMITE_PORTAS:
                print(f"[!!!] ALERTA: Port Scan detectado! O IP {ip_origem} testou {len(portas_acessadas[ip_origem])} portas diferentes!")
                portas_acessadas[ip_origem].clear()

print("Monitorando varredura de portas...")
sniff(filter="tcp", prn=analisar_pacote, store=0)