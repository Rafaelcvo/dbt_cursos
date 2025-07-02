import duckdb
import os
import kagglehub
import pandas as pd
import shutil

# 1. Baixa o dataset via kagglehub
dataset_path = kagglehub.dataset_download("miguelcorraljr/doctoralia-brasil")

# 2. Caminho original do CSV baixado
original_csv_path = os.path.join(dataset_path, '202210_doctoralia_br.csv')

# 3. Corrige a codificação para UTF-8 e salva na pasta data_csv/
dest_folder = 'data_csv'
os.makedirs(dest_folder, exist_ok=True)

# Caminho final do CSV corrigido
utf8_csv_path = os.path.join(dest_folder, '202210_doctoralia_br.csv')

# Converte o CSV para UTF-8, sobrescrevendo se necessário
df = pd.read_csv(original_csv_path)  # latin1 lida bem com acentos no Windows
df.to_csv(utf8_csv_path, index=False, encoding='utf-8')
print(f"Arquivo convertido para UTF-8 e salvo em: {utf8_csv_path}")

# 4. Conecta ao banco DuckDB (arquivo local)
con = duckdb.connect('dev.duckdb')

# 5. Cria ou substitui a tabela 'doutor' com base no CSV corrigido
con.execute("""
    CREATE OR REPLACE TABLE doutor AS
    SELECT * FROM read_csv_auto(?)
""", [utf8_csv_path])

# 6. Fecha a conexão
con.close()

print("Tabela 'doutor' criada com sucesso no banco DuckDB.")
