## API

### Classe `Webapp`

Responsável pela interface do usuário e interações.

#### Métodos Principais

- `execute()`: Inicia o processamento quando o botão é clicado
- `verify_len_text()`: Valida se o texto tem o tamanho mínimo necessário
- `create_zip()`: Empacota os arquivos gerados em um ZIP

### Função `run()`

Processa o input do usuário e aciona a geração dos arquivos.

```python
def run(input):
    """
    Run the crew.
    """
    inputs = {
        'definicao_do_sistema': input,
    }
    
    try:
        CreateCrewProject().crew().kickoff(inputs=inputs)
    except Exception as e:
        raise Exception(f"An error occurred while running the crew: {e}")
```
