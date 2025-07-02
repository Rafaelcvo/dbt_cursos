import duckdb

# Conecta ao banco criado pelo dbt
con = duckdb.connect('dev.duckdb')  # mesmo nome que está no profiles.yml

# Executa consulta na view criada pelo dbt
res = con.execute("SELECT * FROM meu_modelo").fetchall()

# Mostra os resultados
for linha in res:
    print(linha)

con.close()
