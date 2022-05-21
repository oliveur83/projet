# coding: utf-8


import psycopg2
import cgi 
import cgitb
import datetime
date = datetime.date.today()

print("Content-type: text/html; charset=unicode\n")
cgitb.enable()
form=cgi.FieldStorage()

e_mail=form.getvalue('e_mail')
code=form.getvalue('code')
#-------------------------------------
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
  <h2>compte</h2> """
deconnexion="""
    <form action="index.py" method="post">
      <input  type="submit" value="deconnexion" />
      </form>
    """
information=("""
    <form action="information.py" method="post">
    <input  type="submit" value="information sur le camping" />
    <input  name="e_mail" type="hidden" value="{}">
    </form>
    """.format(e_mail))
reservation=("""
      <form action="reservation.py" method="post">
      <input  type="submit" value="reservation " />
      <input  name="e_mail" type="hidden" value="{}">
      <input  name="code" type="hidden" value="{}">
      </form>
    """.format(e_mail,code))
annulation=("""
      <form action="annulation.py" method="post">
      <input  type="submit" value="pour annulé votre reservation" />
      <input  name="e_mail" type="hidden" value="{}">
      </form>
   """.format(e_mail))
act=("""
      <form action="restaurant.py" method="post">
      <input  type="submit" value="nos restaurant " />
      <input  name="e_mail" type="hidden" value="{}">
      </form>
   """.format(e_mail))
restaurant =("""
      <form action="restaurant.py" method="post">
      <input  type="submit" value="resataurant" />
      <input  name="e_mail" type="hidden" value="{}">
      </form>
   """.format(e_mail))


htmlf="""
</div>   
</center>
</body>
</html>
"""

html2="""
<!DOCTYPE html>
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
  <br><br><br><br>
      <form action="connexion.py" method="post">
      votre identifiant ou code est faux !veuillez reessayez
      <input  type="submit" value="retour" />
       </div>
    </form>
      </center>
     """
#------------------connection----------
hostname = 'localhost'  
username = 'postgres'
password = '@toto83DBZ'
database = 'camping'
TableTest1 = "camping.compte"
TableTest2 = "camping.tournoi"
myConnection = psycopg2.connect( host=hostname, user=username,
password=password, dbname=database )
if myConnection :
    cursor =myConnection .cursor()

 # Requete SQL pour avoir tout les compte
req = ('SELECT e_mail_compte,mp_compte from {}'.format(TableTest1))
cursor.execute(req)
data = cursor.fetchall() 
# on prend le maximum 
req = ('SELECT max(id_compte) from {}'.format(TableTest1))
cursor.execute(req)
maxi = cursor.fetchall()    
maxir=maxi[0][0]
i=0
var=0

while(i<maxir):
    if (e_mail==data[i][0]and code==data[i][1]):
        var=1
    i=i+1
if (var==1):
    print(html)
    print(deconnexion)
    print(reservation)
    print(annulation)
    print(act)
    print(restaurant)
    print(information)
    req = ('SELECT * from {}'.format(TableTest2))
    cursor.execute(req)
    data = cursor.fetchall() 
    i=0
    longe=len(data)
    while i<longe:
      if date==data[i][4]:
        print(f""" 
        Bonjour! aujourd'hui c'est tournoi de {data[i][1]}<br>
        Inscription ici
              <form action="inscription_tournoi.py" method="post">
            <input  type="submit" value="inscription au tournoi" />
            <input  type="hidden" name="e_mail" value="{e_mail}" />
            <input  type="hidden" name="id_tournoi" value="{data[0][0]}" />
          </form>
          """)
      i=i+1
else:
    print(html2)
print(htmlf)
