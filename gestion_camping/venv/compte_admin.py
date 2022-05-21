# coding: utf-8
# cette page est accueil de notre site 
print("Content-type: text/html; charset=unicode\n")
import cgi 
import cgitb
import psycopg2

cgitb.enable()
form=cgi.FieldStorage()

valeur=form.getvalue('valeur')
annule=form.getvalue('annule')
present=form.getvalue('present')
act=form.getvalue('act')
du=form.getvalue('du')
prix=form.getvalue('prix')
emplacement=form.getvalue('emplacement')
typee=form.getvalue('type')
id_emplacement=form.getvalue('id_emplacement')



htmld = """<!DOCTYPE html>
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

        #div {
        float:left;
          border: 5px ridge #000;
          background-color: #ffF;
          width:300px;
					height:250px;
        }
        #div1 {
        float:left;
          border: 5px ridge #000;
          background-color: #ffF;
          width:300px;
					height:250px;
        }
        #div2 {
            float:left;
          border: 5px ridge #000;
          background-color: #ffF;
          width:920px;
        }
      </style>
    </head>
<body>
    <div id="div">
    <h3> statistique:</h3>
        <form action="compte_admin.py" method="post">
           1) <input  type="submit" name="valeur" value="nombre de personne sur le camping" />
         </form>
        <form action="compte_admin.py" method="post">
            2)<input  type="submit" name="valeur" value="nombre de reservation sur le camping" />
        </form>
        <form action="compte_admin.py" method="post">
            3)<input  type="submit" name="valeur" value="nombre de reservation pour le camping" />
        </form>

        <form action="compte_admin.py" method="post">
           4) type de selection :
            <select name="annule">
                <option value="0">reservation annule</option>
                <option value="1"> ce qui sont venu </option>
                <option value="2"> les deux </option>
            </select>
            <input  type="submit" name="valeur" value="nombre de reservation depuis sont ouverture" />
         </form>
    </div>
    <div id="div">
            <h3> insertion/modifier emplacement:</h3>
        <form action="compte_admin.py" method="post">
        <input  type="submit" name="valeur" value="tout les emplacement" />
        </form>

            <form action="compte_admin.py" method="post">
                nom de emplacement:   <input type="texte" name="emplacement" value="" />
                <input  type="submit" name="valeur" value="ajoute un emplacement" />
            </form>
            <form action="compte_admin.py" method="post">
            <table> 
                <tr>
                   <td> type de location: </td><td><input type="texte" name="type" value="" /></td>
                </tr>
                <tr>
                   <td> numéro emplacement :</td><td><input type="texte" name="id_emplacement" value="" /></td>
                </tr>
            </table> 
                    <input  type="submit" name="valeur" value="modifier un emplacement" />
            </form>
    </div>
    <div id="div">
        <h3> insertion activité</h3>
            <form action="compte_admin.py" method="post">
                <input  type="submit" name="valeur" value="nos activite" />
            </form>
            <form action="compte_admin.py" method="post">
            <table> 
                <tr>
               <td> nom activite: </td><td>  <input type="texte" name="act" value="" /></td>
                </tr>
                <tr>
                <td>duree:</td><td><input type="texte" name="du" value="" /></td>
                </tr>
                <tr>
               <td> prix par personne :</td><td><input type="texte" name="prix" value="" /></td>
                </tr>
                </table> 
                <input  type="submit" name="valeur" value="ajoute une activite" />
            
            </form>
    </div>


    
<div id="div1">
    <h3> création d'un tournoi </h3>
    <form action="validation_tournoi.py" method="post">
        <table> 
            <tr>
                <td>type de tournoi que vous voulez:</td><td>
                    <select name="type">
                        <option value="tennis">tennis</option>
                        <option value="petanque"> petanque</option>
                        <option value="flechette"> flechett</option>
                    </select></td>
                </tr>
                <tr>
                <td>nombre de participant:</td><td><input type="text" name="nombre_particiapnt"  value="2"/></td>
                </tr>
                <tr>
                <td>l'heure :</td><td><input type="time" name="heure"  value="2"/></td>
                </tr>
                <tr>
               <td> date du tournoi:</td><td><input type="date" name="date" /></td>
                </tr>
       </table> 
        <input  type="submit" name="valeur" value="creation tournoi" />
    </form>    
</div>
<div id="div1">
    <h3>  reservation</h3>
    <form action="compte_admin.py" method="post">
            type de selection :
            <select name="annule">
                <option value="0">reservation annule</option>
                <option value="1"> ce qui sont venu </option>
                <option value="2"> les deux </option>
            </select>
        <input  type="submit" name="valeur" value="voir tout les reservation passe" />
    </form>
    <form action="compte_admin.py" method="post">
    arrivé:
            <select name="present">
                <option value="0"> non </option>
                <option value="1"> oui</option>
                <option value="2"> les deux </option>
            </select>
        <input  type="submit" name="valeur" value="voir tout les reservation en cours" />
    </form>
</div>
<div id="div1">
<center>
    <br><br><br><br><br><br>
    <form action="index.py" method="post">
        <input  type="submit" name="valeur" value="deconnexion" />
    </form>
    </center> 
</div>

</body>
</html>
"""
table="""<table> 
   <tr>
        <th>id_client</th>
       <th>Nom</th>
       <th>prenom</th>
       <th>tel</th>
        <th>e-mail</th>
         <th>adresse</th>
         <th>groupe </th>
   </tr>"""
