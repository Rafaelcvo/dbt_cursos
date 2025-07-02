# Projeto: Análise de Dados Doctoralia Brasil

Este projeto utiliza dbt (data build tool) para análise e transformação de dados do dataset Doctoralia Brasil, disponível no Kaggle. O objetivo é demonstrar práticas de engenharia e análise de dados utilizando dbt, facilitando a criação de modelos analíticos reprodutíveis e escaláveis.

## Pré-requisitos
- Python 3.7+
- dbt (recomendado instalar via pip ou poetry)
- [Poetry](https://python-poetry.org/) (opcional, para gerenciamento de dependências)

## Instalação
1. Clone este repositório:
   ```bash
   git clone https://github.com/Rafaelcvo/dbt_cursos/tree/develop/Project_2
   ```
2. Instale as dependências com Poetry (opcional):
   ```bash
   poetry install
   ```
   Ou instale o dbt diretamente:
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
- `models/` - Modelos SQL transformacionais do dbt
- `data_csv/` - Arquivos CSV de dados brutos
- `macros/` - Macros customizadas para uso nos modelos
- `snapshots/` - Snapshots de dados para controle de mudanças
- `tests/` - Testes customizados do dbt
- `logs/` - Logs de execução
- `src/` - Scripts auxiliares (ex: consultas, ETL)

## Dataset
- **Fonte:** [Doctoralia Brasil - Kaggle](https://www.kaggle.com/datasets/miguelcorraljr/doctoralia-brasil)
- **Descrição:** Dados públicos de profissionais de saúde cadastrados na plataforma Doctoralia Brasil.
- O arquivo principal utilizado está em `data_csv/202210_doctoralia_br.csv`.

## Referências e Recursos
- [Documentação oficial do dbt](https://docs.getdbt.com/docs/introduction)
- [Comunidade dbt no Slack](https://community.getdbt.com/)
- [Blog dbt](https://blog.getdbt.com/)
- [Poetry](https://python-poetry.org/)

---

Sinta-se à vontade para contribuir ou abrir issues para sugestões e melhorias.