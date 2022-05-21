# coding: utf-8
# cette page est accueil de notre site 
print("Content-type: text/html; charset=unicode\n")

import cgi 
import cgitb
import psycopg2
cgitb.enable()
form=cgi.FieldStorage()

e_mail=form.getvalue('e_mail')


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
          border: 5px ridge #000;
          background-color: #ffF;
          width:300px;
					height:200px;
        }
      </style>
    </head>
<body> 
      <center>
  <div></div> 
    <table border="1px">
</div>
"""
htmlf="""
    </table>

       <form action="compte.py" method="post">
        <input  type="submit" value="retour" />
          </form>  
  
  </center> 
</body>
</html>
"""
htmld1 = """<!DOCTYPE html>
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
  
      <form action="compte.py" method="post">
          <input  type="submit" value="retour" />
"""

htmlf1="""

 </form>
       
  </center> 
</body>
</html>
"""


#------------------connection----------
hostname = 'localhost'  
username = 'postgres'
password = '@toto83DBZ'
database = 'camping'
TableTest1 = "camping.reservation"
TableTest2 = "camping.compte"

myConnection = psycopg2.connect( host=hostname, user=username,
password=password, dbname=database )
if myConnection :
    cursor =myConnection .cursor()
req = ("SELECT id_compte from {} where e_mail_compte='{}'".format(TableTest2,e_mail))
cursor.execute(req)
data = cursor.fetchall()  
id_client=data[0][0]
req = ('SELECT id_reservation,date_deb,date_fin from {} where id_compte={} '.format(TableTest1,id_client))
cursor.execute(req)
data = cursor.fetchall()  
i=0
if (data==[]):
    print(htmld1)
    print("""vous n'avez aucune reservation """)
    print(f"""<input  name="id_client" type="hidden" value="{id_client}">""")
    print(f"""<input  name="code" type="hidden" value="{code}">""")
    print(htmlf1)
else:
    n=len(data)
    print(htmld)
    while(i<n):

        print(f"<tr><td>{data[i][0]}</td><td>{data[i][1]}</td><td>{data[i][2]}</td>")
        print(f""" <td>
        <form action="validation_annulation.py" method="post">
        <input  type="submit" name="bouton" value="annule" /> </td> 
        <td><input  type="hidden" name="annule" value="{data[i][0]}" />
         </form>
         </td></tr>""")
        i=i+1
    print(htmlf)