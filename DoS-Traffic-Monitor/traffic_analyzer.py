from scapy.all import sniff, IP, TCP
from collections import defaultdict
import time

contador_pacotes = defaultdict(int)
tempo_inicial = time.time()

LIMITE_PACOTES = 100
JANELA_TEMPO = 10

def detectar_flood(pacote):
    global tempo_inicial
    
    if pacote.haslayer(IP) and pacote.haslayer(TCP):
        ip_origem = pacote[IP].src
        contador_pacotes[ip_origem] += 1

        if time.time() - tempo_inicial > JANELA_TEMPO:
            contador_pacotes.clear()
            tempo_inicial = time.time()

        if contador_pacotes[ip_origem] > LIMITE_PACOTES:
            print(f"[!!!] ALERTA DE DoS/FLOOD: IP {ip_origem} enviou tráfego excessivo!")
            contador_pacotes[ip_origem] = -500

        print(f"[*] Pacote capturado de {ip_origem} -> Porta {pacote[TCP].dport}")

print("Monitorando ataques de Negação de Serviço (DoS)...")
sniff(filter="tcp", prn=detectar_flood, store=0)