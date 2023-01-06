import mariadb

con = mariadb.connect(
    host = 'localhost',
    port = 3307,
    database = 'nomBase',
    user = 'root',
    password= 'password'
    )
curseur = con.cursor()
req = "select * from TABLE"
curseur.execute(req)
resultats = curseur.fetchall()

for resultat in resultats:
    print (resultat[1])
    
