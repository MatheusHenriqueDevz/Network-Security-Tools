# Port Scan Detector

> Módulo de Detecção de Intrusão (IDS) focado na identificação heurística de varreduras horizontais de reconhecimento (Port Scanning), acompanhado de um script ofensivo em Python para simulação e validação.

---

## Arquivos do Módulo

| Arquivo | Papel | Descrição |
| :--- | :--- | :--- |
| `scan_detector.py` | **Defesa (Sensor IDS)** | Monitora a rede passivamente e alerta sobre tentativas de varredura em andamento. |
| `scan.py` | **Ataque (Simulador)** | Dispara um *TCP Connect Scan* contra portas predefinidas de um alvo para acionar a detecção. |

## Engenharia de Detecção

O script de defesa utiliza a biblioteca Scapy para realizar a inspeção profunda de pacotes (DPI) em tempo real, aplicando a seguinte heurística para minimizar falsos positivos:

1. **Filtro de Handshake:** O sensor intercepta exclusivamente pacotes TCP com a flag `SYN` ativada (tentativa de início de conexão), ignorando tráfego estabelecido ou respostas.
2. **Estrutura de Dados de Conjunto:** O sistema armazena as portas alvo acessadas por cada IP de origem em conjuntos matemáticos (`sets`). Isso neutraliza técnicas de ofuscação onde o atacante envia centenas de pacotes para a mesma porta visando burlar contadores simples.
3. **Threshold Crítico:** Caso o volume de portas únicas testadas por um mesmo IP de origem ultrapasse o limite de tolerância (padrão configurado para 15 portas), o alerta de intrusão é gerado no console.

## Como Executar e Homologar

Para homologar a ferramenta em laboratório, utilize dois terminais operando simultaneamente. Devido à captura em baixo nível, o script de detecção requer elevação de privilégios.

### 1. Iniciar o Sensor de Defesa
**Ambiente Linux:**
```bash
sudo python3 scan_detector.py
```

**Ambiente Windows (CMD ou PowerShell elevado):**
```cmd
python scan_detector.py
```

### 2. Disparar a Varredura (Reconhecimento)
No segundo terminal, execute o simulador ofensivo e insira o IP alvo:
```cmd
python scan.py
```

> **Nota sobre Arquitetura Windows:** 
> O tráfego de loopback (`127.0.0.1` para si mesmo) é roteado internamente pelo núcleo do Windows e muitas vezes fica invisível para drivers físicos de captura como o Npcap. Para validar a detecção localmente no Windows, aponte o simulador ofensivo para um IP externo (ex: `8.8.8.8`) simulando tráfego de exfiltração, ou realize o ataque a partir de uma máquina física distinta na rede local.