#------------------connection----------
hostname = 'localhost'  
username = 'postgres'
password = '@toto83DBZ'
database = 'camping'
data1="camping.camping_client"
data2="camping.reservation"
TableTesthisr = "camping.reservation_historique"
TableTesthisc = "camping.client_historique"

myConnection = psycopg2.connect( host=hostname, user=username,
password=password, dbname=database )
if myConnection :
    cursor =myConnection .cursor()
if valeur== "nombre de personne sur le camping":
    req = ("SELECT count(id_profil_client) FROM {} FULL JOIN {} ON camping_client.id_reservation = reservation.id_reservation where s_est_presente=1".format(data1,data2))
    print(htmld)
    cursor.execute(req)
    data = cursor.fetchall() 
    print("""<div id="div2">
        <center>
        <h1>  resultat</h1>
     """)
    print(f""" <FONT size="5pt"> il y a {data[0][0]} deux personne sur le camping </FONT>""")
    print(""" </center> 
    </div>""")
elif valeur== "nombre de reservation sur le camping":
    req = ("SELECT count(id_reservation) FROM {} ".format(data2))
    print(htmld)
    cursor.execute(req)
    data = cursor.fetchall() 
    print("""<div id="div2">
        <center>
        <h1>  resultat</h1>
     """)
    print(f""" <FONT size="5pt">il y a {data[0][0]} reservation  sur le camping </FONT>""")
    print(""" </center> 
    </div>""")
elif valeur== "nombre de reservation pour le camping":
    req = ("SELECT count(id_reservation) FROM {} where s_est_presente=0 ".format(data2))
    print(htmld)
    cursor.execute(req)
    data = cursor.fetchall() 
    print("""<div id="div2">
        <center>
        <h1>  resultat</h1>
     """)
    print(f"""<FONT size="5pt"> il y a {data[0][0]} reservation  sur le camping </FONT>""")
    print(""" </center> 
    </div>""")
elif valeur== "nombre de reservation depuis sont ouverture":
    print(htmld)

    if annule=='2':
        req = ('SELECT * from {}'.format(TableTesthisr))
        cursor.execute(req)
        his = cursor.fetchall() 
        longe=len(his)
        print("""<div id="div2">
        <center>
        <h1>  resultat</h1>
        
     """)
        print(f""" <FONT size="5pt"> il y a eu {longe} reversation depuis sont debut </FONT><br>""")
        print(""" </center> 
    </div>""")
    else:
        req = ('SELECT * from {} where a_annule={}'.format(TableTesthisr,annule))
        cursor.execute(req)
        his = cursor.fetchall() 
        longe=len(his)
        print("""<div id="div2">
        <center>
        <h1>  resultat</h1>
     """)
        print(f"""<FONT size="5pt">  il y a eu {longe} reversation depuis sont debut</FONT> <br>""")
        print(""" </center> 
    </div>""")
    #---------------------------------------------------------------------------
