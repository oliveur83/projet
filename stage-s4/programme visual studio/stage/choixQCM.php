   <!--   1er page de choix de QCM-->
<?php
// On démarre la session AVANT d'écrire du code HTML
session_start();

//  quelques variables de session dans $_SESSION qui nous servent pour QCM plus tard
$_SESSION['e_mail'] =$_POST['i_mail'] ;// variable pour e-mail 
$_SESSION['mp'] =$_POST['i_mp'] ;//variable pour le mot de passe
?>

<!DOCTYPE html>
        <FONT size="5"> <!--ecriture a une certaine taille  -->
<head>
	<link rel="stylesheet" href="choixQCM.CSS">
</head>
<html>
        <body> 
<?php
                $var_t= 0; // verifie dans la base si oui ou non les identifant et mp sont juste 

                $bdd= new PDO ('mysql:host=localhost;dbname=stage_s4','root','');
                $req=$bdd->query("SELECT* FROM utilisateur");
           
                while ($ligne= $req->fetch())// test pour si c'est un vrai compte ou nono
                         { 
                                 if($_POST['i_mail'] ==$ligne['e_mail'] AND $_POST['i_mp']==$ligne['mot_de_passe'])
                                         {
                                         $var_t= 1;
                                        }

                        }   
                if($var_t==1)// si tout est bon 
                {
 ?>  
                 <div class="droite">  <!-- creation du bouton deconnexion -->
                         <form method="post" action="index.php">
                                 <input type ="submit"value="Déconnexion"style=";height:30px;font-size:20px" />
                        </form>      
                 </div> 

          <p><?php echo "<b>";  ?>Questionnaires à choix multiple (QCM)<?php echo "</b>";  ?></p>

                 <form method="post" action="affichage_des_question.php">
                          <input type ="submit" value="QCM1-Acte transfusionnel"style=";height:30px;font-size:20px" />
                         <input type="text" name="toto" value="1" style="display:none" /> <!--  pour affichage des question.php savoir quelle QCM il a cliqué-->
                </form>

                 <form method="post" action="affichage_des_question.php">
                         <input type ="submit" value="QCM2-Les bases théoriques en immuno hématologie (IH) "style="height:30px;font-size:20px" />
                         <input type="text" name="toto" value="2" style="display:none" /><!--  pour affichage des question.php savoir quelle QCM il a cliqué-->
                 </form>

                 <form method="post" action="affichage_des_question.php">
                         <input type ="submit" value="QCM3-Le contrôle pré-transfusionnel"style="height:30px;font-size:20px" />
                         <input type="text" name="toto" value="3" style="display:none" /><!--  pour affichage des question.php savoir quelle QCM il a cliqué-->
                 </form>
                 <form method="post" action="affichage_des_question.php">
                         <input type ="submit" value="QCM4-Evènements indésirables receveurs"style="height:30px;font-size:20px" />
                        <input type="text" name="toto" value="4" style="display:none" /><!--  pour affichage des question.php savoir quelle QCM il a cliqué-->
                </form>
                <form method="post" action="affichage_des_question.php">
                        <input type ="submit" value="QCM5-Prescription d’examens d’immuno hématologie et
 prescription de produits sanguins labiles IDE"style="height:30px;font-size:20px" />
                        <input type="text" name="toto" value="5" style="display:none" /><!--  pour affichage des question.php savoir quelle QCM il a cliqué-->
                </form>
                <form method="post" action="affichage_des_question.php">
                        <input type ="submit" value="QCM6-Règle de compatibilité en transfusion "style="height:30px;font-size:20px" />
                        <input type="text" name="toto" value="6" style="display:none" /> <!--  pour affichage des question.php savoir quelle QCM il a cliqué-->
                </form>           
    <div class="gauche"> 
            <input type="image" src="point.jpg" height='30' onclick="popup('aleatoire.php')" />  
         </div> 
                 <form method="post" action="afficherdesquestionRAMDOM.php">
                 <input type="text" name="toto" value="1" style="display:none" />
                    <input type ="submit" value="QCM7-Mode aléatoire" style="height:30px;font-size:20px"/>
                 </form>     
                 
     <script LANGUAGE="JavaScript"> 
        function popup(tmp)
    { 
        window.open(tmp,'popup','width=200,height=100,toolbar=false,scrollbars=false'); 
    } 
        </script> 
            <p><?php echo "<b>";  ?>Questionnaire à choix multiple (QCM) pour le personnel inscrit en
             formation continue en médecine transfusionnelle<?php echo "</b>";  ?></p>

                  <form method="post" action="codesQCM.php">
                        <input type ="submit" value="QCM8-Questionnaire d’évaluation PRE-FORMATION"style="height:30px;font-size:20px" />
                        <input type="text" name="toto" value="8" style="display:none" />
                 </form>
                 <form method="post" action="codesQCM.php">
                        <input type ="submit" value="QCM9 -Questionnaire d’évaluation POST-FORMATION " style="height:30px;font-size:20px"/>
                        <input type="text" name="toto" value="8" style="display:none" />       
                 </form>  
                 <div class="droite">
                        <form method="post" action="contact.php">
                                <input type ="submit" value=" Nous contacter"style="height:30px;font-size:20px" />
                        </form>
                </div> 
 <?php 
                }
                 else // si yen a un qui est faux 
                {
                        echo "Il y a une erreur dans ton mot de passe ou ton e-mail."
   ?> 
                         <form method="post" action="connexion.php">
                                  <input type ="submit" value="retour " />
                         </form> 
 <?php
                 } 
  ?> 
        </body>
</html>