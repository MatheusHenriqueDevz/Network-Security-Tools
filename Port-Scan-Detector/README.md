# Port Scan Detector

Este módulo contém um Sistema de Detecção de Intrusão, focado na identificação de varreduras horizontais de portas na rede, acompanhado de um script simulador de ataque (TCP Connect) para validação da ferramenta.

## Arquivos do Projeto

* `scan_detector.py`: O script de defesa (Monitor/IDS).
* `scan.py`: O script de ataque (Simulador de Port Scan).

## Como Funciona a Detecção

O detector utiliza a biblioteca Scapy para monitorar o tráfego de rede em busca de pacotes TCP com a flag `SYN` ativada. Para evitar falsos positivos com tráfego legítimo, o script adota a seguinte lógica:
1. Extrai o IP de origem e a porta de destino de cada pacote SYN.
2. Armazena as portas acessadas por cada IP em uma estrutura de dados de conjunto (`set`), que ignora tentativas repetidas na mesma porta.
3. Se um mesmo IP tentar iniciar conexões com portas diferentes que ultrapassem o limite de tolerância estabelecido (ex: 15 portas), o sistema aciona um alerta crítico de segurança no console.

## Como Executar e Testar

Para realizar o teste de validação, são necessários dois terminais rodando simultaneamente. O script de detecção requer privilégios administrativos para capturar pacotes na interface de rede.

**1. Iniciando a Defesa (Terminal 1 - Administrador):**
No Linux:
`sudo python3 scan_detector.py`

No Windows (CMD/PowerShell):
`python scan_detector.py`

**2. Iniciando o Ataque (Terminal 2):**
Execute o simulador e insira um IP alvo (pode ser um IP externo ou outra máquina da rede local):
`python scan.py`

*Nota: Em sistemas Windows, o tráfego de loopback (127.0.0.1 para 127.0.0.1) é processado internamente e não passa pela interface de captura física do Npcap. Para testar localmente no Windows, aponte o simulador para um IP externo (ex: 8.8.8.8) para simular uma exfiltração/reconhecimento, ou ataque a partir de uma máquina física distinta.*