elif valeur== "voir tout les reservation passe":
    print(htmld)
    if annule=='2':
        req = ('SELECT * from {}'.format(TableTesthisr))
        cursor.execute(req)
        his = cursor.fetchall() 
        i=0
        longe=len(his)
        print("""<div id="div2">
        <center>
        <h1>  resultat</h1>
        <table> 
       <tr>  
            <td> numéro du compte </td> 
            <td> nombre de personne </td> 
            <td> nombre de place prise</td> 
            <td> presente </td> 
            <td> annule </td> 
            <td> demi pension  </td> 
            <td> numéro emplacement</td> 
            <td> date de debut </td> 
            <td> date de fin  </td> 
            <td> revenu </td> 
       </tr>
     """)
        while i<longe:
            print(f"""<tr> 
            
           <td> {his[i][0]}</td> 
        <td> {his[i][1]}</td> 
        <td> {his[i][2]}</td> 
        <td> {his[i][3]}</td> 
         <td> {his[i][4]}</td> 
        <td> {his[i][5]}</td> 
        <td> {his[i][6]}</td> 
        <td> {his[i][7]}</td> 
        <td> {his[i][8]}</td> 
        <td> {his[i][9]}</td> 
            
            </tr> """)
            i=i+1
        print(""" </table> </center> 
    </div>""")
    else:
        req = ('SELECT * from {} where a_annule={}'.format(TableTesthisr,annule))
        cursor.execute(req)
        his = cursor.fetchall() 
        i=0
        longe=len(his)
        print("""<div id="div2">
        <center>
        <h1>  resultat</h1>
        <table> 
       <tr>  
            <td> numéro du compte </td> 
            <td> nombre de personne </td> 
            <td> nombre de place prise</td> 
            <td> presente </td> 
            <td> annule </td> 
            <td> demi pension  </td> 
            <td> numéro emplacement</td> 
            <td> date de debut </td> 
            <td> date de fin  </td> 
            <td> revenu </td> 
       </tr>
     """)
        while i<longe:
            print(f"""<tr> 
            
           <td> {his[i][0]}</td> 
        <td> {his[i][1]}</td> 
        <td> {his[i][2]}</td> 
        <td> {his[i][3]}</td> 
         <td> {his[i][4]}</td> 
        <td> {his[i][5]}</td> 
        <td> {his[i][6]}</td> 
        <td> {his[i][7]}</td> 
        <td> {his[i][8]}</td> 
        <td> {his[i][9]}</td> 
            
            </tr> """)
            i=i+1
        print(""" </table></center> 
    </div>""")
elif valeur== "voir tout les reservation en cours":
    print(htmld)
    if present=='2':
        req = ('SELECT * from {}'.format(data2))
        cursor.execute(req)
        his = cursor.fetchall() 
        i=0
        longe=len(his)
        print("""<div id="div2">
        <center>
        <h1>  resultat</h1>
        <table> 
       <tr>  
            <td> numéro de la reservatin </td> 
            <td> numéro emplacement</td> 
            <td> numéro du compte </td> 
            <td> presente </td> 
            <td> date de debut </td> 
            <td> date de fin  </td> 
            <td>nombre de personne </td> 
             <td> nombre de place prise</td> 
            <td> demi pension</td> 
       </tr>
     """)
        while i<longe:
            print(f"""<tr> 
            
           <td> {his[i][0]}</td> 
        <td> {his[i][1]}</td> 
        <td> {his[i][2]}</td> 
        <td> {his[i][3]}</td> 
         <td> {his[i][4]}</td> 
        <td> {his[i][5]}</td> 
        <td> {his[i][6]}</td> 
        <td> {his[i][7]}</td> 
        <td> {his[i][8]}</td> 
            </tr> """)
            i=i+1
        print(""" </table></center> 
    </div>""")
    #-------------------------------------
    else:
        req = ('SELECT * from {} where s_est_presente={}'.format(data2,present))
        cursor.execute(req)
        his = cursor.fetchall() 
        i=0
        longe=len(his)
        print("""<div id="div2">
        <center>
        <h1>  resultat</h1>
        <table> 
       <tr>  
            <td> numéro de la reservatin </td> 
            <td> numéro emplacement</td> 
            <td> numéro du compte </td> 
            <td> presente </td> 
            <td> date de debut </td> 
            <td> date de fin  </td> 
            <td>nombre de personne </td> 
             <td> nombre de place prise</td> 
            <td> demi pension</td> 
       </tr>
     """)
        while i<longe:
            print(f"""<tr> 
            
           <td> {his[i][0]}</td> 
        <td> {his[i][1]}</td> 
        <td> {his[i][2]}</td> 
        <td> {his[i][3]}</td> 
         <td> {his[i][4]}</td> 
        <td> {his[i][5]}</td> 
        <td> {his[i][6]}</td> 
        <td> {his[i][7]}</td> 
        <td> {his[i][8]}</td> 
            
            </tr> """)
            i=i+1
        print("""</table> </center> 
    </div>""")
    #--------------------------------
