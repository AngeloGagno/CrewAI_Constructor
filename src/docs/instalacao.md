## Instalação

### Pré-requisitos

- Python 3.9+
- pip (gerenciador de pacotes do Python)

### Passos para Instalação

1. Clone o repositório:
   ```bash
   git clone https://github.com/angelogagno/CrewAI_Constructor.git
   cd CrewAI_Constructor
   ```

2. Crie e ative um ambiente virtual:
   ```bash
   python -m venv venv
   source venv/bin/activate  # No Windows: venv\Scripts\activate
   ```

3. Instale as dependências:
   ```bash
   pip install -r requirements.txt
   ```

4. Configure as variáveis de ambiente:
   - Crie um arquivo `.env` na raiz do projeto
   - Adicione suas chaves de API conforme necessário:
     ```
     OPENAI_API_KEY=sua_chave_api_aqui
     ```
