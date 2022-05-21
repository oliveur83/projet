# coding: utf-8
# cette page est accueil de notre site 
print("Content-type: text/html; charset=unicode\n")

import psycopg2
import cgi 
import cgitb
import datetime
from datetime import timedelta

cgitb.enable()
form=cgi.FieldStorage()

date = datetime.date.today()

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
        <h1>restaurant</h1> 

      </div>
  </center> 
</body>
</html>
"""

print(html)


