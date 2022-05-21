 <!--2eme page de choix QCM cette page est appelé a chaque fin de QCM -->
<?php
// On démarre la session AVANT d'écrire du code HTML
session_start();

$_SESSION['numeroquestion']=0; // variable pour affiche le nombre de question
// On s'amuse à créer quelques variables de session dans $_SESSION
$_SESSION['Cmp']="rien"
?>

<!DOCTYPE html>
<FONT size="5">
<head>
	<link rel="stylesheet" href="choixQCM.CSS">  <!--source fichier CSS  -->
</head>
<html>
<body> 
      <div class="droite">
                <form method="post" action="index.php">
                     <input type ="submit"value="Déconnexion"style=";height:30px;font-size:20px" />
                 </form>     
        </div> 
            <p><?php echo "<b>";  ?>Questionnaires à choix multiple (QCM)<?php echo "</b>";  ?></p>

                 <form method="post" action="affichage_des_question.php">
                         <input type ="submit" value="QCM1-Acte transfusionnel"style=";height:30px;font-size:20px" />
                         <input type="text" name="toto" value="1" style="display:none" /><!--  pour affichage des question.php savoir quelle QCM il a cliqué-->
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
                                 <input type ="submit" value="QCM7-Mode aléatoire" style="height:30px;font-size:20px"/>
                    <input type="text" name="toto" value="1" style="display:none" /> <!--  pour affichage des question.php savoir quelle QCM il a cliqué-->
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
                    <input type ="submit" value="QCM8-Questionnaire d’évaluation PRE-FORMATION
"style="height:30px;font-size:20px" />
                        <input type="text" name="toto" value="8" style="display:none" /><!--  pour affichage des question.php savoir quelle QCM il a cliqué-->
            </form>
            <form method="post" action="codesQCM.php">
                         <input type ="submit" value="QCM9 -Questionnaire d’évaluation POST-FORMATION " style="height:30px;font-size:20px"/>
                        <input type="text" name="toto" value="8" style="display:none" />   <!--  pour affichage des question.php savoir quelle QCM il a cliqué-->

            </form>
            <div class="droite">
                         <form method="post" action="contact.php">
                                 <input type ="submit" value=" Nous contacter"style="height:30px;font-size:20px" />
                        </form>
                </div> 

 
</body>
</html>