# dbt_cursos

Este repositório reúne diferentes projetos de estudo e demonstração de uso do [dbt (data build tool)](https://www.getdbt.com/), voltados para engenharia de dados, modelagem e integração com ferramentas como DuckDB, Snowflake e Airflow.

## Sumário dos Projetos

- **Doctoralia**: Pipeline de dados simulado para análise de profissionais de saúde, usando dbt com DuckDB.
- **Project_1**: Exemplo de arquitetura integrando dbt, Snowflake e Airflow, com scripts, DAGs e modelos de demonstração.
- **Project_2**: Projeto de estudos e experimentos com dbt, focado em exemplos simples e didáticos.

---

## Estrutura de Diretórios

```
Doctoralia/
  doctoralia/           # Projeto dbt com modelos, seeds, macros, etc.
  logs/                 # Logs de execução

Project_1/
  assets/               # Imagens ilustrativas da arquitetura
  dags/                 # DAGs do Airflow
  src/dbt/              # Projeto dbt para Snowflake
  scripts/              # Scripts auxiliares
  docker-compose.yml    # Ambiente dockerizado

Project_2/
  estudos/              # Projeto dbt de estudos
```

---

## Como usar

1. **Pré-requisitos**
   - Python 3.8+
   - [dbt](https://docs.getdbt.com/docs/installation) (instalado via pip ou poetry)
   - Docker (opcional, para Project_1)

2. **Instalação de dependências**
   - Cada subprojeto possui seu próprio `pyproject.toml` e pode ser instalado via [Poetry](https://python-poetry.org/):
     ```bash
     cd Doctoralia/doctoralia
     poetry install
     # ou
     cd Project_1
     poetry install
     # ou
     cd Project_2/estudos
     poetry install
     ```

3. **Executando modelos dbt**
   - Entre no diretório do projeto desejado e execute:
     ```bash
     dbt run
     dbt test
     ```

4. **Project_1: Ambiente Docker + Airflow + Snowflake**
   - Siga as instruções em `Project_1/README.md` para subir o ambiente dockerizado e executar os exemplos.

---

## Referências e Contato

- [dbt Documentation](https://docs.getdbt.com/)
- Para dúvidas ou sugestões, abra uma issue ou entre em contato com o mantenedor do repositório. 