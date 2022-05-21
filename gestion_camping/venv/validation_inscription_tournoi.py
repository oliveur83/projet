# coding: utf-8
# cette page est accueil de notre site 
print("Content-type: text/html; charset=unicode\n")
import psycopg2
import cgi 
import cgitb

cgitb.enable()
form=cgi.FieldStorage()

id_client=int(form.getvalue('id_client'))
id_tournoi=int(form.getvalue('id_tournoi'))

htmld = """<!DOCTYPE html>
<html>
    <head>
      <style>
        body 
        {color: yellow; 
          background-image: url('https://www.lapascalinette.fr/wp-content/uploads/2018/07/parc-aquatique-du-camping-de-la-pascalinette.jpg');
          background-repeat: no-repeat;
          background-attachment: fixed;  
          background-size: cover;
        }
      </style>
    </head>
<body>
"""

html2="""
</body>   

</html>
"""
#connexion
hostname = 'localhost'  
username = 'postgres'
password = '@toto83DBZ'
database = 'camping'
TableTest1 = "camping.profil_client"
TableTest2 = "camping.compte"

myConnection = psycopg2.connect( host=hostname, user=username,
password=password, dbname=database )
if myConnection :
    cursor =myConnection .cursor()
sql = """INSERT INTO camping.participant(id_profil_client,id_tournoi,resultat)
    VALUES (%s,%s,%s)"""
value = (id_client,id_tournoi,'pac')
cursor.execute(sql, value)
#validé la modification
myConnection .commit()
count = cursor .rowcount
print(htmld)

print(html2)
