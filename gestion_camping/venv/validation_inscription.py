#coding: utf-8
print("Content-type: text/html; charset=unicode\n")
import psycopg2
import cgi 
import cgitb

cgitb.enable()
form=cgi.FieldStorage()

nom_de_compte=form.getvalue('nom_de_compte')
e_mail=form.getvalue('e_mail')
code=form.getvalue('code')

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
          width:400px;
					height:250px;
        }
      </style>
    </head>

<body>
<center>
<div>""" 

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
TableTest1 = "camping.compte"

myConnection = psycopg2.connect( host=hostname, user=username,
password=password, dbname=database )
if myConnection :
    cursor =myConnection .cursor()
    
#selection du max 
reqmaxid_client = ('SELECT max(id_compte) from {}'.format(TableTest1))
cursor.execute(reqmaxid_client)
data = cursor.fetchall()    
maxi=data[0][0]+1
#insert dans la table compte 
sql = """INSERT INTO camping.compte(id_compte,e_mail_compte,mp_compte,nom_du_compte)
    VALUES (%s,%s,%s,%s)"""
value = (maxi,e_mail,code,nom_de_compte)
cursor.execute(sql, value)
#validé la modification
myConnection .commit()
count = cursor .rowcount
#---------------------partie html 

print(html)
print("""Inscription validé <br>
notez bien vos informations""")
print(f"""<table>  <tr> <td> identifiant : </td>  <td>{e_mail} </td></tr> 
<tr> <td> code :  </td> <td>{code}  </td></tr></table>""")
print(htmlf)
