## Uso

### Iniciando a Aplicação

Execute o seguinte comando na raiz do projeto:

```bash
streamlit run main.py
```

A aplicação será iniciada e estará acessível em `http://localhost:8501`.

### Como Usar

1. Acesse a aplicação no navegador
2. No campo de texto, descreva detalhadamente o sistema que deseja criar
   - Exemplo: "Criar um sistema de análise de sentimentos para avaliações de produtos"
3. Clique no botão "Gerar Arquivos"
4. Aguarde o processamento (pode levar alguns segundos)
5. Quando concluído, clique no botão "Baixar Arquivos (.zip)"
6. Extraia o arquivo ZIP para acessar os arquivos gerados

## Estrutura do Projeto

```
crewai-generator/
├── main.py              # Ponto de entrada da aplicação
├── frontend/
│   └── app.py           # Interface de usuário Streamlit
├── create_crew_project/
│    ├── config/          # Arquivos de configuração
|        ├── agents.yaml     # Template para os agentes
│       └── tasks.yaml       # Template para as tarefas
│   ├── backend.py       # Lógica de processamento
│   └── crew.py          # Definição da crew CrewAI
├── output/              # Diretório onde os arquivos são gerados
└── docs/                # Documentação
```
