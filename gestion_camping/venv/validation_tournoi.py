#coding: utf-8

import psycopg2
import cgi 
import cgitb

cgitb.enable()
form=cgi.FieldStorage()

typee=form.getvalue('type')
nombre_particiapnt=form.getvalue('nombre_particiapnt')
heure=form.getvalue('heure')
date=form.getvalue('date')


#---------------------- variable HTML---------------------
html = """<!DOCTYPE html>
<html>
    <head>
      <style>
        body 
        {
          background-image: url('https://www.lapascalinette.fr/wp-content/uploads/2018/07/parc-aquatique-du-camping-de-la-pascalinette.jpg');
          background-repeat: no-repeat;
          background-attachment: fixed;  
          background-size: cover;
        }
        div {
          border: 5px ridge #000;
          background-color: #ffF;
          width:300px;
					height:200px;
        }
      </style>
    </head>

<body><center>
<div><br><br><br>""" 

htmlf="""
<form action="index.py" method="post">
<input  type="submit" value="retour" />
</form>
</div>
</center> 
</body>
</html>
"""
#------------------------------ python et bdd----------
#connexion
hostname = 'localhost'  
username = 'postgres' 
password = '@toto83DBZ'
database = 'camping'
TableTest1 = "camping.tournoi"

myConnection = psycopg2.connect( host=hostname, user=username,
password=password, dbname=database )
if myConnection :
    cursor =myConnection .cursor()
    
#selection du max 
reqmaxid_client = ('SELECT max(id_tournoi) from {}'.format(TableTest1))
cursor.execute(reqmaxid_client)
data = cursor.fetchall()    
maxi=data[0][0]+1

#insert dans la table compte 
sql = """INSERT INTO camping.tournoi(id_tournoi,type_tournoi,nbr_participant,heure_tournoi,date_tournoi)
    VALUES (%s,%s,%s,%s,%s)"""
value = (maxi,typee,nombre_particiapnt,heure,date)
cursor.execute(sql, value)
#validé la modification
myConnection .commit()
count = cursor .rowcount
#---------------------partie html 
print("Content-type: text/html; charset=unicode\n")
print(html)
print("""votre création tournoi a bien été enregistré !! """)
print(htmlf)
