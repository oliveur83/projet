# coding: utf-8
# cette page est accueil de notre site 
print("Content-type: text/html; charset=unicode\n")
import cgi 
import cgitb
import psycopg2

cgitb.enable()
form=cgi.FieldStorage()

e_mail=form.getvalue('e_mail')
code=form.getvalue('code')

prenom=form.getvalue('prenom')
nom=form.getvalue('nom')
tel=form.getvalue('tel')
adresse=form.getvalue('adresse')
date_de_naissance=form.getvalue('date_de_naissance')
adresse_mail=form.getvalue('adresse_mail')

htmld= """<!DOCTYPE html>
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
<center>
votre création client est bien faite
      <form action="reservation.py" method="post">
        <input  type="submit" name="retour" value="retour" />
      </form>
""" 
htmlf="""
</center> 
</body>
</html>
"""


print(htmld)
#------------------connection----------
hostname = 'localhost'  
username = 'postgres'
password = '@toto83DBZ'
database = 'camping'
TableTest1 = "camping.compte"
TableTest2 = "camping.profil_client"

myConnection = psycopg2.connect( host=hostname, user=username,
password=password, dbname=database )
if myConnection :
    cursor =myConnection .cursor()
#recupere id client
req = ("SELECT id_compte from {} where e_mail_compte ='{}'".format(TableTest1,e_mail))
cursor.execute(req)
data = cursor.fetchall()    

id_compte=data[0][0]

#recupere id client
req = ('SELECT max(id_profil_client) from {}'.format(TableTest2))
cursor.execute(req)
data = cursor.fetchall()    
id_client=data[0][0]+1


sqlclient = """INSERT INTO camping.profil_client (id_profil_client,adresse_c,prenom_c,
nom_c,date_naissance_c,telephone_c,adresse_mail_c,id_compte) VALUES (%s,%s,%s,%s,%s,%s,%s,%s)"""

value = (id_client,adresse,prenom,nom,date_de_naissance,tel,adresse_mail,id_compte)
cursor .execute(sqlclient,value)
# validé la modification
myConnection .commit()
count = cursor .rowcount

print("tout est bon")
print(htmlf)