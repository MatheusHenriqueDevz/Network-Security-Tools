# DoS/Flood Traffic Monitor

> Módulo de segurança defensiva focado na análise volumétrica de tráfego de rede para detecção precoce de ataques de Negação de Serviço (DoS) e TCP Flooding.

---

## Arquivos do Módulo

* `traffic_analyzer.py`: Script principal de monitoramento e análise de tráfego.

## Engenharia de Detecção

O script atua como um sensor de rede passivo. Ele utiliza a biblioteca Scapy para inspecionar os cabeçalhos dos pacotes TCP em tempo real e opera com a seguinte lógica de detecção:

1. **Janela de Monitoramento:** O tráfego de entrada é analisado dentro de blocos de tempo predefinidos (ex: janela de 10 segundos).
2. **Threshold (Limite de Tolerância):** O sistema mapeia e contabiliza o volume de pacotes originados por cada endereço IP de forma isolada.
3. **Acionamento e Supressão de Ruído:** Se um IP específico ultrapassar o limite de pacotes configurado dentro da janela de tempo, um alerta de anomalia volumétrica é disparado. Imediatamente após a detecção, o mecanismo silencia os alertas subsequentes vindos desse mesmo IP, evitando que a tela do administrador sofra um flood de logs duplicados.

## Como Executar e Testar

Devido à captura de pacotes em baixo nível (Raw Sockets), o script exige elevação de privilégios para acessar a interface de rede do sistema operacional.

**Ambiente Linux:**
```bash
sudo python3 traffic_analyzer.py
```

**Ambiente Windows (CMD ou PowerShell elevado):**
```cmd
python traffic_analyzer.py
```

### Simulando um Ataque para Validação
Para testar o gatilho de detecção em ambiente de laboratório, você pode utilizar ferramentas de injeção de pacotes (como o `hping3` no Linux) a partir de uma máquina atacante direcionada ao IP do defensor:

```bash
sudo hping3 -S --flood -p 80 <IP_DO_DEFENSOR>
```