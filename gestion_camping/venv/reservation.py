# coding: utf-8
#1 er page de reservation 
# les date ne sont pas configure pour le moment 
print("Content-type: text/html; charset=unicode\n")
import psycopg2
import cgi 
import cgitb
import datetime
from datetime import timedelta

cgitb.enable()
form=cgi.FieldStorage()

datete = datetime.date.today()
#------recuperation de variable 
e_mail=form.getvalue('e_mail')
dated=form.getvalue('dated')
datef=form.getvalue('datef')
val=form.getvalue('val')
typee=form.getvalue('type')
code=form.getvalue('code')
#-------------------connexion
hostname = 'localhost'  
username = 'postgres'
password = '@toto83DBZ'
database = 'camping'
TableTest1 = "camping.reservation"
TableTest2 = "camping.emplacement"

titi=""" """
myConnection = psycopg2.connect( host=hostname, user=username,
password=password, dbname=database )
if myConnection :
    cursor =myConnection .cursor()
#------------------------------

libre=0 #variable bool   
i=0# id_emplacement 

if val=='0':
  #rentre apres validation
  # intervalle pour teste tout les emplacement 
  req= ("SELECT id_emplacement from {} where type_emplacement='{}' ".format(TableTest2,typee))
  cursor.execute(req)
  datarr = cursor.fetchall()  
  i=0
  pp=len(datarr)
  #mettre les date au bon format 
  dateFormatter = "%Y-%m-%d"
  dated=datetime.datetime.strptime(dated,dateFormatter)
  dated=dated.date()
  datef=datetime.datetime.strptime(datef,dateFormatter)
  datef=datef.date()
#------------- voir en fonction des date si c'est libre ou non 
  while i<=pp:
    req= ("SELECT date_deb,date_fin,id_emplacement from {} where id_emplacement={}".format(TableTest1,datarr[i][0]))
    cursor.execute(req)
    datar = cursor.fetchall()   
    if datar!=[]:
      j=0
      x=len(datar)
      while j<x:
        if (  (dated<datar[j][0] and  datef<datar[j][0]) or (dated>datar[x-1][1]) ) and  j==0:
          libre=1
          break
        elif (dated>datar[j-1][1] and  datef<datar[j][0]):
            libre=1
            break
        j=j+1
    else:
        libre=1
    if libre==1:
      break
    i=i+1
#-------------------
  if libre==1:
    titi=""" Vous pouvez reserver<br>"""
  else:
    titi=""" complet<br>"""
#-------------------------------------------

html =  """<!DOCTYPE html>
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
 <center>"""
html1="""
autres informations:
<form action="reservation2.py" method="post">
<table>  
</tr>  
    <tr> <th>nombre de personne  :</th><th> <input type="text" name="duree"value="1"/></th></tr> 
   <tr> <th> demi pension?</th><th>     
   <select name="demi_pension">
        <option value="1">oui</option>
        <option value="0">non</option>
 </select> </th></tr>   
   <tr> <th> nombre de voiture</th><th> <input type="text" name="nbr_voiture" value="0"/></th></tr>   
       </table>
       <input type="submit" value="valider" />
       </form>
"""
if val=='0':
  html11 =("""
autres informations:
<form action="reservation2.py" method="post">
<table>  
</tr>  
    <tr> <th>nombre de personne  :</th><th> <input type="text" name="duree"value="1"/></th></tr> 
   <tr> <th> demi pension?</th><th>     
   <select name="demi_pension">
        <option value="1">oui</option>
        <option value="0">non</option>
 </select> </th></tr>   
   <tr> <th> nombre de voiture</th><th> <input type="text" name="nbr_voiture" value="0"/></th></tr>   
       </table>
       <input  name="e_mail" type="hidden" value="{}">
       <input  name="dated" type="hidden" value="{}">
       <input  name="datef" type="hidden" value="{}">
       <input type="hidden" name="val" value="0" />
       <input type="hidden" name="id_emplacement" value="{}" />
       <input type="submit" value="valider" />
       </form>
    """.format(e_mail,dated,datef,datarr[i][0]))

retour=("""    <form action="compte.py" method="post">
        <input  type="submit" value="retour" /> 
        <input  name="e_mail" type="hidden" value="{}">
        <input  name="code" type="hidden" value="{}">
        </form>""".format(e_mail,code))
html2="""
    </center> 
</body>
</html>
"""
toto=("""     
 choisir vos dates :
 <form action="reservation.py" method="post">
 date de debut: <input type="date" min="{}" name="dated">
      date de fin:<input type="date"  name="datef">
      <input type="hidden" name="val" value="0" />
      <input  name="e_mail" type="hidden" value="{}">
<br>
      <tr><th> type de la location :</th><th>
    <select name="type">
        <option value="ta">grande tente</option>
        <option value="tb"> moyenne tente</option>
        <option value="tc"> petite tente</option>
        <option value="ca">grande  caravane</option>
        <option value="cb">moyenne caravane</option>
        <option value="cc"> petite caravane</option>
        <option value="ma">grande  mobilehome</option>
        <option value="mb"> moyenne mobilehome</option>
        <option value="mc"> petite mobilehome</option>
        <option value="ba">grande  bungalows</option>
        <option value="bb"> moyenne bungalow</option>
        <option value="bsc"> petite bungalow</option>
    </select>
    </th><br>
      <input type="submit" value="valider" />
  </form> """.format(datete,e_mail))
  #-----------------------------------------
#------------------------------------
print(html)


print(toto)
print(titi)
if val=='0':
  print(html11)
else:
  print(html1)
print(retour)
print(html2)

