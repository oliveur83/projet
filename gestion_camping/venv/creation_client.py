#coding: utf-8
# cette page est accueil de notre site 
print("Content-type: text/html; charset=unicode\n")

import cgi 
import cgitb

cgitb.enable()
form=cgi.FieldStorage()
#---------------session---------------
e_mail=form.getvalue('e_mail')
code=form.getvalue('code')

# faire par rapport a la saison 
html = """<!DOCTYPE html>
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

<form action="validation_client.py" method="post">
    nom :<input type="text" name="nom"/><br>
    prenom:<input type="text" name="prenom"/><br>
    date de naissance:<input type="date" name="date_de_naissance"/><br>
    adresse: <input type="text" name="adresse"/><br>
    telephone: <input type="text" name="telephone"/><br>
    adresse mail : <input type="text" name="adresse_mail"/><br>
     <input  type="submit" value="valider " />"""
finform="""
    </form>"""
html1="""
    <form action="reservation.py" method="post">
    <input  type="submit" value="retour" />
</form>
</center> 
</body>
</html>
"""

print(html)
print(f"""<input  name="e_mail" type="hidden" value="{e_mail}">""")
print(f"""<input  name="code" type="hidden" value="{code}">""")
print(finform)
print(html1)