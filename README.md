# FlaskJWTPostgresStarter

## Sobre o Projeto

FlaskJWTPostgresStarter é um projeto base em Python projetado como um ponto de partida para aplicações web. Ele combina o microframework Flask para o backend, JWT (JSON Web Tokens) para autenticação segura, e PostgreSQL para gerenciamento de banco de dados. Este projeto é um modelo para saber se tudo está configurado de maneira certa.

## Recursos

- **Flask**: Um microframework web leve e fácil de usar para Python.
- **JWT**: Implementação de autenticação via JSON Web Tokens.
- **PostgreSQL**: Um sistema de gerenciamento de banco de dados relacional robusto.
- **python-dotenv**: Para gerenciamento seguro de configurações sensíveis através de variáveis de ambiente.

## Pré-requisitos

- Python 3.6 ou superior.
- PostgreSQL instalado e configurado.
- Conhecimento básico em Python e SQL.

## Configuração do Projeto

1. Clone o repositório:
   ```bash
   git clone https://github.com/seu-usuario/FlaskJWTPostgresStarter.git
   cd FlaskJWTPostgresStarter
   ```

2. Crie e ative um ambiente virtual:
   - Linux/Mac:
     ```bash
     python3 -m venv venv
     source venv/bin/activate
     ```
   - Windows:
     ```bash
     python -m venv venv
     .\venv\Scripts\activate
     ```

3. Instale as dependências:
   ```bash
   pip install -r requirements.txt
   ```

4. Configure as variáveis de ambiente:
   - Copie o arquivo `.env.example` para `.env` e ajuste as variáveis conforme necessário.

## Executando o Projeto

Execute o comando abaixo para iniciar o servidor Flask:

```bash
python app.py
```

Acesse `http://localhost:5000` no navegador para ver a aplicação rodando.

## Contribuições

Contribuições são sempre bem-vindas! Por favor, entre em contato comigo para saber como contribuir para o projeto.

## Licença

Distribuído sob a licença MIT. Veja `LICENSE` para mais informações.

