# coding: utf-8
# cette page est accueil de notre site 
print("Content-type: text/html; charset=unicode\n")
import psycopg2
import cgi 
import cgitb

cgitb.enable()
form=cgi.FieldStorage()

e_mail=form.getvalue('e_mail')
id_tournoi=form.getvalue('id_tournoi')


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
bouton_selectiond=""" 
<form action="validation_inscription_tournoi.py" method="post">
  choisir un client:
  <select name="id_client" >
  """
bouton_selectionf=("""
   </select>
<input  type="hidden" name="id_tournoi" value="{}" />
 <input type="submit" value="valide" />
 
 </form>

""".format(id_tournoi))

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
#------passe de e_mail a id_compte 
req= ("SELECT id_compte from {} where e_mail_compte='{}'".format(TableTest2,e_mail))
cursor.execute(req)
datar = cursor.fetchall()  
#afficher les client par rapport au compte 
req= ("SELECT id_profil_client,prenom_c from {} where id_compte='{}'".format(TableTest1,datar[0][0]))
cursor.execute(req)

data = cursor.fetchall()    
longd=len(data)

print(htmld)
print(bouton_selectiond)
i=0
while i<longd:
   print(f"""<option value="{data[i][0]}">{data[i][1]}</option>""")
   i=i+1
print(bouton_selectionf)
print(html2)
