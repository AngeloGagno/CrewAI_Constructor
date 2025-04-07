## Instalação

### Pré-requisitos

- Docker

### Passos para Instalação

1. Clone o repositório:
   ```bash
   git clone https://github.com/angelogagno/CrewAI_Constructor.git
   cd CrewAI_Constructor
   ```

2. Configure as variáveis de ambiente:
   - Crie um arquivo `.env` na raiz do projeto
   - Adicione suas chaves de API conforme necessário:
     ```
     OPENAI_API_KEY=sua_chave_api_aqui
     ```

3. Execute o container da aplicação:
   ```bash
   docker compose up --build
   ```