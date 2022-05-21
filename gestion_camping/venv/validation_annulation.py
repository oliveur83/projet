# coding: utf-8
# cette page est accueil de notre site 
print("Content-type: text/html; charset=unicode\n")
import cgi 
import cgitb
import psycopg2

cgitb.enable()
form=cgi.FieldStorage()

annule=form.getvalue('annule')


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
votre reservation est bien annulée
      <form action="index.py" method="post">
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
TableTest1 = "camping.reservation"
TableTestt = "camping.camping_client"

myConnection = psycopg2.connect( host=hostname, user=username,
password=password, dbname=database )
if myConnection :
    cursor =myConnection .cursor()

req = ("DELETE FROM {} WHERE id_reservation ={}".format(TableTestt,annule))
cursor.execute(req)
myConnection .commit()
count = cursor .rowcount

req = ("DELETE FROM {} WHERE id_reservation ={}".format(TableTest1,annule))
cursor.execute(req)
    # validé la modification
myConnection .commit()
count = cursor .rowcount