# Projeto Doctoralia Brasil — Análise de Dados com dbt

## Descrição

Este projeto utiliza o dbt (data build tool) para transformar e analisar dados públicos de profissionais de saúde da plataforma Doctoralia Brasil. O objetivo é demonstrar boas práticas de engenharia de dados, modelagem analítica e automação de pipelines de dados.

## Sumário

- [Descrição](#descrição)
- [Sumário](#sumário)
- [Pré-requisitos](#pré-requisitos)
- [Instalação](#instalação)
- [Como usar](#como-usar)
- [Estrutura do Projeto](#estrutura-do-projeto)
- [Sobre o Dataset](#sobre-o-dataset)
- [Contribuição](#contribuição)
- [Referências](#referências)

## Pré-requisitos

- Python 3.7 ou superior
- dbt-core
- [Poetry](https://python-poetry.org/) (opcional, para gerenciamento de dependências)
- Git

## Instalação

1. Clone este repositório:
   ```bash
   git clone https://github.com/Rafaelcvo/dbt_cursos/tree/develop/Project_2
   ```
2. Instale as dependências com Poetry (opcional):
   ```bash
   poetry install
   ```
   Ou, se preferir, instale o dbt diretamente:
   ```bash
   pip install dbt-core
   ```

## Como usar

1. Navegue até a pasta do projeto:
   ```bash
   cd Project_2/estudos
   ```
2. Execute os modelos dbt:
   ```bash
   dbt run
   ```
3. Execute os testes dbt:
   ```bash
   dbt test
   ```

## Estrutura do Projeto

```
estudos/
├── data_csv/         # Dados brutos em CSV
├── models/           # Modelos SQL do dbt
├── macros/           # Macros customizadas
├── snapshots/        # Snapshots de dados
├── tests/            # Testes customizados
├── src/              # Scripts auxiliares
├── logs/             # Logs de execução
├── dbt_project.yml   # Configuração principal do dbt
└── README.md         # Este arquivo
```

## Sobre o Dataset

- **Fonte:** [Doctoralia Brasil - Kaggle](https://www.kaggle.com/datasets/miguelcorraljr/doctoralia-brasil)
- **Descrição:** Dados públicos de profissionais de saúde cadastrados na plataforma Doctoralia Brasil.
- **Arquivo principal:** `data_csv/202210_doctoralia_br.csv`

## Contribuição

Contribuições são bem-vindas! Sinta-se à vontade para abrir issues ou enviar pull requests com melhorias, correções ou sugestões.

## Referências

- [Documentação oficial do dbt](https://docs.getdbt.com/docs/introduction)
- [Comunidade dbt no Slack](https://community.getdbt.com/)
- [Blog dbt](https://blog.getdbt.com/)
- [Poetry](https://python-poetry.org/)

## Como automatizar a importação de dados

1. Coloque o arquivo `202210_doctoralia_br_utf8.csv` na pasta `seeds/`.
2. Execute `poetry run dbt seed` para importar o CSV como tabela gerenciada pelo dbt.
3. Ajuste o modelo bronze (`stg_doutores.sql`) para usar a tabela seed criada.
4. Execute `poetry run dbt run` normalmente.

---

Sinta-se à vontade para contribuir ou abrir issues para sugestões e melhorias.