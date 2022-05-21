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
          width:500px;

        }
      </style>
    </head>
<body>

<center> 
<div>
    information:<br>
    Bonjour à tous <br>
    Le camping propose plusieurs types d'emplacements telles que:<br>
    <table>
    <tr>
    <th> Tente</th> <th>nombre de places</th>
    </tr>
    <tr>
    <th> Tente</th> <th> 6 </th>
    </tr>
    <tr>
    <th>Caravane/Campingcar</th> <th> 6  </th>
    </tr>
    <tr>
     <th>Mobilehome </th><th> 6  </th>
    </tr>
    </table>
    Chalets bientôt disponibles sur le camping soyez patient ! <br>

    prix par emplacement :<br>
    <table>
    <tr>
    <th>EMPLACEMENT</th>
    <th>jour</th>
    <th>semaine</th>
    <th>mois</th>
    </tr>  
    <tr>
    <th>Tente</th>
    <th>10</th>
    <th>60</th>
    <th>100</th>
    </tr>  
    <tr>
    <th>Caravane/campingcar</th>
    <th>20</th>
    <th>120</th>
    <th>450</th>
    </tr>  
    <th>Mobile home 6 personne </th>
    <th>50</th>
    <th>300</th>
    <th>800</th>
    </tr>  
    <th>Mobilehome 8 personne</th>
    <th>75</th>
    <th>500</th>
    <th>1800</th>
    </tr>  
    </table><p>
    Option demi-pension disponbile!<br>
    Qui vous offre dîner gratuit au restaurant Gusto<br>

    Réservation à la semaine 10 % de remise <br>
    Résetvation au mois 20 % de remise <br> 
    une offre a pas manque <br>

    Emplacement voiture à 20.00 euros et 16.99 euros par voiture supplémentaire <br>
    les emplacements bicyclette sont gratuits <br></p>  
<form action="index.py" method="post">
<input  type="submit" value="retour" />
</form>
</div>
</center> 
</body>
</html>
"""

print(html)