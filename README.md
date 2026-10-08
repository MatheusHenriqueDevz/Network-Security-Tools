# Network Security Tools

> Repositório central focado na construção, consolidação e versionamento de ferramentas modulares para segurança defensiva, análise de tráfego e detecção de anomalias em redes.

---

## Visão Geral

Este projeto atua como um ecossistema de scripts desenvolvidos em Python. O objetivo arquitetural é fornecer soluções leves, de rápida implantação e compatíveis com múltiplos sistemas operacionais (Linux e Windows), voltadas para o monitoramento de redes locais e ambientes de laboratório.

A arquitetura do repositório é modular. Cada ferramenta de segurança, IDS (Sistema de Detecção de Intrusão) ou script de análise possui seu próprio diretório contendo o código-fonte isolado e uma documentação específica detalhando seu mecanismo de funcionamento, heurística de detecção e instruções de uso.

## Requisitos Base do Ecossistema

A grande maioria das ferramentas deste repositório compartilha a mesma base tecnológica. Dependências específicas de cada script estarão documentadas em seus respectivos diretórios.

* **Linguagem:** Python 3.x+
* **Manipulação de Pacotes:** Biblioteca Scapy
* **Captura em Baixo Nível:** Npcap (Windows) ou libpcap (Linux)

**Instalação da dependência principal:**
```bash
pip install scapy
```

## Navegação e Execução

Para utilizar as ferramentas, navegue até o diretório desejado e consulte a documentação local. Devido à natureza das operações de rede em baixo nível, a execução dos scripts de captura exige elevação de privilégios no sistema operacional hospedeiro.

**Padrão de execução em ambiente Linux:**
```bash
sudo python3 <nome_do_script>.py
```

**Padrão de execução em ambiente Windows (CMD ou PowerShell elevado):**
```cmd
python <nome_do_script>.py
```

---

> **Aviso Legal:**
> Este projeto possui fins estritamente educacionais e acadêmicos. O uso destas ferramentas deve ser restrito a ambientes controlados, simulações (CTFs) ou infraestruturas nas quais o operador possui autorização explícita para realizar monitoramento e interceptação de tráfego.