elif valeur== "nos activite":
    req = ("SELECT * FROM camping.activite ")
    print(htmld)
    cursor.execute(req)
    data = cursor.fetchall() 
    i=0
    longe=len(data)
    print("""<div id="div2">
        <center>
        <h1>  resultat</h1>
        
     """)
    while i<longe:
        print(f""" {data[i][1]},    """)
        i=i+1
    print(""" </center> 
    </div>""")
elif valeur== "ajoute une activite":
    req = ("SELECT max(id_activite) FROM camping.activite ")
    print(htmld)
    cursor.execute(req)
    data = cursor.fetchall() 
    idd=data[0][0]+1
    sql = """INSERT INTO camping.activite(id_activite,nom_act,duree_act,prix_1pers__act)
    VALUES (%s,%s,%s,%s)"""
    value = (idd,act,int(du),prix)
    cursor.execute(sql, value)
    myConnection .commit()
    count = cursor .rowcount
    print("""<div id="div2">
        <center>
        <h1>  resultat</h1>
        <FONT size="5pt">
     """)
    print("    votre création est bien enregistré </FONT>")
    print(""" </center> 
    </div>""")
elif valeur=="ajoute un emplacement":
    req = ("SELECT max(id_emplacement) FROM camping.emplacement ")
    print(htmld)
    cursor.execute(req)
    data = cursor.fetchall() 
    idd=data[0][0]+1
    sql = """INSERT INTO camping.emplacement(id_emplacement,type_emplacement)
    VALUES (%s,%s)"""
    value = (idd,emplacement)
    cursor.execute(sql, value)
    myConnection .commit()
    count = cursor .rowcount
    print("""<div id="div2">
        <center>
        <h1>  resultat</h1>
        <FONT size="5pt">
     """)
    print(" votre création est bien enregistré  </FONT>")
    print(""" </center> 
    </div>""")
elif valeur=="tout les emplacement":
    print(htmld)
    req = 'SELECT * from camping.emplacement'
    cursor.execute(req)
    his = cursor.fetchall() 
    i=0
    longe=len(his)
    print("""<div id="div2">
        <center>
        <h1>  resultat</h1>
        <table> 
       <tr>  
            <td> numéro emplacement</td> 
            <td> type </td> 
       </tr>
     """)
    while i<longe:
        print(f"""       <tr>  
            <td> {his[i][0]}</td> 
            <td> {his[i][1]}</td> 
       </tr> """)
        i=i+1
    print("""</table> </center> 
    </div>""")
elif valeur=="modifier un emplacement":
    print(htmld)
    req = ("UPDATE camping.emplacement SET type_emplacement='{}' where id_emplacement={} ".format(typee,id_emplacement))
    cursor.execute(req)
    myConnection .commit()
    count = cursor .rowcount
    print("""<div id="div2">
        <center>
        <h1>  resultat</h1>
        <FONT size="5pt">
     """)
    print(" la modification est bien enregistré  </FONT>")
    print(""" </center> 
    </div>""")
else: 
    print(htmld)
    print("""<div id="div2">
            </div>
     """)