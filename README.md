Sistema Produtor/Consumidor com RabbitMQ e Python

Este projeto demonstra a implementação do padrão **Produtor/Consumidor** utilizando **Python** e **RabbitMQ**. 
A comunicação é realizada por meio de filas, onde o **Produtor** envia mensagens e o **Consumidor** recebe e registra as mensagens em um arquivo `.txt` com a data e hora de recebimento.

Funcionalidades

- **Produtor**: Lê mensagens digitadas no terminal e envia para a fila no RabbitMQ.
- **Consumidor**: Escuta a fila e salva as mensagens recebidas com data/hora em um arquivo `mensagens.txt`.
- Interface Web para monitoramento do RabbitMQ.
- Utilização de **Docker** para facilitar a execução do RabbitMQ.

Tecnologias utilizadas

- **Python 3.11+**
- **RabbitMQ** (via Docker)
- **pika** (biblioteca Python para RabbitMQ)
- **Docker Compose** (para orquestrar o ambiente RabbitMQ)

Pré-requisitos

- Python instalado (https://www.python.org/downloads/)
- Docker instalado (https://www.docker.com/products/docker-desktop)
- Git instalado (https://git-scm.com/)

Estrutura do projeto
meu_projeto_rabbit/
├── produtor.py # Código do produtor (envia mensagens)
├── consumidor.py # Código do consumidor (recebe e registra mensagens)
├── docker-compose.yml # Configuração do RabbitMQ via Docker
├── mensagens.txt # Arquivo de saída das mensagens recebidas
├── README.md # Documentação do projeto
└── .gitignore # Arquivos ignorados pelo Git

Autor
Desenvolvido por Alessandro Pereira da Rosa Filho
GitHub: https://github.com/alekrszp



