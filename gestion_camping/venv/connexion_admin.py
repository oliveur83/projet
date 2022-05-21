# coding: utf-8
# cette page est accueil de notre site 
print("Content-type: text/html; charset=unicode\n")

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
    <h1>connexion </h1> 
      <form action="compte_admin.py" method="post">
      <table> 
        <tr>
              <td> e_mail: </td> <td> <input type="texte" name="e_mail" value="" /></td>
        </tr>
        <tr>
            <td>  code:  </td><td>  <input type="password" name="code" value="" /></td>
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