## Configuração

### Personalização dos Agentes

O sistema utiliza quatro agentes padrão:

1. **Arquiteto de Solução**: Define a visão geral do sistema
2. **Especialista em Agentes**: Cria e configura os agentes específicos
3. **Gerente de Fluxo de Trabalho**: Define as tarefas e suas associações
4. **Engenheiro de Orquestração**: Integra os componentes em um sistema funcional

Para personalizar os agentes, edite o arquivo `config/agents.yaml`.

### Fluxo de Trabalho

O sistema segue um processo sequencial de quatro etapas:

1. **Planejamento da Arquitetura**: Define a estrutura do sistema
2. **Criação dos Agentes**: Gera as definições dos agentes
3. **Definição das Tarefas**: Especifica as tarefas a serem executadas
4. **Desenvolvimento da Orquestração**: Cria o arquivo que coordena o sistema

Para ajustar este fluxo, edite o arquivo `config/tasks.yaml`.

## Exemplos

### Exemplo 1: Sistema de Recomendação

Prompt de entrada:
```
Criar um sistema de recomendação de filmes baseado nas preferências do usuário e histórico de visualização. O sistema deve considerar gêneros, atores, diretores e classificações anteriores para sugerir novos filmes que o usuário possa gostar.
```

### Exemplo 2: Assistente de Escrita

Prompt de entrada:
```
Desenvolver um assistente de escrita que ajude a criar conteúdo para blogs. O sistema deve analisar o tópico fornecido, pesquisar informações relevantes, sugerir estruturas de artigo e ajudar a melhorar o texto final com sugestões de estilo e gramática.
```

## Solução de Problemas

### Problemas Comuns

| Problema | Solução |
|----------|---------|
| Erro "Não há 3 arquivos na pasta de output" | Verifique se o prompt tem detalhes suficientes e tente novamente |
| Tempo de processamento muito longo | Os modelos de IA podem levar mais tempo com prompts complexos |
| Erro na conexão com a API | Verifique se sua chave de API está configurada corretamente no arquivo .env |