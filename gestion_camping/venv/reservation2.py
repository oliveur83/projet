
# coding: utf-8
# 2eme page inscription 
# inscription des personnne dans la location


#---------------------------initialise les variables-----------------
import cgi 
import cgitb
import psycopg2

cgitb.enable()
form=cgi.FieldStorage()

#regle un probleme 
val=int(form.getvalue('val'))
e_mail=form.getvalue('e_mail')
id_emplacement=int(form.getvalue("id_emplacement"))
duree=form.getvalue('duree')
dated=form.getvalue('dated')
datef=form.getvalue('datef')
nbr_voiture=form.getvalue('nbr_voiture')
demi_pension =form.getvalue('demi_pension')

#variable affichage 
select=form.getvalue('id_client')

select1="n"
chaineclient=", "
if val==1:
    select1=form.getvalue('id_client2')
    select1=select+select1
    chaineclient=form.getvalue('id_toto')
    chaineclient=","+select+chaineclient

print("Content-type: text/html; charset=unicode\n")

#------------------------------------------------------------
# ---------------------------variable pour html -----------------
fonction_recup=(""" 
<input type="hidden"  name="e_mail" value="{}" />
<input type="hidden" name="id_emplacement" value="{}" />
<input type="hidden" name="duree" value="{}" />
<input type="hidden" name="datef" value="{}" />
<input type="hidden"  name="dated" value="{}" />
<input type="hidden" name="nbr_voiture" value="{}" />
<input  type="hidden" name="demi_pension" value="{}" />

""".format(e_mail,id_emplacement,duree,dated,datef,nbr_voiture,demi_pension ))

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
        div {
                border: 2px solid yellow;
                width:400px;
								height:250px;
            }
          div22 {
                border: 2px solid yellow;
            }
         div2 {
              float:left;
                border: 2px solid white;
                width:400px;
								height:300px;
            }
        div3 {
              float:left;
                border: 4px solid green;
            }
        h1 {
                text-align:center;
            }
    .image {
                width: 50px;
            }
      </style>
    </head>
<body>
        <h1>réservation page 2 </h1>
<div2> 
<div> """

htmld1="""
</div> 
 """
htmld2="""

</div2>
<div2>
   <form action="reservation2.py" method="post">
"""

bouton_selectiond=""" 

  choisir un client:
  <select name="id_client" >
  """
bouton_selectionf=("""
   </select>

 <input type="submit" value="valide" />
 <input type="hidden" name="val" value="1" />
  <input type="hidden" name="id_client2" value="{}" />
  <input type="hidden" name="id_toto" value="{}" />
 </form>
</div2>
""".format(select1,chaineclient))



bouton=(""" <div3><form action="validation_reservation.py" method="post">
  <input type="submit" value="valider" />

<input type="hidden" name="id_emplacement" value="{}" />
<input type="hidden" name="duree" value="{}" />
<input type="hidden" name="datef" value="{}" />
<input type="hidden"  name="dated" value="{}" />
<input type="hidden" name="nbr_voiture" value="{}" />
<input  type="hidden" name="demi_pension" value="{}" />
  <input  name="chaineclient" type="hidden" value="{}">
  <input  name="e_mail" type="hidden" value="{}">
</form></div3> <div3> 
<form action="reservation.py" method="post">
 <input type="submit" value="retour" />
 </form></div3> <div3> 
 <form action="creation_client.py" method="post">
 <input type="submit" value="creation " />
  <input  name="e_mail" type="hidden" value="{}">    
 </form></div3>  """.format(id_emplacement,duree,datef,dated,nbr_voiture,demi_pension,chaineclient,e_mail,e_mail))


html2="""
</body>   

</html>
"""

fintable="""</table> """

#-----------------------------------------------------------------
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
#------passe de e_mail a id_compte 
req= ("SELECT id_compte from {} where e_mail_compte='{}'".format(TableTest2,e_mail))
cursor.execute(req)
datar = cursor.fetchall()  
#afficher les client par rapport au compte 
req= ("SELECT id_profil_client,prenom_c from {} where id_compte='{}'".format(TableTest1,datar[0][0]))
cursor.execute(req)

data = cursor.fetchall()    
longd=len(data)
#-----------affichage de client ----------------
if (val==1):
  i=0
  x=len(select1)-1
  toto=""" """
  while i<x:
    req= ("SELECT * from {} where id_profil_client='{}'".format(TableTest1,select1[i]))
    cursor.execute(req)
    datar = cursor.fetchall()  
    toto= toto+("""
    prenom: {}<br>
    """.format(datar[0][4]))

    i=i+1
else: 
  toto=""
#--------------programme principal --------------------
print(htmld)
print(toto)
print(htmld1)
print(bouton)
print(htmld2)
print(fonction_recup)
print(bouton_selectiond)
i=0
while i<longd:
   print(f"""<option value="{data[i][0]}">{data[i][1]}</option>""")
   i=i+1
print(bouton_selectionf)


print(html2)
