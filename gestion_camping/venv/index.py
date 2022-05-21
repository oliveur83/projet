# coding: utf-8
# cette page est accueil de notre site 
print("Content-type: text/html; charset=unicode\n")

import psycopg2
import cgi 
import cgitb
import datetime
from datetime import timedelta

cgitb.enable()
form=cgi.FieldStorage()

date = datetime.date.today()

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
<body>    
<center>
  <div>
    <h1>camping les flots </h1> 
      <form action="connexion.py" method="post">
        <input  type="submit" value="connexion" />
      </form>
      <form action="information.py" method="post">
        <input  type="submit" value="information sur le camping" />
      </form>
        <form action="inscription.py" method="post">
        <input  type="submit" value="inscription pour avoir un compte " />
      </form>
      <form action="connexion_admin.py" method="post">
        <input  type="submit" name="valeur" value="connexion admin" />
      </form>
      </div>
  </center> 
</body>
</html>
"""

print(html)
#---------------------------------pour suprimez automatiquement----------
#------------------connection----------
hostname = 'localhost'  
username = 'postgres'
password = '@toto83DBZ'
database = 'camping'
Reservation = "camping.reservation"
Camping_Client = "camping.camping_client"
Profil_Client = "camping.profil_client"
Reservation_Historique = "camping.reservation_historique"
Client_Historique = "camping.client_historique"

myConnection = psycopg2.connect( host=hostname, user=username,
password=password, dbname=database )
if myConnection :
    cursor =myConnection .cursor()

# Requete SQL pour avoir tout les reservation 
req = ('SELECT * from {}'.format(Reservation))
cursor.execute(req)
data = cursor.fetchall() 
#max idk_his dans reservation historique 
req = ('SELECT max(id_his)from {}'.format(Reservation_Historique))
cursor.execute(req)
his = cursor.fetchall() 
hist=his[0][0]+1
#max idk_his dans client historique 
req = ('SELECT max(id_his)from {}'.format(Client_Historique))
cursor.execute(req)
hisc = cursor.fetchall() 
histc=hisc[0][0]+1


i=0
longe=len(data)
#parcour toute les reservation
while i<longe:
  toto=date- timedelta(days=2)
  if toto>=data[i][4] or date>data[i][5]  :#date de debut 
  
  #insere dans reservation historique
    sqlresa = """INSERT INTO camping.reservation_historique
        (id_reservation,id_emplacement,id_compte,s_est_presente,date_deb,date_fin,nbr_places_parking,nbr_pers_reserv
        ,demi_pens,a_annule,revenu,id_his) VALUES (%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s)
        """
    value=(data[i][0],data[i][1],data[i][2],data[i][3],data[i][4],
        data[i][5],data[i][6],data[i][7],data[i][8],0,0,hist)
    cursor.execute(sqlresa,value)
    myConnection .commit()
    count = cursor .rowcount
    #inserer dans client historique 
    req = ('SELECT * from {} where id_reservation={}'.format(Camping_Client,data[i][0]))
    cursor.execute(req)
    cc = cursor.fetchall() 
    j=0
    longcc=len(cc)
    #parcourir toutes les personnes 
    while j<longcc:
      req = ('SELECT * from {} where id_profil_client={}'.format(Profil_Client,cc[j][1]))
      cursor.execute(req)
      compte= cursor.fetchall() 
      sqlresa = """INSERT INTO camping.client_historique
        (adresse_c,prenom_c,nom_c,date_naissance_c,adresse_mail_c,telephone_c,id_profil_client,id_compte,a_annule
        ,s_est_presente,date_deb,date_fin,id_his) 
        VALUES (%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s)"""
      value=(compte[0][1],compte[0][4],compte[0][5],compte[0][6],compte[0][3],compte[0][2],compte[0][0],
        compte[0][7],0,0,data[i][4],data[i][5],hisc)
      cursor.execute(sqlresa,value)
      myConnection .commit()
      count = cursor .rowcount
      j=j+1

    #suprimme de camping_client
    req = ("DELETE FROM {} WHERE id_reservation ={}".format(Camping_Client,data[i][0]))
    cursor.execute(req)
    myConnection .commit()
    count = cursor .rowcount
    #suprimme de resa
    req = ("DELETE FROM {} WHERE id_reservation ={}".format(Reservation,data[i][0]))
    cursor.execute(req)
    # validé la modification
    myConnection .commit()
    count = cursor .rowcount
  i=i+1




