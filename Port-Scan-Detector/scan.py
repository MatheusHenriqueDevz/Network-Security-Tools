import socket
import time

ip_alvo = input("Digite o IP alvo (ou pressione Enter para testar a própria máquina): ")

if not ip_alvo:
    ip_alvo = "127.0.0.1"

portas_alvo = [21, 22, 23, 25, 53, 80, 110, 135, 139, 443, 445, 1433, 3306, 3389, 8080, 8443]

for porta in portas_alvo:
    s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    s.settimeout(0.1)
    
    resultado = s.connect_ex((ip_alvo, porta))
    
    if resultado == 0:
        print(f"[+] Porta {porta}: ABERTA")
    else:
        print(f"[-] Porta {porta}: Fechada/Filtrada")
        
    s.close()
    time.sleep(0.05)

print("Avada Kedavra!")