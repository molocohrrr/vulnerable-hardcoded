# Hardcoded Credentials Vulnerabilities

Este repositório contém exemplos de vulnerabilidades de credenciais hardcoded em diferentes formatos de arquivo. O objetivo é demonstrar as más práticas de segurança e a importância de evitar o armazenamento de credenciais diretamente no código-fonte.

## Estrutura do Projeto

vulnerable-hardcoded/
├── README.md
├── config/
│   ├── config.py
│   ├── settings.json
│   ├── secrets.yaml
│   ├── email_config.py
│   ├── aws_config.py
│   └── ssl_config.py
├── src/
│   ├── main.py
│   ├── utils.py
│   └── database.py
└── tests/
    └── test_config.py

## Exemplos de Credenciais Hardcoded

- `config/config.py`
- `config/settings.json`
- `config/secrets.yaml`
- `config/email_config.py`
- `config/aws_config.py`
- `config/ssl_config.py`

## Como Executar

1. Clone o repositório.
2. Navegue até o diretório `src`.
3. Execute o script `main.py`:
   ```sh
   python main.py
   ```