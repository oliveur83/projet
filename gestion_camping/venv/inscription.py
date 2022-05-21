#coding: utf-8
# cette page est accueil de notre site 
print("Content-type: text/html; charset=unicode\n")


# faire par rapport a la saison 
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
  <div>
        <form action="validation_inscription.py" method="post">
          <h1> création du compte</h1>
          <br>

          tous les informations demandées sont obligatoire !<br>
          <table>    
          <tr>
          <td>e-mail: </td><td><input type="text" name="e_mail"/></td>
          </tr>
          <tr>
         <td> nom de compte: </td><td><input type="text" name="nom_de_compte"/></td>
          </tr>
          <tr>
         <td> code identification:</td> <td><input type="password" name="code"/></td>
          </tr>
          </table>
          
          <input  type="submit" value="valider " />
        </form>
        <form action="index.py" method="post">
          <input  type="submit" value="retour" />
        </form>
  </div>
</center> 
</body>
</html>
"""

print(html)