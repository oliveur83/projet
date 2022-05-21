# 3 eme page de reservation 
# reste test de 2 location je pense crée un espace compte 
# il y a aussi acompte a faire 

#noublie pas de changer les codes de connection et surement la table avec 


# coding: utf-8
import psycopg2
#-----------------------------
import cgi 
import cgitb
#------------------------------recuperation des variable 
cgitb.enable()
form=cgi.FieldStorage()
demi_pension =form.getvalue('demi_pension')
dated= form.getvalue('dated')
datef=form.getvalue('datef')
datef=form.getvalue('datef')
nbr_voiture=form.getvalue('nbr_voiture')
id_emplacement=int(form.getvalue("id_emplacement"))
e_mail=form.getvalue('e_mail')
chaineclient=form.getvalue('chaineclient')



#-----------------espace html -----------------



htmld= """<!DOCTYPE html>
<html>
<body>"""

htmlf="""
</body>
</html>
"""
print("Content-type: text/html; charset=unicode\n")
print(htmld)
print("""votre reservation est faite""")

print(htmlf)
#------------------connection----------
hostname = 'localhost'  
username = 'postgres'
password = '@toto83DBZ'
database = 'camping'

TableTest2 = "camping.reservation"
TableTest3 = "camping.compte"

myConnection = psycopg2.connect( host=hostname, user=username,
password=password, dbname=database )
if myConnection :
    cursor =myConnection .cursor()

#--------------------------- enregistrement-------
#--------------------savoir id du compte --------
req = ("SELECT id_compte from {} where e_mail_compte='{}'".format(TableTest3,e_mail))
cursor.execute(req)
data = cursor.fetchall()    
id_compte=data[0][0]
#---------------------ajouter la reservation 
# Requete SQL
sqlreservation = """INSERT INTO camping.reservation(id_compte,id_reservation,
date_deb,date_fin,id_emplacement,s_est_presente,demi_pens,nbr_places_parking)
VALUES (%s,%s,%s,%s,%s,%s,%s,%s)"""


req = ('SELECT max(id_reservation) from {}'.format(TableTest2))
cursor.execute(req)
data = cursor.fetchall()    
id_reservation=data[0][0]+1

value=(id_compte,id_reservation,dated,datef,id_emplacement,0,demi_pension,nbr_voiture)
# Exécution de la requête
cursor.execute(sqlreservation, value)
# validé la modification
myConnection .commit()
count = cursor .rowcount
#--------------------mettre les client dans camping client 

sqlclient = """INSERT INTO camping.camping_client (id_reservation,id_profil_client) VALUES [(%s,%s),(%s,%s)]"""
i=1
longe=len(chaineclient)

titi=""
value=[]
while i<longe :
    l=chaineclient[i]

    if l!=",":
        titi=titi+l
    else:
        toto=int(titi)
        titi=""
        sqlclient = ("""INSERT INTO camping.camping_client
        (id_reservation,id_profil_client) VALUES ({},{})""".format(id_reservation,toto
        ))
        cursor.execute(sqlclient)
# validé la modification
        myConnection .commit()
        count = cursor .rowcount
    i=i+1   
#------------------------programme principal ---------



