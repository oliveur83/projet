<?php
session_start();
$_SESSION['numQCM'] =$_POST['toto'] ;// variable num QCM
?>
<!DOCTYPE html><FONT size="5">
<html>
<body><head>
	<link rel="stylesheet" href="choixQCM.CSS">
</head>
<form method="post" action="affichage_des_question20.php">
        <p>Veuillez saisir le mot de passe communisqué par l'équipe de formation  </p> 
        <p>Mot de passe<input type="password" name="i_cmp" /> </p>
    <?php 

      echo "<br>"  ?> 
     <input type ="submit" value="Valider"style=";height:30px;font-size:20px" />
</form>
<div class="droite">
<form method="post" action="choixQCM2.php">
             <input type ="submit" value="Retour"style=";height:30px;font-size:20px" />
</form>  </div>  
</body>
</html>