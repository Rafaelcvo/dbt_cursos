import duckdb

con = duckdb.connect('dev.duckdb')

res = con.execute("SELECT * FROM doutor limit 10").fetchall()
                                    
print(res)

con.close()
