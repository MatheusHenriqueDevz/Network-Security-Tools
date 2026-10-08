# Network Security Tools

Repositório destinado à consolidação de scripts e ferramentas para análise de tráfego, monitoramento de rede e detecção de ameaças. O objetivo principal é construir um arsenal focado em segurança defensiva utilizando Python.

## Ferramentas Disponíveis

### 1. DoS/Flood Traffic Monitor
Um detector de anomalias baseado em volume de tráfego, projetado para identificar ataques de Negação de Serviço (DoS) e TCP Flooding.

**Como funciona:**
O script utiliza a biblioteca Scapy para inspecionar os pacotes TCP da rede. Ele opera com uma lógica de janela de tempo (ex: 10 segundos) e um limite de requisições por IP de origem (threshold). Se um endereço IP enviar um volume de pacotes superior ao limite preestabelecido dentro dessa janela, o sistema identifica o tráfego anômalo e aciona um alerta de segurança no console, silenciando alertas duplicados logo em seguida para evitar poluição visual.

## Requisitos

* Python 3.x
* Scapy

Instalação das dependências:
`pip install scapy`

## Como Executar

A captura e inspeção de tráfego de rede em baixo nível exigem privilégios de administrador para acessar a interface física/virtual.

**No Linux:**
`sudo python3 traffic_analyzer.py`

**No Windows (CMD ou PowerShell como Administrador):**
`python traffic_analyzer.py`

---
**Aviso Legal:** Este projeto possui fins estritamente educacionais e acadêmicos. O uso destas ferramentas deve ser restrito a ambientes de laboratório (CTFs) ou redes nas quais você possui autorização explícita para realizar monitoramento.