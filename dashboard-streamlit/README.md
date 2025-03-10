# Dashboard Streamlit

Este projeto é um dashboard interativo desenvolvido com **Streamlit** para visualização e análise de dados. Ele inclui gráficos criados com **Plotly** e tabelas interativas com **Pandas**.

## 🚀 Como acessar

O deploy do projeto está disponível no Streamlit Community Cloud. Acesse o link abaixo para interagir com o dashboard:

🔗 [Acessar Dashboard](https://cat-cs-python-projects-dashboard-streamlitdashboard-nm8koc.streamlit.app/)

## 🛠️ Como executar localmente

Siga os passos abaixo para configurar e executar o projeto no seu ambiente local.

### Pré-requisitos

- Python 3.8 ou superior
- Pip (gerenciador de pacotes do Python)

### Passos

1. Clone o repositório:

   ```bash
   git clone https://github.com/cat-cs/python-projects.git
   

2. Navegue até a pasta do projeto:

   ```bash
   cd python-projects/dashboard-streamlit
   

3. Crie um ambiente virtual (opcional, mas recomendado):
   ```bash
   python -m venv venv
   ```  

   - No Windows:
   ```bash
     venv\Scripts\activate
    ```   
   - No macOS/Linux:
    ```bash
     source venv/bin/activate
    ``` 

4. Instale as dependências:
   ```bash
   pip install -r requirements.txt
   

5. Execute o aplicativo Streamlit:
   ```bash
   streamlit run Dashboard.py
  

6. Acesse o aplicativo no navegador:

   Abra o endereço exibido no terminal (geralmente `http://localhost:8501`).

## 📦 Dependências

As principais bibliotecas utilizadas neste projeto são:

- **Streamlit**: Para criar a interface do dashboard.
- **Plotly**: Para criar gráficos interativos.
- **Pandas**: Para manipulação e análise de dados.

O arquivo `requirements.txt` contém todas as dependências necessárias. Você pode instalá-las com o comando:
```bash
pip install -r requirements.txt
```

## 📂 Estrutura do Projeto

```bash
dashboard-streamlit/
├── Dashboard.py          # Código principal do dashboard
├── requirements.txt      # Lista de dependências
├── pages/                # Páginas adicionais (se aplicável)
│   └── pagina1.py        # Exemplo de página adicional
└── README.md             # Este arquivo
```

## 📊 Funcionalidades

- Visualização de dados em gráficos interativos.
- Filtros e controles para personalizar a visualização.
- Tabelas dinâmicas para análise detalhada.

## 🤝 Como contribuir

Contribuições são bem-vindas! Siga os passos abaixo:

1. Faça um fork do repositório.
2. Crie uma branch para sua feature (`git checkout -b feature/nova-feature`).
3. Commit suas mudanças (`git commit -m 'Adiciona nova feature'`).
4. Faça push para a branch (`git push origin feature/nova-feature`).
5. Abra um Pull Request.
