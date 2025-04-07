# CrewAI Generator

## Visão Geral

O **CrewAI Generator** é uma aplicação web desenvolvida com Streamlit que automatiza a criação de arquivos de configuração para projetos utilizando o framework CrewAI. A aplicação permite que usuários, mesmo sem experiência técnica profunda, possam gerar rapidamente a estrutura inicial de um projeto CrewAI através de uma descrição textual.

## Funcionalidades

- **Geração Automatizada**: Cria os três arquivos essenciais, agents.yml, task.yml e crew.py para um projeto CrewAI a partir de uma descrição em linguagem natural
- **Interface Amigável**: Design intuitivo com instruções claras e feedback visual
- **Exportação Facilitada**: Empacota automaticamente os arquivos gerados em um arquivo ZIP pronto para download

## Arquitetura

### Componentes Principais

A aplicação é composta por três componentes principais:

1. **Frontend**: Interface de usuário construída com Streamlit
2. **Backend**: Motor de processamento que utiliza IA para gerar os arquivos
3. **Sistema de Arquivos**: Gerencia a criação e empacotamento dos arquivos gerados

### Fluxo de Operação

1. O usuário insere uma descrição do sistema desejado na interface
2. O backend processa a descrição e aciona o fluxo de trabalho CrewAI
3. O sistema gera três arquivos de configuração:
    - `agents.yaml`: Define os agentes que compõem o sistema
    - `tasks.yaml`: Especifica as tarefas a serem executadas
    - `crew.py`: Configura a orquestração dos agentes e tarefas
4. Os arquivos são empacotados em um arquivo ZIP
5. O usuário recebe uma notificação e pode fazer o download dos arquivos

## Contato

- [GitHub](https://github.com/AngeloGagno)
- [LinkedIn](https://www.linkedin.com/in/angelogagno)

---

Desenvolvido por Angelo Gagno